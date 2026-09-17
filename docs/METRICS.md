# Metric documentation

Every testing portfolio in this app is one of **201 anomalies** published at [global-q.org](https://global-q.org/testingportfolios.html). This page explains what each one measures, how it is built and where it comes from.

The definitions are taken from the library's own technical document:

> Kewei Hou, Chen Xue, and Lu Zhang, "Technical Document: Testing Portfolios," global-q.org, July 2026.

which documents the portfolios of Hou, Xue and Zhang (2020), *Replicating Anomalies*. Full citations are in [REFERENCES.md](REFERENCES.md).

## Category pages

| Category | Anomalies | What the category is about |
|---|---:|---|
| [Momentum](metrics/momentum.md) | 43 | Signals built from recent prices, recent earnings news and the news of economically linked firms. The shared idea is that good news is priced in slowly, so past winners keep winning for a while. |
| [Value-versus-Growth](metrics/value-growth.md) | 32 | Signals that compare an accounting or cash-flow anchor to the market price. The shared idea is that a low price relative to fundamentals signals a higher expected return, whether because of risk or because of over-pessimism. |
| [Investment](metrics/investment.md) | 32 | Signals built from how fast the balance sheet is growing and how much of earnings is accrual rather than cash. The shared idea, from q-theory, is that firms invest more when their cost of capital is low, so heavy investors and heavy issuers earn less. |
| [Profitability](metrics/profitability.md) | 50 | Signals built from the level, the change and the forecast of profitability. The shared idea, again from q-theory, is that for a given amount of investment, more profitable firms must be discounted at a higher rate. |
| [Intangibles](metrics/intangibles.md) | 33 | Signals built from assets that do not sit cleanly on the balance sheet - R&D, organisational capital, advertising, operating leverage - plus the return seasonality family. |
| [Trading Frictions](metrics/frictions.md) | 11 | Signals built from trading and risk characteristics rather than fundamentals: size, beta, volatility, skewness, liquidity, tail risk and short-term reversal. |
| **Total** | **201** | |

## How the portfolios are built

| | |
|---|---|
| **Stock sample** | All domestic common stocks listed on NYSE, Amex, and Nasdaq, excluding financial firms (SIC codes 6000-6999) and firms with negative book equity; stock returns are delisting-adjusted. |
| **Sample period** | January 1967 to December 2025 (some testing portfolios start later due to data limitations) |
| **Breakpoints** | NYSE breakpoints on the anomaly variable itself for one-way deciles; for the two-way size interaction, NYSE 20th and 50th percentiles of market equity define micro-, small-, and big-cap groups. |
| **Weighting** | Value-weighted portfolio returns, using end-of-prior-month market equity as weights for monthly returns and end-of-prior-day market equity as weights for daily returns; monthly returns are compounded into quarterly and annual, and daily returns are compounded into weekly (calendar Friday-to-Friday and Wednesday-to-Wednesday). |
| **Two-way (size) sorts** | For each anomaly, stocks are independently sorted into 3 size groups (micro-, small-, and big-cap by NYSE 20th/50th percentile of market equity) and 5 anomaly-variable quintiles (NYSE breakpoints); the intersections yield 15 value-weighted two-way (3x5, 'Me-X') portfolios, alongside the one-way decile portfolios. |
| **Delisting** | CRSP's monthly returns are only partially delisting-adjusted (it omits some delisting event returns and does not impute missing ones), so the authors reverse this partial adjustment and apply their own complete delisting-adjustment procedure (Section 3), imputing missing delisting event returns from average returns by exchange and delisting type over the trailing 60 months. |

### Which anomalies are included

The 201 anomalies are a subset of the 452 anomalies in Hou, Xue, and Zhang (2020). The base set is the 158 anomalies significant (\|t\| >= 1.96) in the original January 1967-December 2016 sample, plus anomalies that became significant in later sample extensions (11 through December 2018, 1 through December 2019, 2 through December 2020, 1 through December 2021, 5 through December 2022, 2 through December 2023, 4 through December 2024, and 2 through December 2025). Anomalies that later turned insignificant are retained for backward compatibility, Hou et al.'s expected growth (1-, 6-, and 12-month holding periods) is included, and 12 additional anomalies prominent in the empirical asset pricing literature are added despite being insignificant.

## Reading the data files

This app ships the **two-way, size-interacted** portfolios. One file per anomaly:

```
data/me_prof_monthly_2025/portf_me_roe_1_monthly_2025.csv
     ^^^^^^^                      ^^^ ^          ^^^^
     category folder              code holding   vintage
                                       period
```

| Column | Meaning |
|---|---|
| `year`, `month` | Observation month |
| `rank_ME` | Size group, 1 = micro-cap ... 3 = big-cap |
| `rank_<CODE>` | Anomaly quintile, 1 = lowest signal ... 5 = highest |
| `nstocks` | Number of stocks in that cell |
| `ret_vw` | Value-weighted monthly return, **in percent** |

`data/portf_me_monthly_<vintage>.csv` holds the size deciles used as the market reference, and `data/q5_factors_monthly_<vintage>.csv` holds the q5 factor returns used by the Factor Model Alphas view.

### The trailing number in a code

`roe_1`, `roe_6` and `roe_12` are the same signal held for 1, 6 and 12 months. A longer holding period means a slower-turning portfolio, so comparing them shows how quickly a signal decays.

## Two cautions

**Attribution.** The *Credited paper* field is filled in only where the technical document itself names an originating paper. For 112 of the 201 anomalies it does not, and those entries say so rather than guessing. Many are still well-known signals with an obvious home in the literature - book-to-market is the obvious case - but this documentation does not invent a citation the source does not make.

**Direction.** The *Which end wins* field is an expected sign, not a result. The technical document mostly documents construction and not direction, so where it is silent the sign is the standard one from the literature. Use the **Factor Model Alphas** view to see what the data actually did.

---

*Generated by `scripts/build_docs.py` from `data/metrics_catalog.json`. See [UPDATING.md](UPDATING.md).*
