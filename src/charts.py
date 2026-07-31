"""Plotly chart builders for the Story, Map, and Country views."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.config import U5MR_TREND_LOOKBACK_YEARS
from src.i18n import chart_labels, country_name
from src.styles import COLOR_MUTED, COLOR_PRIMARY, COLOR_SERIES_WARM, MOTION_MS

CHART_HEIGHT_DRILLDOWN_PX: int = 380
CHART_HEIGHT_TRENDS_PX: int = 360
LINE_SMOOTHING: float = 0.6


def _with_localized_country_names(frame: pd.DataFrame, lang: str) -> pd.DataFrame:
    """Return a copy with a localized `country` column for hover labels."""
    localized = frame.copy()
    localized["country"] = localized["iso3"].map(lambda iso: country_name(lang, iso))
    return localized


def map_ipc(analysis_table: pd.DataFrame, lang: str = "en") -> go.Figure:
    """Build a choropleth of IPC Phase 3+ share; returns a Plotly figure."""
    labels = chart_labels(lang)
    plot_frame = _with_localized_country_names(analysis_table, lang)
    figure = px.choropleth(
        plot_frame,
        locations="iso3",
        color="phase3plus_pct",
        hover_name="country",
        hover_data={
            "iso3": False,
            "phase3plus_pct": ":.1f",
            "phase3plus_people": ":,.0f",
            "displaced": ":,.0f",
            "u5mr": ":.1f",
        },
        color_continuous_scale="Teal",
        labels={
            "phase3plus_pct": labels["chart_map_pct"],
            "phase3plus_people": labels["chart_map_people"],
            "displaced": labels["chart_map_disp"],
            "u5mr": labels["chart_map_u5"],
        },
        title=labels["chart_map_title"],
    )
    figure.update_geos(
        projection_type="natural earth",
        showcountries=True,
        showcoastlines=True,
        fitbounds="locations",
        bgcolor="rgba(0,0,0,0)",
    )
    figure.update_layout(
        margin=dict(l=10, r=10, t=50, b=10),
        coloraxis_colorbar_title=labels["chart_map_colorbar"],
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        transition_duration=MOTION_MS,
        font_family="IBM Plex Sans",
    )
    return figure


def scatter_overlap(analysis_table: pd.DataFrame, lang: str = "en") -> go.Figure:
    """Build displacement × IPC scatter sized by under-5 mortality; returns a Plotly figure."""
    labels = chart_labels(lang)
    plot_frame = _with_localized_country_names(
        analysis_table.dropna(subset=["displaced", "phase3plus_pct"]),
        lang,
    )
    figure = px.scatter(
        plot_frame,
        x="displaced",
        y="phase3plus_pct",
        size="u5mr",
        color="u5mr",
        text="iso3",
        hover_name="country",
        labels={
            "displaced": labels["chart_scatter_x"],
            "phase3plus_pct": labels["chart_scatter_y"],
            "u5mr": labels["chart_scatter_u5"],
        },
        title=labels["chart_scatter_title"],
        color_continuous_scale="Tealgrn",
    )
    figure.update_traces(textposition="top center")
    figure.update_layout(
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        transition_duration=MOTION_MS,
        font_family="IBM Plex Sans",
    )
    return figure


def country_drilldown(
    analysis_table: pd.DataFrame,
    iso3: str,
    lang: str = "en",
) -> go.Figure:
    """Build a three-panel snapshot for one country; returns a Plotly figure."""
    labels = chart_labels(lang)
    country_rows = analysis_table[analysis_table["iso3"] == iso3]
    if country_rows.empty:
        return go.Figure().update_layout(title=labels["chart_no_data"].format(iso3=iso3))

    country_row = country_rows.iloc[0]
    localized_name = country_name(lang, iso3)
    median_u5mr = analysis_table["u5mr"].median()

    figure = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=(
            labels["chart_drill_p1"],
            labels["chart_drill_p2"],
            labels["chart_drill_p3"],
        ),
    )
    figure.add_trace(
        go.Bar(
            x=[labels["chart_drill_bar_ipc"]],
            y=[country_row.get("phase3plus_people") or 0],
            marker_color=COLOR_SERIES_WARM,
            name="IPC",
        ),
        row=1,
        col=1,
    )
    figure.add_trace(
        go.Bar(
            x=[labels["chart_drill_bar_disp"]],
            y=[country_row.get("displaced") or 0],
            marker_color=COLOR_PRIMARY,
            name="UNHCR",
        ),
        row=1,
        col=2,
    )
    figure.add_trace(
        go.Bar(
            x=[localized_name, labels["chart_drill_median"]],
            y=[
                country_row.get("u5mr") or 0,
                median_u5mr if pd.notna(median_u5mr) else 0,
            ],
            marker_color=[COLOR_SERIES_WARM, COLOR_MUTED],
            name="WHO",
        ),
        row=1,
        col=3,
    )
    figure.update_layout(
        title_text=labels["chart_drill_title"].format(country=localized_name),
        showlegend=False,
        margin=dict(l=10, r=10, t=80, b=10),
        height=CHART_HEIGHT_DRILLDOWN_PX,
        paper_bgcolor="rgba(0,0,0,0)",
        transition_duration=MOTION_MS,
        font_family="IBM Plex Sans",
    )
    return figure


def country_trends(
    displacement_history: pd.DataFrame | None,
    u5mr_history: pd.DataFrame | None,
    iso3: str,
    country_label: str,
    lang: str = "en",
) -> go.Figure:
    """Build hosted-displacement and U5MR trend lines for one country; returns a Plotly figure."""
    labels = chart_labels(lang)
    figure = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(labels["chart_trends_p1"], labels["chart_trends_p2"]),
        horizontal_spacing=0.12,
    )

    if displacement_history is not None and not displacement_history.empty:
        displacement_series = displacement_history[
            displacement_history["iso3"] == iso3
        ].sort_values("year")
        if not displacement_series.empty:
            figure.add_trace(
                go.Scatter(
                    x=pd.to_numeric(displacement_series["year"], errors="coerce"),
                    y=pd.to_numeric(displacement_series["displaced"], errors="coerce"),
                    mode="lines+markers",
                    line=dict(
                        color=COLOR_PRIMARY,
                        width=2.5,
                        shape="spline",
                        smoothing=LINE_SMOOTHING,
                    ),
                    marker=dict(size=7, color=COLOR_PRIMARY),
                    name=labels["chart_trends_series_disp"],
                    hovertemplate="%{x}<br>%{y:,.0f}<extra></extra>",
                ),
                row=1,
                col=1,
            )

    if u5mr_history is not None and not u5mr_history.empty:
        u5mr_series = u5mr_history[u5mr_history["iso3"] == iso3].sort_values("year")
        if not u5mr_series.empty:
            earliest_year = u5mr_series["year"].max() - U5MR_TREND_LOOKBACK_YEARS
            u5mr_series = u5mr_series[u5mr_series["year"] >= earliest_year]
            figure.add_trace(
                go.Scatter(
                    x=pd.to_numeric(u5mr_series["year"], errors="coerce"),
                    y=pd.to_numeric(u5mr_series["u5mr"], errors="coerce"),
                    mode="lines+markers",
                    line=dict(
                        color=COLOR_SERIES_WARM,
                        width=2.5,
                        shape="spline",
                        smoothing=LINE_SMOOTHING,
                    ),
                    marker=dict(size=7, color=COLOR_SERIES_WARM),
                    name=labels["chart_trends_series_u5"],
                    hovertemplate="%{x}<br>%{y:.1f}<extra></extra>",
                ),
                row=1,
                col=2,
            )

    if len(figure.data) == 0:
        figure.add_annotation(
            text=labels["chart_no_data"].format(iso3=iso3),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=14, color=COLOR_MUTED),
        )

    figure.update_layout(
        title_text=labels["chart_trends_title"].format(country=country_label),
        showlegend=False,
        margin=dict(l=10, r=10, t=80, b=10),
        height=CHART_HEIGHT_TRENDS_PX,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.55)",
        font_family="IBM Plex Sans",
        font_color=COLOR_MUTED,
    )
    figure.update_xaxes(showgrid=False, zeroline=False)
    figure.update_yaxes(showgrid=True, gridcolor="rgba(20,33,43,0.08)", zeroline=False)
    return figure
