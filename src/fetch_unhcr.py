"""Fetch hosted displacement statistics from the UNHCR Population API."""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any

import pandas as pd
import requests

from src.config import (
    FOCUS_ISO3,
    HTTP_TIMEOUT_SECONDS,
    RAW_DIR,
    UNHCR_API_PAGE_LIMIT,
    UNHCR_POPULATION_URL,
    UNHCR_YEAR_FROM,
    UNHCR_YEAR_TO,
    USER_AGENT,
)

logger = logging.getLogger(__name__)


def _to_number(value: Any) -> float:
    """Coerce UNHCR cell values (including '-') to float; missing becomes 0."""
    if value is None or value == "-" or value == "":
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def fetch_unhcr(
    output_dir: Path | None = None,
    year_from: int = UNHCR_YEAR_FROM,
    year_to: int = UNHCR_YEAR_TO,
) -> Path:
    """
    Download hosted REF+ASY+OOC for focus countries of asylum.

    Returns path to unhcr_displacement_focus.csv.
    Requires `coa` + `cf_type=ISO` — omitting `coa` returns a world aggregate.
    """
    output_dir = output_dir or RAW_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    params = [
        ("limit", UNHCR_API_PAGE_LIMIT),
        ("yearFrom", year_from),
        ("yearTo", year_to),
        ("cf_type", "ISO"),
        ("coa", ",".join(FOCUS_ISO3)),
    ]
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}

    try:
        response = requests.get(
            UNHCR_POPULATION_URL,
            params=params,
            headers=headers,
            timeout=HTTP_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(
            f"UNHCR API request failed: {exc}. "
            "Fallback: save data/raw/unhcr_manual.csv with columns iso3,displaced,year"
        ) from exc
    except ValueError as exc:
        raise RuntimeError(f"UNHCR API returned invalid JSON: {exc}") from exc

    raw_path = output_dir / "unhcr_population_raw.json"
    raw_path.write_text(response.text, encoding="utf-8")

    records = payload.get("items") or []
    frame = pd.DataFrame(records)
    if frame.empty:
        raise RuntimeError(
            "UNHCR API returned no rows. Add data/raw/unhcr_manual.csv or check coa filters."
        )

    if "coa_iso" in frame.columns:
        frame["iso3"] = frame["coa_iso"].astype(str).str.upper()
    elif "coa" in frame.columns:
        frame["iso3"] = frame["coa"].astype(str).str.upper()
    else:
        raise RuntimeError(
            f"No asylum country field in UNHCR payload. Columns: {list(frame.columns)}"
        )

    frame = frame[frame["iso3"].isin(FOCUS_ISO3)]

    for col in ["refugees", "asylum_seekers", "ooc"]:
        if col not in frame.columns:
            frame[col] = 0
        frame[col] = frame[col].map(_to_number)

    # Locked definition: refugees + asylum-seekers + others of concern (hosted)
    frame["displaced"] = frame["refugees"] + frame["asylum_seekers"] + frame["ooc"]
    frame["year"] = pd.to_numeric(frame.get("year"), errors="coerce")

    grouped = frame.groupby(["iso3", "year"], as_index=False)["displaced"].sum()
    latest = (
        grouped.sort_values("year")
        .groupby("iso3", as_index=False)
        .tail(1)
        .reset_index(drop=True)
    )

    if latest.empty:
        raise RuntimeError("UNHCR rows present but none matched FOCUS_ISO3.")

    out_csv = output_dir / "unhcr_displacement_focus.csv"
    history_csv = output_dir / "unhcr_displacement_history.csv"
    latest.to_csv(out_csv, index=False)
    grouped.to_csv(history_csv, index=False)
    logger.info("UNHCR displacement saved: %s (%s countries)", out_csv, len(latest))
    print(f"UNHCR displacement saved: {out_csv} ({len(latest)} countries)")
    return out_csv


def main() -> None:
    """CLI entry for `python -m src.fetch_unhcr`."""
    fetch_unhcr()


if __name__ == "__main__":
    main()
    sys.exit(0)
