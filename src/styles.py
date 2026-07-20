"""Design tokens and Streamlit chrome, cool slate + deep teal (not cream/serif/terracotta)."""

from __future__ import annotations

import streamlit as st

# Named colors consumed by charts and CSS (single source of truth)
COLOR_INK: str = "#14212B"
COLOR_MUTED: str = "#5A6872"
COLOR_PRIMARY: str = "#0F5C66"
COLOR_SURFACE: str = "#E4EBEF"
COLOR_BACKGROUND: str = "#F2F5F7"
COLOR_SERIES_WARM: str = "#B45309"
COLOR_BORDER: str = "rgba(20, 33, 43, 0.08)"

SPACE_1: int = 4
SPACE_2: int = 8
SPACE_3: int = 12
SPACE_4: int = 16
SPACE_5: int = 24
SPACE_6: int = 32
RADIUS_MD: int = 12
MAX_CONTENT_WIDTH_PX: int = 1120
MOTION_MS: int = 400

CSS: str = f"""
:root {{
  --color-ink: {COLOR_INK};
  --color-muted: {COLOR_MUTED};
  --color-primary: {COLOR_PRIMARY};
  --color-surface: {COLOR_SURFACE};
  --color-bg: {COLOR_BACKGROUND};
  --color-warm: {COLOR_SERIES_WARM};
  --color-border: {COLOR_BORDER};
  --space-1: {SPACE_1}px;
  --space-2: {SPACE_2}px;
  --space-3: {SPACE_3}px;
  --space-4: {SPACE_4}px;
  --space-5: {SPACE_5}px;
  --space-6: {SPACE_6}px;
  --radius-md: {RADIUS_MD}px;
  --max-content: {MAX_CONTENT_WIDTH_PX}px;
  --motion: {MOTION_MS}ms;
}}

@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {{
  font-family: 'IBM Plex Sans', 'Helvetica Neue', sans-serif;
  color: var(--color-ink);
}}

h1, h2, h3, .hero-title {{
  font-family: 'IBM Plex Sans', 'Helvetica Neue', sans-serif !important;
  font-weight: 650 !important;
  letter-spacing: -0.02em;
  color: var(--color-ink) !important;
}}

@keyframes fade-up {{
  from {{ opacity: 0; transform: translateY(6px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

section.main > div {{
  animation: fade-up var(--motion) ease-out;
}}

.block-container {{
  padding-top: var(--space-5) !important;
  padding-bottom: var(--space-6) !important;
  max-width: var(--max-content);
}}

#MainMenu {{ visibility: hidden; }}
footer {{ visibility: hidden; }}
header[data-testid="stHeader"] {{ background: transparent; }}

div[data-testid="stMetric"] {{
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-4);
  transition: transform var(--motion) ease, box-shadow var(--motion) ease;
}}
div[data-testid="stMetric"]:hover {{
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(15, 92, 102, 0.10);
}}
div[data-testid="stMetric"] label {{
  font-size: 0.85rem !important;
  color: var(--color-muted) !important;
}}

div[data-testid="stRadio"] > label {{
  font-weight: 600;
  font-size: 0.95rem;
}}
div[data-testid="stRadio"] [role="radiogroup"] label {{
  padding: var(--space-2) var(--space-3);
  border-radius: 999px;
  transition: background var(--motion) ease, color var(--motion) ease;
}}

.soft-card {{
  background: rgba(228, 235, 239, 0.85);
  border: 1px solid var(--color-border);
  border-left: 4px solid var(--color-primary);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  margin: var(--space-2) 0 var(--space-4) 0;
  animation: fade-up var(--motion) ease-out;
}}
.soft-card strong {{ color: var(--color-primary); }}

.eyebrow {{
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-muted);
  margin-bottom: var(--space-1);
}}

.hero-why {{
  font-size: 1.05rem;
  line-height: 1.55;
  color: var(--color-ink);
  max-width: 46rem;
  margin: var(--space-2) 0 var(--space-4) 0;
  opacity: 0.92;
}}

.footer-note {{
  color: var(--color-muted);
  font-size: 0.85rem;
  margin-top: var(--space-5);
}}

.status-pill {{
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--color-primary);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 999px;
  padding: var(--space-1) var(--space-3);
  margin-bottom: var(--space-3);
}}

div[data-testid="stExpander"] {{
  border: 1px solid var(--color-border);
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.45);
}}

div[data-testid="stPlotlyChart"] {{
  border-radius: var(--radius-md);
  overflow: hidden;
}}

a, button {{
  outline-offset: 2px;
}}
"""


def inject_styles() -> None:
    """Inject design-token CSS into the Streamlit page. Returns None."""
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


def soft_card(html_body: str) -> None:
    """Render a left-accent insight card. Returns None."""
    st.markdown(f'<div class="soft-card">{html_body}</div>', unsafe_allow_html=True)
