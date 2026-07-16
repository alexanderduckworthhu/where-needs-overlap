# Deploy & demo checklist

Goal: a stranger can open a URL and understand the overlap story in under two minutes.

## Streamlit Community Cloud

1. Create a GitHub repo and push this project (include `data/processed/analysis_table.csv`
   and `metadata.json` so the demo works without live API calls on first load).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Main file path: `app.py`
4. Python version: 3.11+ recommended.
5. After deploy, paste the public URL into `README.md` (Live app row).

### Cloud notes

- Live fetches from HDX/UNHCR/WHO can be slow or rate-limited on Cloud.
  Committing the processed table keeps the portfolio reliable.
- Refresh workflow: run `python -m src.run_pipeline` locally → commit updated
  `analysis_table.csv` + `metadata.json` → push.

## 90-second demo video

1. Open the live app.
2. Follow `docs/talking_points.md` (do not improvise a tour of every widget).
3. Record Loom/YouTube.
4. Paste the link into `src/config.py` as `DEMO_VIDEO_URL = "https://..."`.
5. Add the same link to the README table.

## Pre-share self-check

- [ ] Displacement definition visible near KPIs
- [ ] Overlap tab shows a specific dual-pressure finding
- [ ] Missing IPC gap (e.g. South Sudan) explained in-app
- [ ] Methods & glossary tab opens
- [ ] EN/FR toggle works
- [ ] README case study matches what the app says
- [ ] “Not operational” footer present
