"""Derived narrative for the Story view, dual-pressure countries and coverage gaps."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from src.formatters import fmt_int
from src.i18n import GAP_VERBS, country_name, t


@dataclass
class OverlapInsight:
    """Story-view copy built from the analysis table."""

    headline: str
    body: str
    dual_pressure_countries: list[str]
    missing_ipc_countries: list[str]


def _gap_verb(lang: str, count: int) -> str:
    """Return singular/plural linking verb for coverage-gap sentences."""
    singular, plural = GAP_VERBS.get(lang, GAP_VERBS["en"])
    return singular if count == 1 else plural


def compute_overlap_insight(analysis_table: pd.DataFrame, lang: str = "en") -> OverlapInsight:
    """Identify dual-pressure countries and return Story-view headline/body copy."""
    missing_iso = analysis_table.loc[
        analysis_table["phase3plus_pct"].isna(), "iso3"
    ].tolist()
    missing_names = [country_name(lang, iso) for iso in missing_iso]
    scored = analysis_table.dropna(subset=["phase3plus_pct", "displaced"]).copy()

    median_ipc_pct = scored["phase3plus_pct"].median()
    median_displaced = scored["displaced"].median()
    dual_pressure = scored[
        (scored["phase3plus_pct"] >= median_ipc_pct)
        & (scored["displaced"] >= median_displaced)
    ].sort_values(["phase3plus_pct", "displaced"], ascending=False)

    dual_pressure_names = [
        country_name(lang, iso) for iso in dual_pressure["iso3"].tolist()
    ]
    median_displaced_text = fmt_int(median_displaced, lang)

    if dual_pressure_names:
        headline = t(
            lang,
            "insight_headline",
            names=", ".join(dual_pressure_names),
            ipc_pct=f"{median_ipc_pct:.0f}",
            displaced=median_displaced_text,
        )
    else:
        headline = t(lang, "insight_headline_empty")

    contrast = ""
    high_ipc_low_displacement = scored[
        (scored["phase3plus_pct"] >= median_ipc_pct)
        & (scored["displaced"] < median_displaced)
    ]
    if not high_ipc_low_displacement.empty:
        contrast_row = high_ipc_low_displacement.sort_values(
            "phase3plus_pct", ascending=False
        ).iloc[0]
        contrast = t(
            lang,
            "insight_contrast",
            country=country_name(lang, contrast_row["iso3"]),
            ipc_pct=f"{contrast_row['phase3plus_pct']:.0f}",
        )

    gap = ""
    if missing_names:
        gap = t(
            lang,
            "insight_gap",
            names=", ".join(missing_names),
            verb=_gap_verb(lang, len(missing_names)),
        )

    body = "\n\n".join(
        part for part in (t(lang, "insight_body_lead"), contrast.strip(), gap.strip()) if part
    )

    return OverlapInsight(
        headline=headline,
        body=body,
        dual_pressure_countries=dual_pressure_names,
        missing_ipc_countries=missing_names,
    )


def format_action_steps(insight: OverlapInsight, lang: str = "en") -> str:
    """Return Story-view bullets tied to this run's dual-pressure and gap countries."""
    bullets: list[str] = []
    if insight.dual_pressure_countries:
        bullets.append(
            t(
                lang,
                "action_dual_pressure",
                countries=", ".join(insight.dual_pressure_countries),
            )
        )
    if insight.missing_ipc_countries:
        bullets.append(
            t(
                lang,
                "action_missing_ipc",
                countries=", ".join(insight.missing_ipc_countries),
            )
        )
    bullets.append(t(lang, "action_single_axis"))
    return "\n".join(f"- {line}" for line in bullets)


def missing_ipc_note(analysis_table: pd.DataFrame, lang: str = "en") -> str | None:
    """Return Map-view copy when IPC Phase 3+ is missing; None when complete."""
    missing_iso = analysis_table.loc[
        analysis_table["phase3plus_pct"].isna(), "iso3"
    ].tolist()
    if not missing_iso:
        return None
    missing_names = [country_name(lang, iso) for iso in missing_iso]
    return t(
        lang,
        "map_gap_note",
        names=", ".join(missing_names),
        verb=_gap_verb(lang, len(missing_names)),
    )
