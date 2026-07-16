"""Fetch IPC acute food insecurity (national long) from HDX."""

from __future__ import annotations

import logging
import sys
from pathlib import Path

from hdx.api.configuration import Configuration
from hdx.data.dataset import Dataset

from src.config import (
    HDX_IPC_DATASET_ID,
    IPC_OUTPUT_FILENAME,
    IPC_RESOURCE_HINT,
    RAW_DIR,
    USER_AGENT,
)

logger = logging.getLogger(__name__)


def _ensure_hdx_configuration() -> None:
    """Create a read-only HDX configuration, or reuse one already in the process."""
    try:
        Configuration.create(
            hdx_site="prod",
            user_agent=USER_AGENT,
            hdx_read_only=True,
        )
    except ValueError as exc:
        # HDX raises when Configuration already exists in-process.
        logger.debug("HDX configuration already present: %s", exc)


def fetch_ipc(output_dir: Path | None = None) -> Path:
    """Download the latest IPC national long CSV into data/raw; returns the saved path."""
    output_dir = output_dir or RAW_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    _ensure_hdx_configuration()

    try:
        dataset = Dataset.read_from_hdx(HDX_IPC_DATASET_ID)
    except (OSError, RuntimeError, ValueError) as exc:
        raise RuntimeError(
            f"Failed to read HDX dataset '{HDX_IPC_DATASET_ID}': {exc}"
        ) from exc

    if not dataset:
        raise RuntimeError(f"Could not read HDX dataset: {HDX_IPC_DATASET_ID}")

    resources = dataset.get_resources()
    chosen = None
    for resource in resources:
        name = (resource.get("name") or "").lower()
        url = (resource.get("download_url") or resource.get("url") or "").lower()
        if IPC_RESOURCE_HINT in name or IPC_RESOURCE_HINT in url:
            chosen = resource
            break

    if chosen is None:
        for resource in resources:
            fmt = (resource.get("format") or "").lower()
            name = (resource.get("name") or "").lower()
            if fmt == "csv" or name.endswith(".csv"):
                chosen = resource
                break

    if chosen is None:
        raise RuntimeError("No suitable IPC CSV resource found on HDX.")

    try:
        url, path = chosen.download(str(output_dir))
    except (OSError, RuntimeError, ValueError) as exc:
        raise RuntimeError(f"IPC download failed: {exc}") from exc

    downloaded = Path(path)
    target = output_dir / IPC_OUTPUT_FILENAME
    if downloaded.resolve() != target.resolve():
        target.write_bytes(downloaded.read_bytes())
    logger.info("IPC downloaded from %s -> %s", url, target)
    print(f"IPC downloaded from {url}")
    print(f"Saved to {target}")
    return target


def main() -> None:
    """CLI entry for `python -m src.fetch_hdx`."""
    fetch_ipc()


if __name__ == "__main__":
    main()
    sys.exit(0)
