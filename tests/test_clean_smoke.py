"""Smoke tests for loaders and Story-view insight narrative."""

from __future__ import annotations

import pandas as pd

from src.clean import _load_unhcr, _load_who
from src.insights import compute_overlap_insight, format_action_steps, missing_ipc_note


def test_load_who_keeps_iso3(tmp_path) -> None:
    """WHO loader keeps ISO3 and u5mr columns."""
    path = tmp_path / "who.csv"
    pd.DataFrame(
        {"iso3": ["ETH", "SOM"], "year": [2022, 2022], "u5mr": [48.0, 110.0]}
    ).to_csv(path, index=False)
    out = _load_who(path)
    assert set(out["iso3"]) == {"ETH", "SOM"}
    assert "u5mr" in out.columns


def test_load_unhcr_keeps_displaced(tmp_path) -> None:
    """UNHCR loader preserves displaced counts."""
    path = tmp_path / "unhcr.csv"
    pd.DataFrame(
        {"iso3": ["ETH"], "displaced": [800000], "year": [2023]}
    ).to_csv(path, index=False)
    out = _load_unhcr(path)
    assert out.loc[0, "displaced"] == 800000


def test_overlap_insight_flags_dual_pressure_and_gaps() -> None:
    """Dual-pressure countries and missing IPC gaps appear in Story copy."""
    frame = pd.DataFrame(
        {
            "iso3": ["ETH", "SOM", "SSD"],
            "country": ["Ethiopia", "Somalia", "South Sudan"],
            "phase3plus_pct": [40.0, 30.0, None],
            "displaced": [1000.0, 100.0, 500.0],
            "u5mr": [50.0, 60.0, 70.0],
        }
    )
    insight = compute_overlap_insight(frame, lang="en")
    assert "Ethiopia" in insight.dual_pressure_countries
    assert "South Sudan" in insight.missing_ipc_countries
    assert "dual" in insight.body.lower() or "joint" in insight.body.lower()
    note = missing_ipc_note(frame, lang="en")
    assert note is not None
    assert "South Sudan" in note

    steps = format_action_steps(insight, lang="en")
    assert "Ethiopia" in steps
    assert "South Sudan" in steps
    assert "dual-pressure" in steps.lower() or "both" in steps.lower()

    french = compute_overlap_insight(frame, lang="fr")
    assert "Éthiopie" in french.dual_pressure_countries
    assert "Soudan du Sud" in french.missing_ipc_countries
    assert "double pression" in french.headline.lower()

    german = compute_overlap_insight(frame, lang="de")
    assert "Äthiopien" in german.dual_pressure_countries
    assert "Doppeldruck" in german.headline

    chinese = compute_overlap_insight(frame, lang="zh")
    assert "埃塞俄比亚" in chinese.dual_pressure_countries
    assert "双重压力" in chinese.headline

