"""Run fetch → clean in one command: `python -m src.run_pipeline`."""

from __future__ import annotations

import logging
import sys

import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    """Fetch IPC, WHO, and UNHCR sources then write the analysis table."""
    from src.clean import build_analysis_table
    from src.fetch_hdx import fetch_ipc
    from src.fetch_unhcr import fetch_unhcr
    from src.fetch_who import fetch_u5mr

    print("=== 1/4 IPC (HDX) ===")
    fetch_ipc()
    print("=== 2/4 WHO U5MR ===")
    fetch_u5mr()
    print("=== 3/4 UNHCR displacement ===")
    try:
        fetch_unhcr()
    except (RuntimeError, requests.RequestException, OSError) as exc:
        logger.warning("UNHCR fetch failed: %s", exc)
        print(f"UNHCR fetch failed: {exc}")
        print("If you added data/raw/unhcr_manual.csv, clean will still work.")
    print("=== 4/4 Clean / join ===")
    build_analysis_table()
    print("Done. Launch with: streamlit run app.py")


if __name__ == "__main__":
    main()
    sys.exit(0)
