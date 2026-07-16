"""Write data/processed/metadata.json when the pipeline finishes."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from src.config import (
    HDX_IPC_DATASET_ID,
    PROCESSED_DIR,
    WHO_U5MR_INDICATOR,
)


def write_metadata(processed_dir: Path | None = None) -> Path:
    """Persist access date and source URLs; returns the metadata.json path."""
    processed_dir = processed_dir or PROCESSED_DIR
    processed_dir.mkdir(parents=True, exist_ok=True)
    meta = {
        "project": "where-needs-overlap",
        "access_date": date.today().isoformat(),
        "sources": [
            {
                "name": "IPC Acute Food Insecurity (national long)",
                "provider": "IPC via HDX",
                "dataset_id": HDX_IPC_DATASET_ID,
                "url": f"https://data.humdata.org/dataset/{HDX_IPC_DATASET_ID}",
                "license_note": "Check HDX dataset page for current license terms.",
            },
            {
                "name": "UNHCR Population Statistics API",
                "provider": "UNHCR",
                "url": "https://api.unhcr.org/population/v1/population/",
                "definition": "Hosted REF + asylum-seekers + others of concern (coa, ISO)",
                "license_note": "UNHCR public API / refugee statistics terms.",
            },
            {
                "name": "WHO GHO under-5 mortality",
                "provider": "WHO",
                "indicator": WHO_U5MR_INDICATOR,
                "url": f"https://ghoapi.azureedge.net/api/{WHO_U5MR_INDICATOR}",
                "license_note": "WHO GHO public data; attribute WHO.",
            },
        ],
        "join_key": "ISO3",
        "not_for_operational_use": True,
    }
    path = processed_dir / "metadata.json"
    path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return path
