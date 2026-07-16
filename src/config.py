"""
Locked project scope and shared constants.

Edit geography only as a deliberate product decision — not mid-build.
"""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
RAW_DIR: Path = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR: Path = PROJECT_ROOT / "data" / "processed"

# Horn of Africa + Sahel — co-occurring crisis contexts for UNICEF / UNHCR / OCHA
FOCUS_ISO3: list[str] = ["BFA", "TCD", "ETH", "MLI", "NER", "SOM", "SSD", "SDN"]

# English names for the analysis table; UI strings live in src.i18n
FOCUS_NAMES: dict[str, str] = {
    "BFA": "Burkina Faso",
    "TCD": "Chad",
    "ETH": "Ethiopia",
    "MLI": "Mali",
    "NER": "Niger",
    "SOM": "Somalia",
    "SSD": "South Sudan",
    "SDN": "Sudan",
}

USER_AGENT: str = "where-needs-overlap-portfolio/0.1 (learning project)"

HDX_IPC_DATASET_ID: str = "global-acute-food-insecurity-country-data"
IPC_RESOURCE_HINT: str = "ipc_global_national_long_latest"
IPC_OUTPUT_FILENAME: str = "ipc_global_national_long_latest.csv"

WHO_U5MR_INDICATOR: str = "MDG_0000000001"
WHO_GHO_BASE: str = "https://ghoapi.azureedge.net/api"

UNHCR_POPULATION_URL: str = "https://api.unhcr.org/population/v1/population/"
UNHCR_YEAR_FROM: int = 2018
UNHCR_YEAR_TO: int = 2024
UNHCR_API_PAGE_LIMIT: int = 10_000

HTTP_TIMEOUT_SECONDS: int = 120

# IPC Percentage arrives as a 0–1 share; values above this are treated as already percent
IPC_SHARE_TO_PERCENT_CEILING: float = 1.5

# Country deep-dive: trailing years of WHO U5MR history shown on charts
U5MR_TREND_LOOKBACK_YEARS: int = 15

DEMO_VIDEO_URL: str = ""
LIVE_APP_URL: str = ""
