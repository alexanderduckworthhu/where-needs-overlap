"""Fetch under-5 mortality from WHO Global Health Observatory."""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

import pandas as pd
import requests

from src.config import (
    FOCUS_ISO3,
    HTTP_TIMEOUT_SECONDS,
    RAW_DIR,
    USER_AGENT,
    WHO_GHO_BASE,
    WHO_U5MR_INDICATOR,
)

logger = logging.getLogger(__name__)


def fetch_u5mr(output_dir: Path | None = None) -> Path:
    """Download WHO U5MR for focus countries; returns path to who_u5mr_focus.csv."""
    output_dir = output_dir or RAW_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    url = f"{WHO_GHO_BASE}/{WHO_U5MR_INDICATOR}"
    headers = {"User-Agent": USER_AGENT}
    try:
        response = requests.get(url, headers=headers, timeout=HTTP_TIMEOUT_SECONDS)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"WHO GHO request failed: {exc}") from exc
    except ValueError as exc:
        raise RuntimeError(f"WHO GHO returned invalid JSON: {exc}") from exc

    records = payload.get("value", [])
    raw_path = output_dir / "who_u5mr_raw.json"
    raw_path.write_text(json.dumps(payload), encoding="utf-8")

    frame = pd.DataFrame(records)
    if frame.empty:
        raise RuntimeError("WHO GHO returned no under-5 mortality records.")

    if "SpatialDimType" in frame.columns:
        frame = frame[frame["SpatialDimType"].str.upper() == "COUNTRY"]

    if "Dim1" in frame.columns:
        both_sexes = frame["Dim1"].astype(str).str.upper().isin(
            ["BTSX", "SEX_BTSX", "BOTH SEXES", "NAN", ""]
        )
        if both_sexes.any():
            frame = frame[both_sexes | frame["Dim1"].isna()]

    frame = frame.rename(
        columns={
            "SpatialDim": "iso3",
            "TimeDim": "year",
            "NumericValue": "u5mr",
        }
    )
    keep = [c for c in ["iso3", "year", "u5mr"] if c in frame.columns]
    frame = frame[keep].dropna(subset=["iso3", "u5mr"])
    frame["iso3"] = frame["iso3"].astype(str).str.upper()
    frame["year"] = pd.to_numeric(frame["year"], errors="coerce")
    frame["u5mr"] = pd.to_numeric(frame["u5mr"], errors="coerce")
    frame = frame[frame["iso3"].isin(FOCUS_ISO3)].dropna(subset=["year", "u5mr"])

    latest = (
        frame.sort_values("year")
        .groupby("iso3", as_index=False)
        .tail(1)
        .reset_index(drop=True)
    )

    out_csv = output_dir / "who_u5mr_focus.csv"
    history_csv = output_dir / "who_u5mr_focus_history.csv"
    latest.to_csv(out_csv, index=False)
    frame.to_csv(history_csv, index=False)
    logger.info("WHO U5MR saved: %s (%s countries)", out_csv, len(latest))
    print(f"WHO U5MR saved: {out_csv} ({len(latest)} countries)")
    return out_csv


def main() -> None:
    """CLI entry for `python -m src.fetch_who`."""
    fetch_u5mr()


if __name__ == "__main__":
    main()
    sys.exit(0)
