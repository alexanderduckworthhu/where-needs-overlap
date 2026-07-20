# Methods

This note exists so a hiring manager (or future you) can audit the numbers without reading every script.

## IPC Phase 3+ (HDX)

1. Download `ipc_global_national_long_latest.csv` from HDX dataset
   `global-acute-food-insecurity-country-data` via `src/fetch_hdx.py`.
2. Filter to focus ISO3 codes (`src/config.py`).
3. Prefer rows where `Validity period == current` (exclude projections for the main KPIs).
4. Keep rows where `Phase == 3+` (Crisis or worse, the operational threshold).
5. `Number` → `phase3plus_people`.
6. `Percentage` in the HDX extract is a **0–1 share**; multiply by 100 for chart percent labels.

If a focus country has no current `3+` row, the analysis table leaves IPC fields blank.
**Blank ≠ zero hunger**, it means this national extract did not provide a current Phase 3+ estimate.

## Displacement (UNHCR)

Endpoint: `https://api.unhcr.org/population/v1/population/`

Required query pattern:

- `coa=<ISO3 list>`, country of asylum (hosted)
- `cf_type=ISO`
- `yearFrom` / `yearTo`

**API pitfall:** if `coa` is omitted, the API returns a world aggregate (`coa_iso = '-'`).

Locked metric per country-year:

`displaced = refugees + asylum_seekers + ooc`

Latest year per country feeds the dashboard; full history feeds the country deep-dive trend.

We intentionally do **not** mix country-of-origin totals into the same chart.

## Under-5 mortality (WHO GHO)

- Indicator code: `MDG_0000000001`
- Filter to `SpatialDimType == COUNTRY` and focus ISO3
- Prefer both-sex rows when a sex dimension exists
- Latest year → analysis table; longer history → deep-dive trend

Treat U5MR as **structural child-survival context**, not a real-time outbreak pulse.

## Joins and compound score

- Skeleton frame of all 8 focus countries, left-joined to IPC / UNHCR / WHO on `iso3`
- `compound_score` = sum of simple z-scores across IPC %, displacement, and U5MR  
  → conversation aid only; **not** an official severity index

## Reproducibility

```bash
python -m src.run_pipeline
```

Writes:

- `data/processed/analysis_table.csv`
- `data/processed/metadata.json` (access date + source URLs)

Dependency pins: `requirements.txt`.
