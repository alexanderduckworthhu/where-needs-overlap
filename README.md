# Where Needs Overlap

A country-level dashboard that shows where acute food insecurity, hosted displacement, and under-5 mortality coincide ; built for IM and programme analysts working with UNICEF, UNHCR, and OCHA counterparts in Geneva.

| | |
|---|---|
| **Live app** | Set `LIVE_APP_URL` in `src/config.py` after Streamlit Cloud deploy (`docs/deploy.md`) |
| **Demo (90 sec)** | Set `DEMO_VIDEO_URL` in `src/config.py` |
| **Status** | Portfolio learning project ; not an operational product |
| **Data access date** | `2026-07-14` (see `data/processed/metadata.json`) |

## Why it exists

Food security, displacement, and child survival are still often viewed in separate tools. That split hides **compounded** pressure: a high IPC Phase 3+ share in a country that also hosts large displaced populations signals a different coordination problem than either metric alone. Public HDX, UNHCR, and WHO sources already carry the pieces; this project joins them on ISO3 and frames one decision question for Geneva audiences.

## Technical decisions

- **Streamlit over Dash/Tableau** ; fastest path to a shareable URL and EN/FR toggle for a portfolio; Tableau would require licenses analysts at many IOs already have, but does not showcase reproducible Python.
- **IPC via HDX (national long) over subnational IPC** ; national Phase 3+ is the honest scope for an eight-country join; subnational maps need different QA and would inflate scope without changing the core narrative.
- **UNHCR hosted (CoA) counts over origin-based totals** ; origin and asylum answer different questions; locking CoA keeps the Story chart interpretable.
- **WHO GHO under-5 mortality as context, not a real-time pulse** ; structural child-survival risk that UNICEF stakeholders recognize; lagged by design.
- **No ML / forecasting** ; avoiding unverifiable crisis prediction claims that would undermine trust in an IO interview.

## Results & metrics

Current extract (`data/processed/analysis_table.csv`, access date 2026-07-14):

- **8** focus countries (Horn of Africa + Sahel)
- **~48.6 million** people in IPC Phase 3+ across countries with a current national estimate
- **3** dual-pressure countries at or above both focus-set medians for Phase 3+ share and hosted displacement: **Sudan, Ethiopia, Chad**
- **1** intentional coverage gap: **South Sudan** has no current national IPC Phase 3+ row in this HDX extract
- **EN / FR / DE / IT / PT / ZH / RU** UI via `src/i18n.py` + `src/locales_extra.py`

## Setup & usage

```bash
cd where-needs-overlap
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python -m src.run_pipeline
streamlit run app.py
```

UNHCR fallback if the API is unreachable: save `data/raw/unhcr_manual.csv` with columns `iso3,displaced,year`, then `python -m src.clean`.

## Data

| Source | Access | Definition / transform | License |
|--------|--------|------------------------|---------|
| IPC acute food insecurity (national long) | [HDX dataset](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data) via HDX Python API | Keep `Validity period == current`, `Phase == 3+`; convert 0–1 share to percent | Check HDX dataset page; attribute IPC / HDX |
| UNHCR Population Statistics API | `https://api.unhcr.org/population/v1/population/` with `coa` + `cf_type=ISO` | Hosted refugees + asylum-seekers + others of concern | UNHCR public stats terms |
| WHO GHO under-5 mortality | `MDG_0000000001` via GHO OData | Latest year per focus ISO3 | Attribute WHO |

Joins use **ISO3** only. All figures are **national public aggregates** ; no individual or community identifiers. Access dates are written to `data/processed/metadata.json` on every clean run.

**For production use**, an IO shop would need: agreed displacement definition in a data dictionary, automated refresh + lineage, subnational coverage QA, and a named data steward ; none of which this portfolio claims to provide.

## What I'd improve next

1. Replace the illustrative z-score `compound_score` with a transparent, documented multi-criteria ranking co-designed with an IM officer (or drop the score and keep dual-pressure medians only).
2. Add one deep-dive country’s subnational IPC (admin-1) once a single operation is locked ; national medians still hide hotspots.
3. Wire HDX HAPI where endpoints cover IPC so resource selection is less brittle than CSV name matching.

## Docs

| Doc | Use |
|-----|-----|
| `REVERSE_ENGINEERING.txt` | Codebase walkthrough |
| `docs/methods.md` | Metric construction |
| `docs/deploy.md` | Streamlit Cloud + demo |
| `docs/limitations.md` | Coverage and definition limits |
| `docs/talking_points.md` | 90-second oral walkthrough |

## About me

_Add 1–2 sentences on motivation for humanitarian data work + LinkedIn/CV URL._
