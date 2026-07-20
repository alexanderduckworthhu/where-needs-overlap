"""Display formatters for dashboard KPIs and captions."""

from __future__ import annotations

from typing import Any

import pandas as pd

# Languages that prefer a thin/nbsp thousands separator instead of comma
_SPACE_THOUSANDS_LANGS = frozenset({"fr", "de", "it", "pt", "ru"})


def fmt_int(value: Any, lang: str = "en") -> str:
    """Format an integer with locale-aware thousands separators; returns em dash if missing."""
    if pd.isna(value):
        return ", "
    raw = f"{int(value):,}"
    if lang in _SPACE_THOUSANDS_LANGS:
        return raw.replace(",", "\u00a0")
    return raw


def fmt_float(value: Any, digits: int = 1) -> str:
    """Format a float to a fixed number of decimals; returns em dash if missing."""
    if pd.isna(value):
        return ", "
    return f"{float(value):.{digits}f}"
