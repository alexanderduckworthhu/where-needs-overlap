"""
Where Needs Overlap — Streamlit entry point.

Story-first navigation: insight first, optional Map / Country / About afterward.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

import pandas as pd
import streamlit as st

from src.charts import country_drilldown, country_trends, map_ipc, scatter_overlap
from src.config import DEMO_VIDEO_URL, FOCUS_ISO3, LIVE_APP_URL, PROCESSED_DIR, RAW_DIR
from src.formatters import fmt_float, fmt_int
from src.i18n import (
    GLOSSARY,
    LANGUAGE_LABELS,
    LANGUAGE_OPTIONS,
    NAV_KEYS,
    country_name,
    t,
)
from src.insights import compute_overlap_insight, format_action_steps, missing_ipc_note
from src.styles import inject_styles, soft_card

logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="Where Needs Overlap",
    page_icon="◎",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_PATH: Path = PROCESSED_DIR / "analysis_table.csv"
META_PATH: Path = PROCESSED_DIR / "metadata.json"
DISP_HISTORY: Path = RAW_DIR / "unhcr_displacement_history.csv"
U5_HISTORY: Path = RAW_DIR / "who_u5mr_focus_history.csv"


@st.cache_data(show_spinner=False)
def load_analysis_table(path: str) -> pd.DataFrame:
    """Load the processed analysis CSV; raises FileNotFoundError if missing."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        raise
    except (OSError, pd.errors.ParserError) as exc:
        raise RuntimeError(f"Could not read analysis table at {path}: {exc}") from exc


@st.cache_data(show_spinner=False)
def load_optional_csv(path: str) -> pd.DataFrame | None:
    """Load a history CSV when present; returns None if the file is missing."""
    file_path = Path(path)
    if not file_path.exists():
        return None
    try:
        return pd.read_csv(file_path)
    except (OSError, pd.errors.ParserError) as exc:
        logger.warning("Skipping unreadable optional CSV %s: %s", path, exc)
        return None


def load_metadata(path: Path) -> dict:
    """Load provenance metadata JSON; returns {} when absent or invalid."""
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("Metadata unreadable at %s: %s", path, exc)
        return {}


inject_styles()

lang = st.sidebar.selectbox(
    "Language",
    options=list(LANGUAGE_OPTIONS),
    format_func=lambda code: LANGUAGE_LABELS.get(code, code),
    key="ui_lang",
)
st.sidebar.caption(t(lang, "sidebar_hint"))
st.sidebar.markdown(t(lang, "sidebar_guide"))
if st.sidebar.button(t(lang, "reset_view"), type="secondary"):
    st.session_state["main_nav"] = "story"
    st.rerun()

st.markdown(f'<div class="eyebrow">{t(lang, "eyebrow")}</div>', unsafe_allow_html=True)
st.markdown(f'<h1 class="hero-title">{t(lang, "title")}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-why">{t(lang, "why")}</p>', unsafe_allow_html=True)

demo_or_live = DEMO_VIDEO_URL or LIVE_APP_URL
if demo_or_live:
    st.link_button(t(lang, "demo_watch"), demo_or_live, type="primary")

with st.expander(t(lang, "def_expander"), expanded=False):
    st.markdown(f"**{t(lang, 'def_title')}**")
    st.markdown(t(lang, "def_body"))

if not DATA_PATH.exists():
    st.info(t(lang, "no_data"))
    st.stop()

try:
    with st.spinner(t(lang, "loading")):
        analysis_table = load_analysis_table(str(DATA_PATH))
        meta = load_metadata(META_PATH)
        insight = compute_overlap_insight(analysis_table, lang=lang)
        gap_note = missing_ipc_note(analysis_table, lang=lang)
        displacement_history = load_optional_csv(str(DISP_HISTORY))
        u5mr_history = load_optional_csv(str(U5_HISTORY))
except (RuntimeError, OSError) as exc:
    st.error(t(lang, "load_error", detail=str(exc)))
    st.stop()

st.markdown(
    f'<span class="status-pill">{t(lang, "status_ready")}</span>',
    unsafe_allow_html=True,
)

kpi_cols = st.columns(3)
kpi_cols[0].metric(
    t(lang, "kpi_ipc"),
    fmt_int(analysis_table["phase3plus_people"].sum(), lang),
    help=t(lang, "kpi_ipc_help"),
)
kpi_cols[1].metric(
    t(lang, "kpi_disp"),
    fmt_int(analysis_table["displaced"].sum(), lang),
    help=t(lang, "kpi_disp_help"),
)
kpi_cols[2].metric(
    t(lang, "kpi_u5"),
    fmt_float(analysis_table["u5mr"].median()),
    help=t(lang, "kpi_u5_help"),
)

if meta.get("access_date"):
    st.caption(
        f"{t(lang, 'access_dates')} **{meta['access_date']}** {t(lang, 'access_dates_hint')}"
    )

nav = st.radio(
    t(lang, "nav_label"),
    options=list(NAV_KEYS),
    format_func=lambda key: t(lang, f"nav_{key}"),
    horizontal=True,
    key="main_nav",
)

if nav == "story":
    soft_card(f"<strong>{t(lang, 'insight_title')}</strong><br/>{insight.headline}")
    st.plotly_chart(scatter_overlap(analysis_table, lang=lang), width="stretch")
    st.markdown(insight.body)
    st.markdown(f"**{t(lang, 'action_heading')}**")
    st.markdown(format_action_steps(insight, lang=lang))

elif nav == "map":
    st.plotly_chart(map_ipc(analysis_table, lang=lang), width="stretch")
    st.caption(t(lang, "map_takeaway"))
    if gap_note:
        st.markdown(gap_note)

elif nav == "country":
    selected_iso = st.selectbox(
        t(lang, "country_select"),
        options=sorted(FOCUS_ISO3),
        format_func=lambda iso: country_name(lang, iso),
    )
    localized_name = country_name(lang, selected_iso)
    country_row = analysis_table[analysis_table["iso3"] == selected_iso].iloc[0]

    st.plotly_chart(
        country_drilldown(analysis_table, selected_iso, lang=lang),
        width="stretch",
    )
    if pd.isna(country_row.get("phase3plus_pct")):
        st.markdown(t(lang, "country_gap", country=localized_name))
    else:
        st.markdown(
            t(
                lang,
                "country_snapshot",
                country=localized_name,
                pct=fmt_float(country_row.get("phase3plus_pct")),
                displaced=fmt_int(country_row.get("displaced"), lang),
                u5mr=fmt_float(country_row.get("u5mr")),
            )
        )

    st.markdown(f"#### {t(lang, 'trends_title')}")
    st.caption(t(lang, "trends_intro"))
    st.plotly_chart(
        country_trends(
            displacement_history,
            u5mr_history,
            selected_iso,
            localized_name,
            lang=lang,
        ),
        width="stretch",
    )
    st.caption(t(lang, "trends_caption"))

else:
    st.markdown(t(lang, "about_intro"))
    st.markdown(t(lang, "methods_md"))
    st.markdown(t(lang, "glossary_heading"))
    for term, meaning in GLOSSARY[lang]:
        st.markdown(f"- **{term}** — {meaning}")
    st.markdown(t(lang, "sources_md"))
    if meta.get("access_date"):
        st.markdown(f"**{t(lang, 'access_date_label')}:** {meta['access_date']}")
        for src in meta.get("sources", []):
            st.markdown(f"- {src.get('name')}: {src.get('url', '')}")
    st.markdown(t(lang, "ethics_md"))

st.markdown(f'<p class="footer-note">{t(lang, "footer")}</p>', unsafe_allow_html=True)
