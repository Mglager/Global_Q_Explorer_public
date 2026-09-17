# Updating to a new data release

global-q.org republishes the whole testing-portfolio library roughly once a
year. The last sample year is stamped into every filename, so a release is
identified by its **vintage**: the files shipped here are the `2025` vintage,
released July 2026, covering January 1967 to December 2025.

Nothing in the code hard-codes a vintage. The loader reads it off the filenames
(`DataLoader.detect_vintage`), so dropping in new files is enough to move the
app forward.

## 1. Fetch the new vintage

```bash
python scripts/fetch_data.py --vintage 2026
```

This downloads the six size-interacted category archives, pulls the size-decile
market portfolio out of the one-way frictions archive, grabs the q5 factor
returns, removes the previous vintage and lays everything out as:

```
data/me_mom_monthly_2026/portf_me_<code>_monthly_2026.csv
data/me_vvg_monthly_2026/...
data/me_inv_monthly_2026/...
data/me_prof_monthly_2026/...
data/me_intan_monthly_2026/...
data/me_fric_monthly_2026/...
data/portf_me_monthly_2026.csv
data/q5_factors_monthly_2026.csv
```

Pass `--keep-old` if you want both vintages side by side. The app will then use
the newest one, because `detect_vintage` takes the maximum year.

The script finishes by comparing the file list against
`data/metrics_catalog.json` and telling you which anomalies are new or gone.

> One quirk worth knowing: the published archives are not always named
> consistently inside. The 2025 value-versus-growth archive unpacks to a folder
> called `me_monthlyl_2025`. `fetch_data.py` decides the destination from the
> archive it downloaded, never from the folder inside it, so this does not
> matter — but it will bite you if you unzip by hand.

## 2. Update the metric catalog

`data/metrics_catalog.json` is the single source of truth for metric names,
definitions, formulas and citations. It is used by both the app and the
documentation, so they cannot drift apart.

If step 1 reported no new or missing anomalies, skip to step 3.

If it did report changes, the definitions come from the release's own technical
document, linked from
<https://global-q.org/testingportfolios.html> and mirrored here as
`docs/portfoliostd_2026jul.pdf`. Find the new variable's subsection in
"Variable Definitions and Portfolio Construction" and add an entry:

```json
{
  "code": "roe_1",
  "name": "Return on Equity (1m)",
  "category": "profitability",
  "definition": "One or two sentences on what it measures and why it should predict returns.",
  "formula": "The construction, as the technical document states it.",
  "inputs": ["IBQ", "SEQQ/CEQQ/ATQ/LTQ", "TXDITCQ"],
  "sort": "NYSE deciles on most recent past Roe, monthly rebalance",
  "rebalance": "monthly",
  "holding_period": "1 month",
  "direction": "high - more profitable firms earn higher returns",
  "start": "January 1967",
  "source_paper": "Hou, Xue, and Zhang (2015)",
  "doc_section": "2.4.1"
}
```

Category keys are `momentum`, `value-growth`, `investment`, `profitability`,
`intangibles`, `frictions`.

Two conventions worth keeping:

- **`source_paper`** is filled in only where the technical document actually
  names an originating paper. Where it does not, use the exact string
  `"Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document"`.
  Do not substitute a citation from memory — the documentation states plainly
  how many anomalies have no named source, and that count should stay honest.
- **`direction`** starts with the word `high` or `low`, then a dash and a short
  reason. It is an expected sign from the literature, not a measured result.

## 3. Regenerate the documentation

```bash
python scripts/build_docs.py
```

Rewrites `docs/METRICS.md`, `docs/metrics/<category>.md` and
`docs/REFERENCES.md` from the catalog. No network access.

## 4. Check it

```bash
streamlit run app.py
```

Worth a look:

- the sidebar caption shows the new vintage and sample range;
- **Metric Reference** counts add up to the release's anomaly total;
- **Factor Model Alphas** runs, and the category screen finishes.

A quick sanity check that the wiring is right: pick `roe_1` in the
profitability category, high-minus-low. The raw spread should be strongly
positive with a large t-statistic, the q-factor alpha should collapse to near
zero, and the profitability loading should be close to 1 with a very large
t-statistic — the q model contains a profitability factor, so it had better
explain a profitability sort.

## 5. Refresh the mirrored technical document

If the release ships a new technical document, replace
`docs/portfoliostd_2026jul.pdf` with it and update the link in
`docs/REFERENCES.md`'s generator (`CORE_PAPERS` in `scripts/build_docs.py`).
