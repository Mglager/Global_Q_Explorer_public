# Intangibles

Signals built from assets that do not sit cleanly on the balance sheet - R&D, organisational capital, advertising, operating leverage - plus the return seasonality family.

33 anomalies. Definitions from Kewei Hou, Chen Xue, and Lu Zhang, "Technical Document: Testing Portfolios," global-q.org, July 2026.

[<- back to the metric index](../METRICS.md)

## Summary

| Code | Metric | What it measures | Which end wins | Rebalance | Holding | Starts |
|---|---|---|---|---|---|---|
| `adm` | [Advertising Expense-to-Market](#adm) | Advertising spending scaled by market value. Advertising builds brand capital that is expensed immediately rather than capitalized, so the market may underprice firms with large advertising outlays relative to their size, similar in spirit to R&D-to-market. | High | annual (June) | 12 months | July 1973 |
| `alaq_1` | [Asset Liquidity-to-Assets (1m)](#alaq-1) | Share of a firm's balance sheet held in liquid, easily redeployable assets (cash, near-cash current assets, and tangible fixed assets), scaled by total assets. Low asset liquidity means capital is harder to redeploy, which raises risk. | Low | monthly | 1 month | January 1976 |
| `vcf_1` | [Cash Flow Volatility (1m)](#vcf-1) | Standard deviation of operating cash flow scaled by sales over the trailing 16 quarters, capturing the stability of a firm's cash-generating ability. | Low | monthly | 1 month | January 1978 |
| `dls_1` | [Disparity Between Long- and Short-Term Earnings Growth Forecasts (1m)](#dls-1) | Following Da and Warachka (2011), the gap between analysts' consensus long-term earnings growth forecast and the growth rate implied by comparing this year's consensus EPS forecast to last year's actual EPS. A large positive gap signals analysts extrapolating overly optimistic long-run growth beyond what near-term realizations support. | Low | monthly | 1 month | January 1982 |
| `eprd` | [Earnings Predictability](#eprd) | Residual volatility from a firm-level first-order autoregressive model of annual EPS estimated over a rolling 10-year window, following Francis, LaFond, Olsson, and Schipper (2004); higher residual volatility means earnings are less predictable from their own past values, a proxy for lower earnings quality. | High | annual (June) | 12 months | January 1967 |
| `etl` | [Earnings Timeliness](#etl) | R-squared from a rolling regression of earnings on contemporaneous stock returns (with an added term for negative-return periods), following Francis, LaFond, Olsson, and Schipper (2004); measures how quickly and fully accounting earnings reflect information already impounded in stock returns. | Low | annual (June) | 12 months | January 1967 |
| `etr` | [Effective Tax Rate](#etr) | A fundamental-analysis signal, following Abarbanell and Bushee (1998), comparing a firm's current effective tax rate to its trailing 3-year average effective tax rate, scaled by the direction of the change in EPS; intended to capture tax-driven earnings-quality information. | Low | annual (June) | 12 months | January 1967 |
| `hs` | [Industry Concentration in Sales](#hs) | Herfindahl index of sales market shares within a firm's 3-digit SIC industry, averaged over the past 3 years, following Hou and Robinson (2006); measures the degree of competition a firm faces, which the paper links to priced competitive risk. | Low | annual (June) | 12 months | January 1967 |
| `ioca` | [Industry-Adjusted Organizational Capital-to-Assets](#ioca) | Industry-standardized version of Oca: a firm's Oca demeaned by its Fama-French 17-industry mean and divided by the industry standard deviation, isolating organizational-capital intensity relative to industry peers rather than the whole market. | High | annual (June) | 12 months | January 1967 |
| `rer` | [Industry-Adjusted Real Estate Ratio](#rer) | Share of a firm's property, plant and equipment held as real estate (buildings and capital leases), measured relative to its industry, following Tuzel (2010); real-estate-intensive firms carry distinct exposure to commercial property value risk. | High | annual (June) | 12 months | July 1970 |
| `ol` | [Operating Leverage](#ol) | Fixed-cost intensity of operations: total operating costs relative to total assets. Higher operating leverage amplifies the sensitivity of profits to revenue shocks, which raises the firm's systematic risk and expected return. | High | annual (June) | 12 months | January 1967 |
| `oca` | [Organizational Capital-to-Assets](#oca) | Measures the accumulated stock of a firm's organization capital, built up from cumulative SG&A spending, scaled by total assets. Following Eisfeldt and Papanikolaou (2013), the idea is that SG&A creates firm-specific organizational capital -- an intangible asset omitted from the balance sheet -- and cross-sectional differences in this intangible investment are priced. | High | annual (June) | 12 months | January 1967 |
| `almq_12` | [Quarterly Asset Liquidity-to-Market (12m)](#almq-12) | Same Almq measure as the 1-month version, held for 12 months by averaging twelve staggered monthly-formed subdecile portfolios. | Low | monthly (overlapping subdeciles, rebalanced at the start of each month) | 12 months | January 1976 |
| `almq_1` | [Quarterly Asset Liquidity-to-Market (1m)](#almq-1) | Same asset-liquidity numerator as Alaq, but scaled by the market value of the firm's assets instead of book assets, so it also reflects market pricing of the firm's asset base. | Low | monthly | 1 month | January 1976 |
| `almq_6` | [Quarterly Asset Liquidity-to-Market (6m)](#almq-6) | Same Almq measure as the 1-month version, held for 6 months by averaging six staggered monthly-formed subdecile portfolios. | Low | monthly (overlapping subdeciles, rebalanced at the start of each month) | 6 months | January 1976 |
| `olq_12` | [Quarterly Operating Leverage (12m)](#olq-12) | Same Olq measure as the 1-month version, held for 12 months by averaging twelve staggered monthly-formed subdecile portfolios. | High | monthly (overlapping subdeciles, rebalanced at the start of each month) | 12 months | January 1973 |
| `olq_1` | [Quarterly Operating Leverage (1m)](#olq-1) | Monthly-updated version of Ol using the latest quarterly operating costs scaled by quarterly total assets, allowing more timely portfolio formation than the annual Ol. | High | monthly | 1 month | January 1973 |
| `olq_6` | [Quarterly Operating Leverage (6m)](#olq-6) | Same Olq measure as the 1-month version, held for 6 months by averaging six staggered monthly-formed subdecile portfolios. | High | monthly (overlapping subdeciles, rebalanced at the start of each month) | 6 months | January 1973 |
| `rdmq_12` | [Quarterly R&D Expense-to-Market (12m)](#rdmq-12) | Same Rdmq measure as the 1-month version, held for 12 months by averaging twelve staggered monthly-formed subdecile portfolios, each initiated in a different one of the prior twelve months. | High | monthly (overlapping subdeciles, rebalanced at the start of each month) | 12 months | January 1990 |
| `rdmq_1` | [Quarterly R&D Expense-to-Market (1m)](#rdmq-1) | Monthly-updated version of Rdm: the latest quarterly R&D expense scaled by current market equity, allowing more timely portfolio formation than the annual Rdm. | High | monthly | 1 month | January 1990 |
| `rdmq_6` | [Quarterly R&D Expense-to-Market (6m)](#rdmq-6) | Same Rdmq measure as the 1-month version, held for 6 months by averaging six staggered monthly-formed subdecile portfolios, each initiated in a different one of the prior six months. | High | monthly (overlapping subdeciles, rebalanced at the start of each month) | 6 months | January 1990 |
| `rdsq_12` | [Quarterly R&D Expense-to-Sales (12m)](#rdsq-12) | Same Rdsq measure as the 6-month version, held for 12 months by averaging twelve staggered monthly-formed subdecile portfolios. | High | monthly (overlapping subdeciles, rebalanced at the start of each month) | 12 months | January 1990 |
| `rdsq_6` | [Quarterly R&D Expense-to-Sales (6m)](#rdsq-6) | R&D intensity measured against sales rather than market value, using the latest quarterly R&D expense scaled by quarterly sales; captures innovation intensity independent of valuation. Held 6 months via averaged staggered subdeciles. | High | monthly (overlapping subdeciles, rebalanced at the start of each month) | 6 months | January 1990 |
| `rca` | [R&D Capital-to-Assets](#rca) | Stock of accumulated, depreciated R&D spending (R&D capital) scaled by total assets, following Li (2011); captures a firm's cumulative innovation investment rather than a single year's R&D flow. | High | annual (June) | 12 months | July 1980 |
| `rdm` | [R&D Expense-to-Market](#rdm) | R&D spending scaled by market value. Like Adm, this captures expensed intangible (innovation) investment that is not reflected in book value, which the market may not fully price into the stock. | High | annual (June) | 12 months | July 1976 |
| `r1a` | [Return Seasonality, 12-Month Lag (1m)](#r1a) | Following Heston and Sadka (2008), a return-seasonality measure based on a stock's own return exactly one year earlier (the same calendar month), testing whether stock returns recur seasonally at annual-multiple lags. | High | monthly | 1 month | January 1967 |
| `r15a` | [Return Seasonality, Annual Lags Years 11-15 (1m)](#r15a) | Following Heston and Sadka (2008), the average of a stock's returns at the annual-anniversary lags falling in years 11 through 15 (months t-132, t-144, t-156, t-168, t-180), testing return seasonality at very long horizons. | High | monthly | 1 month | January 1967 |
| `r20a` | [Return Seasonality, Annual Lags Years 16-20 (1m)](#r20a) | Following Heston and Sadka (2008), the average of a stock's returns at the annual-anniversary lags falling in years 16 through 20 (months t-192, t-204, t-216, t-228, t-240), the longest-horizon seasonality measure in the document. | High | monthly | 1 month | January 1967 |
| `r5a` | [Return Seasonality, Annual Lags Years 2-5 (1m)](#r5a) | Following Heston and Sadka (2008), the average of a stock's returns at the annual-anniversary lags falling in years 2 through 5 (months t-24, t-36, t-48, t-60), testing whether return seasonality persists beyond the first year. | High | monthly | 1 month | January 1967 |
| `r10a` | [Return Seasonality, Annual Lags Years 6-10 (1m)](#r10a) | Following Heston and Sadka (2008), the average of a stock's returns at the annual-anniversary lags falling in years 6 through 10 (months t-72, t-84, t-96, t-108, t-120), testing whether return seasonality persists a decade out. | High | monthly | 1 month | January 1967 |
| `r1n` | [Return Seasonality, Non-Annual Lags Year 1 (1m)](#r1n) | Following Heston and Sadka (2008), the average of a stock's returns over the eleven months of the prior year that do NOT fall on the annual seasonal lag, used as a non-seasonal benchmark against R1a. | High | monthly | 1 month | January 1967 |
| `r5n` | [Return Seasonality, Non-Annual Lags Years 2-5 (1m)](#r5n) | Following Heston and Sadka (2008), the average of a stock's returns over months t-60 to t-13 excluding the four annual seasonal lags (t-24, t-36, t-48, t-60), used as the non-seasonal benchmark against R5a. | High | monthly | 1 month | January 1967 |
| `r10n` | [Return Seasonality, Non-Annual Lags Years 6-10 (1m)](#r10n) | Following Heston and Sadka (2008), the average of a stock's returns over months t-120 to t-61 excluding the five annual seasonal lags (t-72, t-84, t-96, t-108, t-120), used as the non-seasonal benchmark against R10a. | High | monthly | 1 month | January 1967 |

## Detail

<a id="adm"></a>

### Advertising Expense-to-Market - `adm`

Advertising spending scaled by market value. Advertising builds brand capital that is expensed immediately rather than capitalized, so the market may underprice firms with large advertising outlays relative to their size, similar in spirit to R&D-to-market.

**Construction**

```
Adm = advertising expense (Compustat annual item XAD) for the fiscal year ending in calendar year t-1, divided by market equity (CRSP) at the end of December of t-1. For firms with more than one share class, market equity is merged across classes before computing Adm. Only firms with positive advertising expense are kept.
```

| | |
|---|---|
| **Inputs** | `Advertising expense (Compustat item XAD)`, `Market equity (Me, CRSP)` |
| **Portfolio sort** | Firms with positive XAD sorted into deciles (and separately quintiles) on Adm at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Adm portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - high advertising-to-market predicts higher subsequent returns, consistent with intangible-investment mispricing |
| **Series starts** | July 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.2 |

[^ summary table](#summary)

<a id="alaq-1"></a>

### Asset Liquidity-to-Assets (1m) - `alaq_1`

Share of a firm's balance sheet held in liquid, easily redeployable assets (cash, near-cash current assets, and tangible fixed assets), scaled by total assets. Low asset liquidity means capital is harder to redeploy, which raises risk.

**Construction**

```
Asset liquidity = cash and short-term investments (item CHEQ) + 0.75 x noncash current assets (current assets [item ACTQ] minus cash) + 0.50 x tangible fixed assets (total assets [item ATQ] minus current assets [item ACTQ] minus intangibles [item INTANQ, zero if missing]). Alaq = asset liquidity scaled by 1-quarter-lagged total assets.
```

| | |
|---|---|
| **Inputs** | `Cash and short-term investments (item CHEQ)`, `Current assets (item ACTQ)`, `Total assets (item ATQ)`, `Intangibles (item INTANQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Alaq at the beginning of each month t, using the fiscal quarter ending at least 4 months ago; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Alaq portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - less liquid, harder-to-redeploy assets carry higher priced risk |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.15 |

[^ summary table](#summary)

<a id="vcf-1"></a>

### Cash Flow Volatility (1m) - `vcf_1`

Standard deviation of operating cash flow scaled by sales over the trailing 16 quarters, capturing the stability of a firm's cash-generating ability.

**Construction**

```
Vcf = standard deviation, over the past 16 quarters (minimum 8 nonmissing), of [operating cash flow / sales (item SALEQ)], where operating cash flow = income before extraordinary items (item IBQ) + depreciation and amortization (item DPQ) + change in working capital (item WCAPQ) from the prior quarter.
```

| | |
|---|---|
| **Inputs** | `Income before extraordinary items (Compustat item IBQ)`, `Depreciation and amortization (item DPQ)`, `Working capital (item WCAPQ)`, `Sales (item SALEQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Vcf at the beginning of each month t, using the fiscal quarter ending at least 4 months ago; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Vcf portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - more stable (lower-volatility) operating cash flows earn higher average returns, consistent with the low-risk cash-flow-volatility literature |
| **Series starts** | January 1978 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.12 |

[^ summary table](#summary)

<a id="dls-1"></a>

### Disparity Between Long- and Short-Term Earnings Growth Forecasts (1m) - `dls_1`

Following Da and Warachka (2011), the gap between analysts' consensus long-term earnings growth forecast and the growth rate implied by comparing this year's consensus EPS forecast to last year's actual EPS. A large positive gap signals analysts extrapolating overly optimistic long-run growth beyond what near-term realizations support.

**Construction**

```
Implied short-term growth forecast = 100 x (A1t - A0t)/|A0t|, where A1t = analysts' consensus median EPS forecast for the current fiscal year (unadjusted IBES item MEDEST, fiscal period indicator = 1) and A0t = actual EPS for the latest reported fiscal year (item FY0A, measure indicator = EPS); both must be denominated in USD. Dls = consensus median long-term earnings growth forecast (item MEDEST, fiscal period indicator = 0) minus the implied short-term growth forecast.
```

| | |
|---|---|
| **Inputs** | `IBES consensus EPS forecast (item MEDEST, fpi=1)`, `Actual EPS (item FY0A)`, `IBES consensus long-term growth forecast (item MEDEST, fpi=0)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Dls, computed with analyst forecasts reported in month t-1, at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Dls portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - a large disparity (overly optimistic long-term forecast relative to realized short-term growth) predicts lower future returns as expectations correct (Da and Warachka 2011) |
| **Series starts** | January 1982 |
| **Credited paper** | Da and Warachka (2011) |
| **Technical document** | section 2.5.16 |

[^ summary table](#summary)

<a id="eprd"></a>

### Earnings Predictability - `eprd`

Residual volatility from a firm-level first-order autoregressive model of annual EPS estimated over a rolling 10-year window, following Francis, LaFond, Olsson, and Schipper (2004); higher residual volatility means earnings are less predictable from their own past values, a proxy for lower earnings quality.

**Construction**

```
Estimate an AR(1) model of split-adjusted annual EPS (item EPSPX / item AJEX) over a rolling 10-year window up to the fiscal year ending in t-1 (only firms with a complete 10-year history included). Eprd = the residual volatility of this regression.
```

| | |
|---|---|
| **Inputs** | `Split-adjusted EPS (item EPSPX / item AJEX)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Eprd, formed at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Eprd portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - poor earnings predictability (higher residual volatility) commands an information-risk premium |
| **Series starts** | January 1967 |
| **Credited paper** | Francis, LaFond, Olsson, and Schipper (2004) |
| **Technical document** | section 2.5.13 |

[^ summary table](#summary)

<a id="etl"></a>

### Earnings Timeliness - `etl`

R-squared from a rolling regression of earnings on contemporaneous stock returns (with an added term for negative-return periods), following Francis, LaFond, Olsson, and Schipper (2004); measures how quickly and fully accounting earnings reflect information already impounded in stock returns.

**Construction**

```
EARN(i,t) = alpha0 + alpha1 x NEG(i,t) + beta1 x R(i,t) + beta2 x NEG(i,t) x R(i,t) + e(i,t), estimated over a rolling 10-year window (complete history required), where EARN = earnings (item IB) for the fiscal year ending in t, scaled by fiscal year-end market equity; R = the firm's 15-month stock return ending 3 months after fiscal year-end; NEG = 1 if R < 0, else 0. Market equity merged across share classes. Etl = the R-squared of this regression, computed over the window up to the fiscal year ending in t-1.
```

| | |
|---|---|
| **Inputs** | `Earnings (Compustat item IB)`, `Market equity (Me, CRSP)`, `15-month stock return` |
| **Portfolio sort** | Firms with a complete 10-year history sorted into deciles (and separately quintiles) on Etl, formed at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Etl portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - less timely earnings recognition implies a higher information-risk premium |
| **Series starts** | January 1967 |
| **Credited paper** | Francis, LaFond, Olsson, and Schipper (2004) |
| **Technical document** | section 2.5.14 |

[^ summary table](#summary)

<a id="etr"></a>

### Effective Tax Rate - `etr`

A fundamental-analysis signal, following Abarbanell and Bushee (1998), comparing a firm's current effective tax rate to its trailing 3-year average effective tax rate, scaled by the direction of the change in EPS; intended to capture tax-driven earnings-quality information.

**Construction**

```
Etr(t) = [TaxExpense(t)/EBT(t) - (1/3) x Sum_{tau=1}^{3} TaxExpense(t-tau)/EBT(t-tau)] x dEPS(t), where TaxExpense = total income taxes (item TXT), EBT = pretax income (item PI), and dEPS = change in split-adjusted EPS (item EPSPX / item AJEX) between t-1 and t, deflated by the split-adjusted stock price (item PRCC_F / item AJEX) at the end of t-1.
```

| | |
|---|---|
| **Inputs** | `Total income taxes (Compustat item TXT)`, `Pretax income (item PI)`, `EPS (item EPSPX / item AJEX)`, `Stock price (item PRCC_F / item AJEX)` |
| **Portfolio sort** | All firms sorted into deciles (and separately quintiles) on Etr for the fiscal year ending in t-1, formed at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Etr portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - a falling effective tax rate relative to trend is a bullish earnings-quality signal (Abarbanell and Bushee 1998) |
| **Series starts** | January 1967 |
| **Credited paper** | Abarbanell and Bushee (1998) |
| **Technical document** | section 2.5.10 |

[^ summary table](#summary)

<a id="hs"></a>

### Industry Concentration in Sales - `hs`

Herfindahl index of sales market shares within a firm's 3-digit SIC industry, averaged over the past 3 years, following Hou and Robinson (2006); measures the degree of competition a firm faces, which the paper links to priced competitive risk.

**Construction**

```
Hs = average, over the past 3 years, of Sum_j(s_ij)^2, where s_ij is firm i's share of industry j sales (Compustat item SALE) and industries are defined by 3-digit SIC codes. Financial firms (SIC 6000-6999) and specified regulated industries (railroads through 1980, trucking through 1980, airlines through 1978, telecom through 1982, gas/electric utilities) are excluded; industries with fewer than 5 firms or less than 80% firm coverage are excluded.
```

| | |
|---|---|
| **Inputs** | `Sales (Compustat item SALE)`, `3-digit SIC industry classification` |
| **Portfolio sort** | All firms sorted into deciles (and separately quintiles) on Hs for the fiscal year ending in t-1, formed at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Hs portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms in more competitive (less concentrated) industries earn higher returns, per Hou and Robinson (2006) |
| **Series starts** | January 1967 |
| **Credited paper** | Hou and Robinson (2006) |
| **Technical document** | section 2.5.9 |

[^ summary table](#summary)

<a id="ioca"></a>

### Industry-Adjusted Organizational Capital-to-Assets - `ioca`

Industry-standardized version of Oca: a firm's Oca demeaned by its Fama-French 17-industry mean and divided by the industry standard deviation, isolating organizational-capital intensity relative to industry peers rather than the whole market.

**Construction**

```
Ioca = (Oca - industry mean of Oca) / (industry standard deviation of Oca), using the Fama and French (1997) 17-industry classification. Oca is winsorized at the 1st and 99th percentiles across all firms each year before industry standardization.
```

| | |
|---|---|
| **Inputs** | `Oca`, `Fama-French (1997) 17-industry classification` |
| **Portfolio sort** | All firms sorted into deciles (and separately quintiles) on Ioca for the fiscal year ending in t-1, formed at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Ioca portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - same organizational-capital risk story as Oca, measured relative to industry peers |
| **Series starts** | January 1967 |
| **Credited paper** | Eisfeldt and Papanikolaou (2013) |
| **Technical document** | section 2.5.1 |

[^ summary table](#summary)

<a id="rer"></a>

### Industry-Adjusted Real Estate Ratio - `rer`

Share of a firm's property, plant and equipment held as real estate (buildings and capital leases), measured relative to its industry, following Tuzel (2010); real-estate-intensive firms carry distinct exposure to commercial property value risk.

**Construction**

```
Real estate ratio = (buildings [item PPENB] + capital leases [item PPENLS]) / net PP&E (item PPENT), used prior to 1983; from 1984 onward, = (buildings at cost [item FATB] + leases at cost [item FATL]) / gross PP&E (item PPEGT). Rer = real estate ratio minus its 2-digit SIC industry average (industries with fewer than 5 firms excluded); the real estate ratio is winsorized at the 1st and 99th percentiles each year before computing Rer.
```

| | |
|---|---|
| **Inputs** | `Buildings (item PPENB, pre-1983) / buildings at cost (item FATB, 1984+)`, `Capital leases (item PPENLS, pre-1983) / leases at cost (item FATL, 1984+)`, `Net PP&E (item PPENT, pre-1983) / gross PP&E (item PPEGT, 1984+)`, `2-digit SIC industry classification` |
| **Portfolio sort** | All firms sorted into deciles (and separately quintiles) on Rer for the fiscal year ending in t-1, formed at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Rer portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - greater industry-relative real-estate intensity carries priced real-estate risk (Tuzel 2010) |
| **Series starts** | July 1970 |
| **Credited paper** | Tuzel (2010) |
| **Technical document** | section 2.5.11 |

[^ summary table](#summary)

<a id="ol"></a>

### Operating Leverage - `ol`

Fixed-cost intensity of operations: total operating costs relative to total assets. Higher operating leverage amplifies the sensitivity of profits to revenue shocks, which raises the firm's systematic risk and expected return.

**Construction**

```
Ol = (cost of goods sold [item COGS] + SG&A [item XSGA]) / total assets (item AT, current, not lagged), for the fiscal year ending in calendar year t-1.
```

| | |
|---|---|
| **Inputs** | `Cost of goods sold (Compustat item COGS)`, `SG&A (Compustat item XSGA)`, `Total assets (item AT)` |
| **Portfolio sort** | All firms sorted into deciles (and separately quintiles) on Ol for the fiscal year ending in t-1, formed at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Ol portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - high operating leverage raises systematic risk and expected return |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.6 |

[^ summary table](#summary)

<a id="oca"></a>

### Organizational Capital-to-Assets - `oca`

Measures the accumulated stock of a firm's organization capital, built up from cumulative SG&A spending, scaled by total assets. Following Eisfeldt and Papanikolaou (2013), the idea is that SG&A creates firm-specific organizational capital -- an intangible asset omitted from the balance sheet -- and cross-sectional differences in this intangible investment are priced.

**Construction**

```
Oc(i,t) = (1 - delta) x Oc(i,t-1) + SG&A(i,t)/CPI(t), with annual depreciation delta = 15%. Initial stock Oc(i,0) = SG&A(i,0)/(g + delta), g = 10% long-term SG&A growth rate; missing SG&A after the start date treated as zero. Oca = Oc scaled by inflation-adjusted total assets (item AT). Firms with zero Oc excluded; SG&A must be nonmissing for the fiscal year ending in t-1.
```

| | |
|---|---|
| **Inputs** | `SG&A (Compustat annual item XSGA)`, `Consumer price index (CPI)`, `Total assets (item AT)` |
| **Portfolio sort** | All firms sorted into deciles (and separately quintiles) on Oca for the fiscal year ending in calendar year t-1, formed at the end of June of year t; independently, firms split into micro/small/big by NYSE 20th/50th percentile of June-end market equity (Me); intersections give 15 Me-Oca portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - organizational capital is a priced firm-specific risk exposure, per Eisfeldt and Papanikolaou (2013) |
| **Series starts** | January 1967 |
| **Credited paper** | Eisfeldt and Papanikolaou (2013) |
| **Technical document** | section 2.5.1 |

[^ summary table](#summary)

<a id="almq-12"></a>

### Quarterly Asset Liquidity-to-Market (12m) - `almq_12`

Same Almq measure as the 1-month version, held for 12 months by averaging twelve staggered monthly-formed subdecile portfolios.

**Construction**

```
Almq = asset liquidity (as defined for Alaq) scaled by 1-quarter-lagged market value of assets (total assets + market equity [PRCCQ x CSHOQ] - book equity [CEQQ]). The Almq12 decile return averages twelve subdecile returns, one from each of the twelve most recent monthly decile formations.
```

| | |
|---|---|
| **Inputs** | `Cash and short-term investments (item CHEQ)`, `Current assets (item ACTQ)`, `Total assets (item ATQ)`, `Intangibles (item INTANQ)`, `Market equity (item PRCCQ x item CSHOQ)`, `Book equity (item CEQQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Almq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Almq portfolios. |
| **Rebalance** | monthly (overlapping subdeciles, rebalanced at the start of each month) |
| **Holding period** | 12 months |
| **Which end wins** | Low - same illiquid-asset risk premium as Alaq, held twelve months |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.15 |

[^ summary table](#summary)

<a id="almq-1"></a>

### Quarterly Asset Liquidity-to-Market (1m) - `almq_1`

Same asset-liquidity numerator as Alaq, but scaled by the market value of the firm's assets instead of book assets, so it also reflects market pricing of the firm's asset base.

**Construction**

```
Almq = asset liquidity (cash [CHEQ] + 0.75 x noncash current assets + 0.50 x tangible fixed assets, as defined for Alaq) scaled by 1-quarter-lagged market value of assets, where market value of assets = total assets (ATQ) + market equity (item PRCCQ x item CSHOQ) - book equity (item CEQQ).
```

| | |
|---|---|
| **Inputs** | `Cash and short-term investments (item CHEQ)`, `Current assets (item ACTQ)`, `Total assets (item ATQ)`, `Intangibles (item INTANQ)`, `Market equity (item PRCCQ x item CSHOQ)`, `Book equity (item CEQQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Almq at the beginning of each month t, using the fiscal quarter ending at least 4 months ago; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Almq portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - same illiquid-asset risk premium as Alaq |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.15 |

[^ summary table](#summary)

<a id="almq-6"></a>

### Quarterly Asset Liquidity-to-Market (6m) - `almq_6`

Same Almq measure as the 1-month version, held for 6 months by averaging six staggered monthly-formed subdecile portfolios.

**Construction**

```
Almq = asset liquidity (as defined for Alaq) scaled by 1-quarter-lagged market value of assets (total assets + market equity [PRCCQ x CSHOQ] - book equity [CEQQ]). The Almq6 decile return averages six subdecile returns, one from each of the six most recent monthly decile formations.
```

| | |
|---|---|
| **Inputs** | `Cash and short-term investments (item CHEQ)`, `Current assets (item ACTQ)`, `Total assets (item ATQ)`, `Intangibles (item INTANQ)`, `Market equity (item PRCCQ x item CSHOQ)`, `Book equity (item CEQQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Almq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Almq portfolios. |
| **Rebalance** | monthly (overlapping subdeciles, rebalanced at the start of each month) |
| **Holding period** | 6 months |
| **Which end wins** | Low - same illiquid-asset risk premium as Alaq, held six months |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.15 |

[^ summary table](#summary)

<a id="olq-12"></a>

### Quarterly Operating Leverage (12m) - `olq_12`

Same Olq measure as the 1-month version, held for 12 months by averaging twelve staggered monthly-formed subdecile portfolios.

**Construction**

```
Olq = (quarterly COGSQ + quarterly XSGAQ) / quarterly total assets (ATQ), for the fiscal quarter ending at least 4 months ago. The Olq12 decile return averages twelve subdecile returns, one from each of the twelve most recent monthly decile formations.
```

| | |
|---|---|
| **Inputs** | `Quarterly cost of goods sold (Compustat item COGSQ)`, `Quarterly SG&A (Compustat item XSGAQ)`, `Quarterly total assets (item ATQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Olq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Olq portfolios. |
| **Rebalance** | monthly (overlapping subdeciles, rebalanced at the start of each month) |
| **Holding period** | 12 months |
| **Which end wins** | High - same operating-leverage risk story as Ol, held twelve months |
| **Series starts** | January 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.7 |

[^ summary table](#summary)

<a id="olq-1"></a>

### Quarterly Operating Leverage (1m) - `olq_1`

Monthly-updated version of Ol using the latest quarterly operating costs scaled by quarterly total assets, allowing more timely portfolio formation than the annual Ol.

**Construction**

```
Olq = (quarterly cost of goods sold [item COGSQ] + quarterly SG&A [item XSGAQ]) / quarterly total assets (item ATQ), for the fiscal quarter ending at least 4 months ago.
```

| | |
|---|---|
| **Inputs** | `Quarterly cost of goods sold (Compustat item COGSQ)`, `Quarterly SG&A (Compustat item XSGAQ)`, `Quarterly total assets (item ATQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Olq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Olq portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - same operating-leverage risk story as Ol, refreshed monthly |
| **Series starts** | January 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.7 |

[^ summary table](#summary)

<a id="olq-6"></a>

### Quarterly Operating Leverage (6m) - `olq_6`

Same Olq measure as the 1-month version, held for 6 months by averaging six staggered monthly-formed subdecile portfolios.

**Construction**

```
Olq = (quarterly COGSQ + quarterly XSGAQ) / quarterly total assets (ATQ), for the fiscal quarter ending at least 4 months ago. The Olq6 decile return averages six subdecile returns, one from each of the six most recent monthly decile formations.
```

| | |
|---|---|
| **Inputs** | `Quarterly cost of goods sold (Compustat item COGSQ)`, `Quarterly SG&A (Compustat item XSGAQ)`, `Quarterly total assets (item ATQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Olq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Olq portfolios. |
| **Rebalance** | monthly (overlapping subdeciles, rebalanced at the start of each month) |
| **Holding period** | 6 months |
| **Which end wins** | High - same operating-leverage risk story as Ol, held six months |
| **Series starts** | January 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.7 |

[^ summary table](#summary)

<a id="rdmq-12"></a>

### Quarterly R&D Expense-to-Market (12m) - `rdmq_12`

Same Rdmq measure as the 1-month version, held for 12 months by averaging twelve staggered monthly-formed subdecile portfolios, each initiated in a different one of the prior twelve months.

**Construction**

```
Rdmq = quarterly R&D expense (XRDQ) for the fiscal quarter ending at least 4 months ago, scaled by market equity (CRSP) at end of month t-1; only positive-R&D firms. The Rdmq12 decile return averages twelve subdecile returns, one from each of the twelve most recent monthly decile formations.
```

| | |
|---|---|
| **Inputs** | `Quarterly R&D expense (Compustat item XRDQ)`, `Market equity (Me, CRSP)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Rdmq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Rdmq portfolios. |
| **Rebalance** | monthly (overlapping subdeciles, rebalanced at the start of each month) |
| **Holding period** | 12 months |
| **Which end wins** | High - same R&D mispricing story as Rdm, held twelve months |
| **Series starts** | January 1990 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.4 |

[^ summary table](#summary)

<a id="rdmq-1"></a>

### Quarterly R&D Expense-to-Market (1m) - `rdmq_1`

Monthly-updated version of Rdm: the latest quarterly R&D expense scaled by current market equity, allowing more timely portfolio formation than the annual Rdm.

**Construction**

```
Rdmq = quarterly R&D expense (Compustat quarterly item XRDQ) for the fiscal quarter ending at least 4 months ago, scaled by market equity (CRSP) at the end of month t-1; market equity merged across share classes; only firms with positive R&D expense kept.
```

| | |
|---|---|
| **Inputs** | `Quarterly R&D expense (Compustat item XRDQ)`, `Market equity (Me, CRSP)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Rdmq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Rdmq portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - same R&D mispricing story as Rdm, refreshed monthly |
| **Series starts** | January 1990 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.4 |

[^ summary table](#summary)

<a id="rdmq-6"></a>

### Quarterly R&D Expense-to-Market (6m) - `rdmq_6`

Same Rdmq measure as the 1-month version, held for 6 months by averaging six staggered monthly-formed subdecile portfolios, each initiated in a different one of the prior six months.

**Construction**

```
Rdmq = quarterly R&D expense (XRDQ) for the fiscal quarter ending at least 4 months ago, scaled by market equity (CRSP) at end of month t-1; only positive-R&D firms. The Rdmq6 decile return averages six subdecile returns, one from each of the six most recent monthly decile formations.
```

| | |
|---|---|
| **Inputs** | `Quarterly R&D expense (Compustat item XRDQ)`, `Market equity (Me, CRSP)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Rdmq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Rdmq portfolios. |
| **Rebalance** | monthly (overlapping subdeciles, rebalanced at the start of each month) |
| **Holding period** | 6 months |
| **Which end wins** | High - same R&D mispricing story as Rdm, held six months |
| **Series starts** | January 1990 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.4 |

[^ summary table](#summary)

<a id="rdsq-12"></a>

### Quarterly R&D Expense-to-Sales (12m) - `rdsq_12`

Same Rdsq measure as the 6-month version, held for 12 months by averaging twelve staggered monthly-formed subdecile portfolios.

**Construction**

```
Rdsq = quarterly R&D expense (Compustat quarterly item XRDQ) scaled by sales (item SALEQ) for the fiscal quarter ending at least 4 months ago; only positive-R&D firms. The Rdsq12 decile return averages twelve subdecile returns, one from each of the twelve most recent monthly decile formations.
```

| | |
|---|---|
| **Inputs** | `Quarterly R&D expense (Compustat item XRDQ)`, `Quarterly sales (Compustat item SALEQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Rdsq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Rdsq portfolios. |
| **Rebalance** | monthly (overlapping subdeciles, rebalanced at the start of each month) |
| **Holding period** | 12 months |
| **Which end wins** | High - high R&D intensity relative to sales predicts higher returns, same intangible-investment logic as Rdm |
| **Series starts** | January 1990 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.5 |

[^ summary table](#summary)

<a id="rdsq-6"></a>

### Quarterly R&D Expense-to-Sales (6m) - `rdsq_6`

R&D intensity measured against sales rather than market value, using the latest quarterly R&D expense scaled by quarterly sales; captures innovation intensity independent of valuation. Held 6 months via averaged staggered subdeciles.

**Construction**

```
Rdsq = quarterly R&D expense (Compustat quarterly item XRDQ) scaled by sales (item SALEQ) for the fiscal quarter ending at least 4 months ago; only positive-R&D firms. The Rdsq6 decile return averages six subdecile returns, one from each of the six most recent monthly decile formations.
```

| | |
|---|---|
| **Inputs** | `Quarterly R&D expense (Compustat item XRDQ)`, `Quarterly sales (Compustat item SALEQ)` |
| **Portfolio sort** | Firms sorted into deciles (and separately quintiles) on Rdsq at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-Rdsq portfolios. |
| **Rebalance** | monthly (overlapping subdeciles, rebalanced at the start of each month) |
| **Holding period** | 6 months |
| **Which end wins** | High - high R&D intensity relative to sales predicts higher returns, same intangible-investment logic as Rdm |
| **Series starts** | January 1990 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.5 |

[^ summary table](#summary)

<a id="rca"></a>

### R&D Capital-to-Assets - `rca`

Stock of accumulated, depreciated R&D spending (R&D capital) scaled by total assets, following Li (2011); captures a firm's cumulative innovation investment rather than a single year's R&D flow.

**Construction**

```
Rc(i,t) = XRD(i,t) + 0.8 x XRD(i,t-1) + 0.6 x XRD(i,t-2) + 0.4 x XRD(i,t-3) + 0.2 x XRD(i,t-4) (5-year accumulation with linear 20%-per-year depreciation). Rca = Rc scaled by total assets (item AT). Only firms with positive Rc are kept; R&D expense must be nonmissing for the fiscal year ending in t-1.
```

| | |
|---|---|
| **Inputs** | `R&D expense (Compustat item XRD), trailing 5 fiscal years`, `Total assets (item AT)` |
| **Portfolio sort** | Firms with positive Rc sorted into deciles (and separately quintiles) on Rca for the fiscal year ending in t-1, formed at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Rca portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - larger accumulated R&D capital predicts higher returns via financing-constraint/innovation risk (Li 2011) |
| **Series starts** | July 1980 |
| **Credited paper** | Li (2011) |
| **Technical document** | section 2.5.8 |

[^ summary table](#summary)

<a id="rdm"></a>

### R&D Expense-to-Market - `rdm`

R&D spending scaled by market value. Like Adm, this captures expensed intangible (innovation) investment that is not reflected in book value, which the market may not fully price into the stock.

**Construction**

```
Rdm = R&D expense (Compustat annual item XRD) for the fiscal year ending in calendar year t-1, divided by market equity (CRSP) at the end of December of t-1; market equity merged across share classes. Only firms with positive R&D expense are kept.
```

| | |
|---|---|
| **Inputs** | `R&D expense (Compustat item XRD)`, `Market equity (Me, CRSP)` |
| **Portfolio sort** | Firms with positive XRD sorted into deciles (and separately quintiles) on Rdm at the end of June of year t; independently, micro/small/big split by NYSE 20th/50th percentile of June-end Me; intersections give 15 Me-Rdm portfolios. |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - high R&D-to-market predicts higher subsequent returns (intangible-investment mispricing) |
| **Series starts** | July 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.5.3 |

[^ summary table](#summary)

<a id="r1a"></a>

### Return Seasonality, 12-Month Lag (1m) - `r1a`

Following Heston and Sadka (2008), a return-seasonality measure based on a stock's own return exactly one year earlier (the same calendar month), testing whether stock returns recur seasonally at annual-multiple lags.

**Construction**

```
R1a = the stock's return in month t-12. Monthly returns must carry a CRSP flag of 'CR' or 'MP' (compounded from prior month-end to current month-end).
```

| | |
|---|---|
| **Inputs** | `Monthly stock returns (CRSP, flagged 'CR' or 'MP')` |
| **Portfolio sort** | Stocks sorted into deciles (and separately quintiles) on R1a at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-R1a portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - stocks with higher returns at the matching 12-month seasonal lag earn higher future returns (positive return seasonality, Heston and Sadka 2008) |
| **Series starts** | January 1967 |
| **Credited paper** | Heston and Sadka (2008) |
| **Technical document** | section 2.5.17 |

[^ summary table](#summary)

<a id="r15a"></a>

### Return Seasonality, Annual Lags Years 11-15 (1m) - `r15a`

Following Heston and Sadka (2008), the average of a stock's returns at the annual-anniversary lags falling in years 11 through 15 (months t-132, t-144, t-156, t-168, t-180), testing return seasonality at very long horizons.

**Construction**

```
R15a (R[11,15]a) = average of the stock's returns in months t-132, t-144, t-156, t-168, and t-180. Monthly returns must carry a CRSP flag of 'CR' or 'MP'.
```

| | |
|---|---|
| **Inputs** | `Monthly stock returns (CRSP, flagged 'CR' or 'MP')` |
| **Portfolio sort** | Stocks sorted into deciles (and separately quintiles) on R15a at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-R15a portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher returns at the years-11-15 annual seasonal lags predict higher future returns (Heston and Sadka 2008) |
| **Series starts** | January 1967 |
| **Credited paper** | Heston and Sadka (2008) |
| **Technical document** | section 2.5.17 |

[^ summary table](#summary)

<a id="r20a"></a>

### Return Seasonality, Annual Lags Years 16-20 (1m) - `r20a`

Following Heston and Sadka (2008), the average of a stock's returns at the annual-anniversary lags falling in years 16 through 20 (months t-192, t-204, t-216, t-228, t-240), the longest-horizon seasonality measure in the document.

**Construction**

```
R20a (R[16,20]a) = average of the stock's returns in months t-192, t-204, t-216, t-228, and t-240. Monthly returns must carry a CRSP flag of 'CR' or 'MP'.
```

| | |
|---|---|
| **Inputs** | `Monthly stock returns (CRSP, flagged 'CR' or 'MP')` |
| **Portfolio sort** | Stocks sorted into deciles (and separately quintiles) on R20a at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-R20a portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher returns at the years-16-20 annual seasonal lags predict higher future returns (Heston and Sadka 2008) |
| **Series starts** | January 1967 |
| **Credited paper** | Heston and Sadka (2008) |
| **Technical document** | section 2.5.17 |

[^ summary table](#summary)

<a id="r5a"></a>

### Return Seasonality, Annual Lags Years 2-5 (1m) - `r5a`

Following Heston and Sadka (2008), the average of a stock's returns at the annual-anniversary lags falling in years 2 through 5 (months t-24, t-36, t-48, t-60), testing whether return seasonality persists beyond the first year.

**Construction**

```
R5a (R[2,5]a) = average of the stock's returns in months t-24, t-36, t-48, and t-60. Monthly returns must carry a CRSP flag of 'CR' or 'MP'.
```

| | |
|---|---|
| **Inputs** | `Monthly stock returns (CRSP, flagged 'CR' or 'MP')` |
| **Portfolio sort** | Stocks sorted into deciles (and separately quintiles) on R5a at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-R5a portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher returns at the years-2-5 annual seasonal lags predict higher future returns (Heston and Sadka 2008) |
| **Series starts** | January 1967 |
| **Credited paper** | Heston and Sadka (2008) |
| **Technical document** | section 2.5.17 |

[^ summary table](#summary)

<a id="r10a"></a>

### Return Seasonality, Annual Lags Years 6-10 (1m) - `r10a`

Following Heston and Sadka (2008), the average of a stock's returns at the annual-anniversary lags falling in years 6 through 10 (months t-72, t-84, t-96, t-108, t-120), testing whether return seasonality persists a decade out.

**Construction**

```
R10a (R[6,10]a) = average of the stock's returns in months t-72, t-84, t-96, t-108, and t-120. Monthly returns must carry a CRSP flag of 'CR' or 'MP'.
```

| | |
|---|---|
| **Inputs** | `Monthly stock returns (CRSP, flagged 'CR' or 'MP')` |
| **Portfolio sort** | Stocks sorted into deciles (and separately quintiles) on R10a at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-R10a portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher returns at the years-6-10 annual seasonal lags predict higher future returns (Heston and Sadka 2008) |
| **Series starts** | January 1967 |
| **Credited paper** | Heston and Sadka (2008) |
| **Technical document** | section 2.5.17 |

[^ summary table](#summary)

<a id="r1n"></a>

### Return Seasonality, Non-Annual Lags Year 1 (1m) - `r1n`

Following Heston and Sadka (2008), the average of a stock's returns over the eleven months of the prior year that do NOT fall on the annual seasonal lag, used as a non-seasonal benchmark against R1a.

**Construction**

```
R1n = average of the stock's returns from month t-11 to month t-1. Monthly returns must carry a CRSP flag of 'CR' or 'MP'.
```

| | |
|---|---|
| **Inputs** | `Monthly stock returns (CRSP, flagged 'CR' or 'MP')` |
| **Portfolio sort** | Stocks sorted into deciles (and separately quintiles) on R1n at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-R1n portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher average non-seasonal-lag past returns predict higher future returns (Heston and Sadka 2008) |
| **Series starts** | January 1967 |
| **Credited paper** | Heston and Sadka (2008) |
| **Technical document** | section 2.5.17 |

[^ summary table](#summary)

<a id="r5n"></a>

### Return Seasonality, Non-Annual Lags Years 2-5 (1m) - `r5n`

Following Heston and Sadka (2008), the average of a stock's returns over months t-60 to t-13 excluding the four annual seasonal lags (t-24, t-36, t-48, t-60), used as the non-seasonal benchmark against R5a.

**Construction**

```
R5n (R[2,5]n) = average of the stock's returns from month t-60 to t-13, excluding lags 24, 36, 48, and 60. Monthly returns must carry a CRSP flag of 'CR' or 'MP'.
```

| | |
|---|---|
| **Inputs** | `Monthly stock returns (CRSP, flagged 'CR' or 'MP')` |
| **Portfolio sort** | Stocks sorted into deciles (and separately quintiles) on R5n at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-R5n portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher average non-seasonal-lag past returns predict higher future returns (Heston and Sadka 2008) |
| **Series starts** | January 1967 |
| **Credited paper** | Heston and Sadka (2008) |
| **Technical document** | section 2.5.17 |

[^ summary table](#summary)

<a id="r10n"></a>

### Return Seasonality, Non-Annual Lags Years 6-10 (1m) - `r10n`

Following Heston and Sadka (2008), the average of a stock's returns over months t-120 to t-61 excluding the five annual seasonal lags (t-72, t-84, t-96, t-108, t-120), used as the non-seasonal benchmark against R10a.

**Construction**

```
R10n (R[6,10]n) = average of the stock's returns from month t-120 to t-61, excluding lags 72, 84, 96, 108, and 120. Monthly returns must carry a CRSP flag of 'CR' or 'MP'.
```

| | |
|---|---|
| **Inputs** | `Monthly stock returns (CRSP, flagged 'CR' or 'MP')` |
| **Portfolio sort** | Stocks sorted into deciles (and separately quintiles) on R10n at the beginning of each month t; independently, micro/small/big split by NYSE 20th/50th percentile of prior month-end Me; intersections give 15 Me-R10n portfolios. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher average non-seasonal-lag past returns predict higher future returns (Heston and Sadka 2008) |
| **Series starts** | January 1967 |
| **Credited paper** | Heston and Sadka (2008) |
| **Technical document** | section 2.5.17 |

[^ summary table](#summary)
