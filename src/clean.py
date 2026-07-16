"""Clean and join IPC + UNHCR + WHO into one analysis table on ISO3."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

from src.config import (
    FOCUS_ISO3,
    FOCUS_NAMES,
    IPC_OUTPUT_FILENAME,
    IPC_SHARE_TO_PERCENT_CEILING,
    PROCESSED_DIR,
    RAW_DIR,
)
from src.metadata_io import write_metadata


def _load_ipc(path: Path) -> pd.DataFrame:
    """
    Parse HDX IPC national long CSV into per-country Phase 3+ people and percent.

    Returns a DataFrame with iso3, phase3plus_people, phase3plus_pct[, population_ref].
    """
    try:
        frame = pd.read_csv(path)
    except (OSError, pd.errors.ParserError) as exc:
        raise RuntimeError(f"Failed to read IPC file {path}: {exc}") from exc

    cols = {c.lower().strip(): c for c in frame.columns}

    def col(*names: str) -> str | None:
        for name in names:
            if name in cols:
                return cols[name]
        return None

    country_col = col("country", "country_iso3", "iso3")
    phase_col = col("phase")
    number_col = col("number", "population")
    pct_col = col("percentage", "percent")
    validity_col = col("validity period", "validity_period")
    date_col = col("date of analysis", "date_of_analysis")
    pop_col = col("total country population", "total_population")

    if country_col is None or phase_col is None or number_col is None:
        raise RuntimeError(f"Unexpected IPC columns: {list(frame.columns)}")

    work = frame.copy()
    work["iso3"] = work[country_col].astype(str).str.upper()
    work = work[work["iso3"].isin(FOCUS_ISO3)]

    # Prefer current assessment over projections so KPIs stay operationally grounded
    if validity_col:
        current = work[work[validity_col].astype(str).str.lower().eq("current")]
        if not current.empty:
            work = current

    phase3 = work[
        work[phase_col].astype(str).str.strip().isin(["3+", "3 +", "Phase 3+"])
    ].copy()
    if phase3.empty:
        raise RuntimeError("IPC file has no Phase '3+' rows for focus countries.")

    phase3["phase3plus_people"] = pd.to_numeric(phase3[number_col], errors="coerce")
    if pct_col:
        pct = pd.to_numeric(phase3[pct_col], errors="coerce")
        # HDX stores shares (0.28); convert to percent for chart labels
        phase3["phase3plus_pct"] = pct.apply(
            lambda x: x * 100
            if pd.notna(x) and x <= IPC_SHARE_TO_PERCENT_CEILING
            else x
        )
    else:
        phase3["phase3plus_pct"] = pd.NA

    if pop_col:
        phase3["population_ref"] = pd.to_numeric(phase3[pop_col], errors="coerce")

    if date_col:
        phase3["_sort"] = phase3[date_col].astype(str)
        phase3 = phase3.sort_values("_sort")

    keep_cols = ["iso3", "phase3plus_people", "phase3plus_pct"]
    if "population_ref" in phase3.columns:
        keep_cols.append("population_ref")

    return (
        phase3.groupby("iso3", as_index=False)
        .tail(1)[keep_cols]
        .reset_index(drop=True)
    )


def _load_unhcr(path: Path) -> pd.DataFrame:
    """Load hosted displacement CSV; returns iso3, displaced[, displacement_year]."""
    try:
        frame = pd.read_csv(path)
    except (OSError, pd.errors.ParserError) as exc:
        raise RuntimeError(f"Failed to read UNHCR file {path}: {exc}") from exc

    frame["iso3"] = frame["iso3"].astype(str).str.upper()
    if "year" in frame.columns:
        frame = frame.rename(columns={"year": "displacement_year"})
        return frame[["iso3", "displaced", "displacement_year"]]
    return frame[["iso3", "displaced"]]


def _load_who(path: Path) -> pd.DataFrame:
    """Load WHO U5MR CSV; returns iso3, u5mr[, u5mr_year]."""
    try:
        frame = pd.read_csv(path)
    except (OSError, pd.errors.ParserError) as exc:
        raise RuntimeError(f"Failed to read WHO file {path}: {exc}") from exc

    frame["iso3"] = frame["iso3"].astype(str).str.upper()
    if "year" in frame.columns:
        frame = frame.rename(columns={"year": "u5mr_year"})
        return frame[["iso3", "u5mr", "u5mr_year"]]
    return frame[["iso3", "u5mr"]]


def build_analysis_table(
    raw_dir: Path | None = None,
    processed_dir: Path | None = None,
) -> Path:
    """
    Left-join IPC, UNHCR, and WHO onto the focus-country skeleton.

    Writes analysis_table.csv and metadata.json; returns the analysis table path.
    """
    raw_dir = raw_dir or RAW_DIR
    processed_dir = processed_dir or PROCESSED_DIR
    processed_dir.mkdir(parents=True, exist_ok=True)

    ipc_path = raw_dir / IPC_OUTPUT_FILENAME
    unhcr_path = raw_dir / "unhcr_displacement_focus.csv"
    who_path = raw_dir / "who_u5mr_focus.csv"
    manual_unhcr = raw_dir / "unhcr_manual.csv"

    if not ipc_path.exists():
        raise FileNotFoundError(f"Missing {ipc_path}. Run: python -m src.fetch_hdx")
    if not who_path.exists():
        raise FileNotFoundError(f"Missing {who_path}. Run: python -m src.fetch_who")
    if not unhcr_path.exists():
        if manual_unhcr.exists():
            unhcr_path = manual_unhcr
        else:
            raise FileNotFoundError(
                f"Missing {unhcr_path}. Run: python -m src.fetch_unhcr "
                "or add data/raw/unhcr_manual.csv"
            )

    ipc = _load_ipc(ipc_path)
    unhcr = _load_unhcr(unhcr_path)
    who = _load_who(who_path)

    base = pd.DataFrame({"iso3": FOCUS_ISO3})
    base["country"] = base["iso3"].map(FOCUS_NAMES)

    merged = (
        base.merge(ipc, on="iso3", how="left")
        .merge(unhcr, on="iso3", how="left")
        .merge(who, on="iso3", how="left")
    )

    # Illustrative ranking only — not an official severity index
    for col in ["phase3plus_pct", "displaced", "u5mr"]:
        if col in merged.columns:
            merged[f"{col}_z"] = (
                (merged[col] - merged[col].mean()) / merged[col].std(ddof=0)
            ).fillna(0)

    z_cols = [c for c in merged.columns if c.endswith("_z")]
    merged["compound_score"] = merged[z_cols].sum(axis=1) if z_cols else 0
    merged = merged.drop(columns=z_cols, errors="ignore")
    merged = merged.sort_values("compound_score", ascending=False)

    out_path = processed_dir / "analysis_table.csv"
    merged.to_csv(out_path, index=False)
    meta_path = write_metadata(processed_dir)
    print(f"Analysis table written: {out_path}")
    print(f"Metadata written: {meta_path}")
    print(
        merged[
            ["iso3", "country", "phase3plus_people", "phase3plus_pct", "displaced", "u5mr"]
        ].to_string(index=False)
    )
    return out_path


def main() -> None:
    """CLI entry for `python -m src.clean`."""
    build_analysis_table()


if __name__ == "__main__":
    main()
    sys.exit(0)
