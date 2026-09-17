# Global Q Explorer

A Streamlit app for exploring the **global-q.org testing portfolios** — the
201 equity anomalies replicated by Hou, Xue and Zhang on one consistent data
pipeline.

Current data: the **2025 vintage**, released July 2026, covering
**January 1967 to December 2025**.

## What you can do with it

| View | What it answers |
|---|---|
| **Portfolio Analysis** | How has this anomaly's portfolio performed? Cumulative and excess returns, correlations, rolling statistics, drawdowns, and a weighted multifactor portfolio you build yourself. |
| **Metric Reference** | What *is* this signal? A searchable dictionary of all 201 anomalies — definition, exact construction, inputs, sort, expected direction and the paper it comes from. |
| **Factor Model Alphas** | Does a factor model explain it? Long-short spreads regressed on CAPM, the q-factor model and q5, with alphas, t-statistics and factor loadings — plus a one-click screen across a whole category. |

The Metric Reference is also written out as markdown: start at
[docs/METRICS.md](docs/METRICS.md).

## Setup

### Local Python

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Then open <http://localhost:8501>.

### Docker

```bash
docker compose up --build
```

Or without compose:

```bash
docker build -t global-q-explorer .
docker run -p 8501:8501 global-q-explorer
```

## The data

The app ships the **two-way, size-interacted** testing portfolios: each anomaly
is sorted into 3 size groups × 5 signal quintiles, value-weighted, on NYSE
breakpoints.

```
data/
├── me_mom_monthly_2025/      43 momentum anomalies
├── me_vvg_monthly_2025/      32 value-versus-growth
├── me_inv_monthly_2025/      32 investment
├── me_prof_monthly_2025/     50 profitability
├── me_intan_monthly_2025/    33 intangibles
├── me_fric_monthly_2025/     10 trading frictions
├── portf_me_monthly_2025.csv     size deciles, used as the market reference
├── q5_factors_monthly_2025.csv   q5 factor returns
└── metrics_catalog.json          definitions behind every code
```

Each anomaly file has `year`, `month`, `rank_ME` (1 = micro … 3 = big),
`rank_<CODE>` (1 = lowest signal … 5 = highest), `nstocks` and `ret_vw`, the
value-weighted monthly return **in percent**.

`metrics_catalog.json` is the single source of truth for what each code means.
The app and the docs both read it, so they cannot drift apart.

No vintage is hard-coded anywhere — the loader reads it off the filenames.

## Updating to a new release

```bash
python scripts/fetch_data.py --vintage 2026   # download and lay out the new files
python scripts/build_docs.py                  # regenerate the markdown docs
```

Full instructions, including what to do when a release adds or drops an
anomaly, are in [docs/UPDATING.md](docs/UPDATING.md).

## Project structure

```
app.py                      Streamlit entry point and the Portfolio Analysis view
src/
├── data_loader.py          vintage detection, file discovery, loading
├── data_processor.py       portfolio statistics
├── analysis.py             rolling statistics, drawdowns, market-relative stats
├── factor_models.py        CAPM / q-factor / q5 regressions, spread construction
├── metrics.py              access to the metric catalog
├── views.py                Metric Reference and Factor Model Alphas
└── visualizations.py       plotly chart builders
scripts/
├── fetch_data.py           download a vintage from global-q.org
└── build_docs.py           regenerate docs from the catalog
docs/
├── METRICS.md              metric index and library conventions
├── metrics/                one page per category, full detail per anomaly
├── REFERENCES.md           the papers behind the library
├── UPDATING.md             how to move to a new data release
└── portfoliostd_2026jul.pdf  the library's own technical document
```

## Dependencies

streamlit, pandas, numpy, plotly, scipy, statsmodels, seaborn, matplotlib,
python-dateutil. See `requirements.txt`.

## Tests

```bash
pip install pytest
pytest tests/
```

`tests/test_app.py` renders all three views and, critically, selects a factor
first — the Portfolio Analysis code only runs after a selection, so a
load-the-page check never reaches it. Two pandas releases have broken exactly
that path.

Streamlit Cloud installs the newest version of everything in
`requirements.txt`, so it is worth running the tests against the latest
packages before a push:

```bash
python -m venv .venv-latest
.venv-latest/Scripts/pip install -U -r requirements.txt pytest
.venv-latest/Scripts/python -m pytest tests/ -W error::FutureWarning
```

Promoting `FutureWarning` to an error catches the next deprecation before it
becomes an outage.

## Sources and credit

The data and its construction are entirely the work of Kewei Hou, Chen Xue and
Lu Zhang, published at <https://global-q.org>. The four q-factor papers and the
technical documents are listed in [docs/REFERENCES.md](docs/REFERENCES.md).

Check the terms on global-q.org before redistributing the data.

## Notes on reading the output

- **Direction fields are expectations, not results.** Where the technical
  document does not state which end of a sort should win, the metric pages use
  the standard sign from the literature. The Factor Model Alphas view is where
  you see what the data actually did.
- **Attribution is only as good as the source.** The technical document names an
  originating paper for 89 of the 201 anomalies. The rest are marked as having
  no named source rather than being given a guessed citation.
- **Some series start late.** Analyst-based signals begin in the 1970s,
  systematic volatility in 1990. Each metric page states its start.

## Troubleshooting

**Port already in use** — Streamlit picks the next free port; check the terminal
for the URL.

**`No metric catalog found`** — `data/metrics_catalog.json` is missing. It is
committed to the repo; restore it, or see [docs/UPDATING.md](docs/UPDATING.md).

**`No q-factor return file found`** — the Factor Model Alphas view needs
`data/q5_factors_monthly_<vintage>.csv`. Run
`python scripts/fetch_data.py --vintage <vintage>` to fetch it.

**Memory** — loading all 200 anomaly files takes a few hundred MB. Streamlit
caches them, so the first load is the slow one.
