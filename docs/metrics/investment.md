# Investment

Signals built from how fast the balance sheet is growing and how much of earnings is accrual rather than cash. The shared idea, from q-theory, is that firms invest more when their cost of capital is low, so heavy investors and heavy issuers earn less.

32 anomalies. Definitions from Kewei Hou, Chen Xue, and Lu Zhang, "Technical Document: Testing Portfolios," global-q.org, July 2026.

[<- back to the metric index](../METRICS.md)

## Summary

| Code | Metric | What it measures | Which end wins | Rebalance | Holding | Starts |
|---|---|---|---|---|---|---|
| `ig2` | [2-Year Investment Growth](#ig2) | The two-year growth rate in capital expenditure, a longer-horizon version of investment growth capturing sustained capex ramp-ups that predict lower subsequent returns. | Low | annual (June) | 12 months | January 1967 |
| `aci` | [Abnormal Corporate Investment](#aci) | Measures whether a firm's current capital-expenditure intensity is abnormally high or low relative to its own recent 3-year average, capturing over- or under-investment relative to a trend benchmark. | Low | annual (June) | 12 months | January 1967 |
| `dbe` | [Changes in Book Equity](#dbe) | The annual change in common book equity, capturing balance-sheet equity growth as part of the same accrual/financing decomposition used for total accruals. | Low | annual (June) | 12 months | January 1967 |
| `dcoa` | [Changes in Current Operating Assets](#dcoa) | The change in current operating assets alone (current assets less cash and short-term investments), one component underlying the net working-capital accrual. | Low | annual (June) | 12 months | January 1967 |
| `dfnl` | [Changes in Financial Liabilities](#dfnl) | The change in financial liabilities (long-term debt, current debt, and preferred stock), the liability-side component of net financial assets in the total-accruals decomposition. | Low | annual (June) | 12 months | January 1967 |
| `dlti` | [Changes in Long-term Investments](#dlti) | The change in long-term investments alone, one component of net financial assets in the total-accruals decomposition. | Low | annual (June) | 12 months | January 1967 |
| `dlno` | [Changes in Long-term Net Operating Assets](#dlno) | Captures the annual change in long-term (non-current) operating assets net of long-term operating liabilities, with a depreciation add-back, scaled by average total assets — an investment-growth measure focused on fixed assets and intangibles. | Low | annual (June) | 12 months | January 1967 |
| `dfin` | [Changes in Net Financial Assets](#dfin) | The change in financial assets (short- and long-term investments) minus financial liabilities (debt and preferred stock), the financing-side component of total accruals. | Low | annual (June) | 12 months | January 1967 |
| `dwc` | [Changes in Net Non-cash Working Capital](#dwc) | The change in current operating assets minus current operating liabilities (excluding cash and short-term debt), the working-capital accrual component of total accruals. | Low | annual (June) | 12 months | January 1967 |
| `dnco` | [Changes in Net Non-current Operating Assets](#dnco) | The change in noncurrent operating assets minus noncurrent operating liabilities, the long-term-asset accrual component of total accruals. | Low | annual (June) | 12 months | January 1967 |
| `dnoa` | [Changes in Net Operating Assets](#dnoa) | The annual change in net operating assets (operating assets minus operating liabilities, as defined for Noa) scaled by lagged total assets; captures balance-sheet growth from accruals and investment that predicts lower returns. | Low | annual (June) | 12 months | January 1967 |
| `dnca` | [Changes in Non-current Operating Assets](#dnca) | The change in noncurrent operating assets alone (total assets less current assets and long-term investments), a component of the noncurrent-operating accrual. | Low | annual (June) | 12 months | January 1967 |
| `dpia` | [Changes in PP&E and Inventory-to-Assets](#dpia) | Captures the combined annual growth in fixed capital (gross property, plant and equipment) and inventory, scaled by lagged total assets — a broad measure of the physical-capital investment rate. | Low | annual (June) | 12 months | January 1967 |
| `cei` | [Composite Equity Issuance](#cei) | Captures the portion of a firm's 5-year market-equity growth that is not explained by its own stock return, i.e., growth attributable to net share issuance — a broad measure of external equity financing that predicts lower subsequent returns. | Low | annual (June) | 12 months | January 1967 |
| `dac` | [Discretionary Accruals](#dac) | The residual (abnormal) component of operating accruals after removing the portion explained by sales growth net of receivables growth and by PP&E, estimated via cross-sectional industry-year regressions — the modified-Jones-model measure of earnings management. | Low | annual (June) | 12 months | January 1967 |
| `ivc` | [Inventory Changes](#ivc) | The annual change in inventory scaled by average total assets, isolating inventory investment in asset-scaled (rather than growth-rate) terms. | Low | annual (June) | 12 months | January 1967 |
| `ivg` | [Inventory Growth](#ivg) | The one-year growth rate in inventory, a component-level investment measure; firms building inventory rapidly tend to earn lower subsequent returns. | Low | annual (June) | 12 months | January 1967 |
| `ig` | [Investment Growth](#ig) | The one-year growth rate in capital expenditure, capturing the pace of capex expansion; firms ramping up capex sharply tend to earn lower subsequent returns. | Low | annual (June) | 12 months | January 1967 |
| `ia` | [Investment-to-Assets](#ia) | Measures a firm's one-year growth rate in total assets, a standard proxy for the corporate investment rate; per q-theory, firms that invest (grow assets) more aggressively earn lower subsequent returns. | Low | annual (June) | 12 months | January 1967 |
| `ndf` | [Net Debt Financing](#ndf) | The net cash raised from long-term and current debt issuance less repayments, the debt-financing component of net external financing. | Low | annual (June) | 12 months | July 1972 |
| `nxf` | [Net External Financing](#nxf) | The sum of net equity financing and net debt financing raised over the year, a comprehensive measure of external capital raised; firms relying heavily on external financing tend to earn lower subsequent returns. | Low | annual (June) | 12 months | January 1967 |
| `noa` | [Net Operating Assets](#noa) | Net operating assets is operating assets minus operating liabilities, scaled by lagged total assets; a high level reflects balance-sheet expansion driven by accruals and investment, which is associated with lower subsequent returns. | Low | annual (June) | 12 months | January 1967 |
| `nsi` | [Net Stock Issues](#nsi) | Measures net share issuance over the prior year via the log change in split-adjusted shares outstanding; firms issuing (diluting) shares tend to underperform, while firms repurchasing shares tend to outperform. | Low | annual (June) | 12 months | January 1967 |
| `oa` | [Operating Accruals](#oa) | Operating accruals capture the non-cash component of earnings (via a working-capital balance-sheet approach pre-1988, and directly from the cash-flow statement from 1988), used to detect low earnings quality / earnings management that predicts lower future returns (the accrual anomaly). | Low | annual (June) | 12 months | January 1967 |
| `pda` | [Percent Discretionary Accruals](#pda) | Discretionary accruals rescaled from a total-assets basis to an earnings basis, by multiplying Dac by lagged total assets and dividing by the absolute value of net income — the percent-accruals analogue of Dac. | Low | annual (June) | 12 months | January 1967 |
| `poa` | [Percent Operating Accruals](#poa) | Operating accruals scaled by the absolute value of net income rather than total assets; percent-scaling better isolates firms for which sophisticated and naive earnings forecasts diverge most. | Low | annual (June) | 12 months | January 1967 |
| `pta` | [Percent Total Accruals](#pta) | Total accruals scaled by the absolute value of net income, the percent-accruals analogue of Ta, applying the same earnings-basis scaling idea used for Poa. | Low | annual (June) | 12 months | January 1967 |
| `dii` | [Percentage Change in Investment Relative to Industry](#dii) | Compares a firm's percentage change in capital investment (relative to its own 2-year average) against the same percentage change aggregated across its 2-digit SIC industry, isolating investment moves that are idiosyncratic rather than industry-wide. | Low | annual (June) | 12 months | January 1967 |
| `iaq_12` | [Quarterly Investment-to-Assets (12m)](#iaq-12) | A quarterly, higher-frequency analogue of I/A measuring the growth in total assets over the trailing four fiscal quarters; sorted monthly, it captures short-horizon investment-driven mispricing. | Low | monthly | 12 months | January 1973 |
| `iaq_1` | [Quarterly Investment-to-Assets (1m)](#iaq-1) | A quarterly, higher-frequency analogue of I/A measuring the growth in total assets over the trailing four fiscal quarters; sorted monthly, it captures short-horizon investment-driven mispricing. | Low | monthly | 1 month | January 1973 |
| `iaq_6` | [Quarterly Investment-to-Assets (6m)](#iaq-6) | A quarterly, higher-frequency analogue of I/A measuring the growth in total assets over the trailing four fiscal quarters; sorted monthly, it captures short-horizon investment-driven mispricing. | Low | monthly | 6 months | January 1973 |
| `ta` | [Total Accruals](#ta) | Total accruals extend operating accruals by decomposing the balance sheet into working-capital, noncurrent-operating, and net-financial-asset components (Richardson, Sloan, Soliman, and Tuna 2005); from 1988 measured directly from cash-flow-statement financing and investing flows. | Low | annual (June) | 12 months | January 1967 |

## Detail

<a id="ig2"></a>

### 2-Year Investment Growth - `ig2`

The two-year growth rate in capital expenditure, a longer-horizon version of investment growth capturing sustained capex ramp-ups that predict lower subsequent returns.

**Construction**

```
2Ig = CAPX_{t-1} / CAPX_{t-3} − 1, the growth rate in capital expenditure from the fiscal year ending in calendar year t−3 to the fiscal year ending in t−1.
```

| | |
|---|---|
| **Inputs** | `Compustat annual CAPX` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on 2Ig; independently, quintiles on 2Ig crossed with micro/small/big size terciles into 15 Me-2Ig portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low 2-year capex growth earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.8 |

[^ summary table](#summary)

<a id="aci"></a>

### Abnormal Corporate Investment - `aci`

Measures whether a firm's current capital-expenditure intensity is abnormally high or low relative to its own recent 3-year average, capturing over- or under-investment relative to a trend benchmark.

**Construction**

```
Aci = Ce_{t-1} / [(Ce_{t-2} + Ce_{t-3} + Ce_{t-4}) / 3] − 1, where Ce_{t-j} = CAPX / SALE for the fiscal year ending in calendar year t−j. Firms with sales below $10 million are excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat annual CAPX`, `Compustat annual SALE` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Aci; independently, quintiles on Aci crossed with micro/small/big size terciles (NYSE 20th/50th Me percentiles) into 15 Me-Aci portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low (or negative) abnormal investment earn higher returns than over-investors |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.1 |

[^ summary table](#summary)

<a id="dbe"></a>

### Changes in Book Equity - `dbe`

The annual change in common book equity, capturing balance-sheet equity growth as part of the same accrual/financing decomposition used for total accruals.

**Construction**

```
dBe = ΔCEQ, the change in book equity for the fiscal year ending in t−1, scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual CEQ`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dBe; independently, quintiles on dBe crossed with micro/small/big size terciles into 15 Me-dBe portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low growth in book equity earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.18 |

[^ summary table](#summary)

<a id="dcoa"></a>

### Changes in Current Operating Assets - `dcoa`

The change in current operating assets alone (current assets less cash and short-term investments), one component underlying the net working-capital accrual.

**Construction**

```
dCoa = ΔCoa, where Coa = ACT − CHE. The change is for the fiscal year ending in t−1, scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual ACT`, `Compustat annual CHE`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dCoa; independently, quintiles on dCoa crossed with micro/small/big size terciles into 15 Me-dCoa portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low increases in current operating assets earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.16 |

[^ summary table](#summary)

<a id="dfnl"></a>

### Changes in Financial Liabilities - `dfnl`

The change in financial liabilities (long-term debt, current debt, and preferred stock), the liability-side component of net financial assets in the total-accruals decomposition.

**Construction**

```
dFnl = ΔFnl, where Fnl = DLTT + DLC + PSTK. The change is for the fiscal year ending in t−1, scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual DLTT`, `Compustat annual DLC`, `Compustat annual PSTK`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dFnl; independently, quintiles on dFnl crossed with micro/small/big size terciles into 15 Me-dFnl portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low increases in financial liabilities (less debt/preferred financing) earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.18 |

[^ summary table](#summary)

<a id="dlti"></a>

### Changes in Long-term Investments - `dlti`

The change in long-term investments alone, one component of net financial assets in the total-accruals decomposition.

**Construction**

```
dLti = ΔIVAO, the change in long-term investments for the fiscal year ending in t−1, scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual IVAO`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dLti; independently, quintiles on dLti crossed with micro/small/big size terciles into 15 Me-dLti portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low increases in long-term investments earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.18 |

[^ summary table](#summary)

<a id="dlno"></a>

### Changes in Long-term Net Operating Assets - `dlno`

Captures the annual change in long-term (non-current) operating assets net of long-term operating liabilities, with a depreciation add-back, scaled by average total assets — an investment-growth measure focused on fixed assets and intangibles.

**Construction**

```
dLno = [ΔPPENT + ΔINTAN + ΔAO − ΔLO + DP] / [(AT_t + AT_{t-1})/2], where the changes are for the fiscal year ending in calendar year t−1, scaled by the average of total assets from the current and prior years.
```

| | |
|---|---|
| **Inputs** | `Compustat annual PPENT`, `Compustat annual INTAN`, `Compustat annual AO`, `Compustat annual LO`, `Compustat annual DP`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dLno for the fiscal year ending in t−1; independently, quintiles on dLno crossed with micro/small/big size terciles into 15 Me-dLno portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with smaller growth in long-term operating assets earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.6 |

[^ summary table](#summary)

<a id="dfin"></a>

### Changes in Net Financial Assets - `dfin`

The change in financial assets (short- and long-term investments) minus financial liabilities (debt and preferred stock), the financing-side component of total accruals.

**Construction**

```
dFin = ΔFna − ΔFnl, where Fna = IVST + IVAO and Fnl = DLTT + DLC + PSTK (missing changes set to 0, requiring at least one non-missing). The change is for the fiscal year ending in t−1, scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual IVST`, `Compustat annual IVAO`, `Compustat annual DLTT`, `Compustat annual DLC`, `Compustat annual PSTK`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dFin; independently, quintiles on dFin crossed with micro/small/big size terciles into 15 Me-dFin portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low increases in net financial assets earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.18 |

[^ summary table](#summary)

<a id="dwc"></a>

### Changes in Net Non-cash Working Capital - `dwc`

The change in current operating assets minus current operating liabilities (excluding cash and short-term debt), the working-capital accrual component of total accruals.

**Construction**

```
dWc = ΔCoa − ΔCol, where Coa = ACT − CHE and Col = LCT − DLC (missing ΔDLC set to 0). Changes are for the fiscal year ending in t−1, scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual ACT`, `Compustat annual CHE`, `Compustat annual LCT`, `Compustat annual DLC`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dWc; independently, quintiles on dWc crossed with micro/small/big size terciles into 15 Me-dWc portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low increases in net working capital earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.16 |

[^ summary table](#summary)

<a id="dnco"></a>

### Changes in Net Non-current Operating Assets - `dnco`

The change in noncurrent operating assets minus noncurrent operating liabilities, the long-term-asset accrual component of total accruals.

**Construction**

```
dNco = ΔNca − ΔNcl, where Nca = AT − ACT − IVAO and Ncl = LT − LCT − DLTT (missing ΔIVAO and ΔDLTT set to 0). Changes are for the fiscal year ending in t−1, scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual AT`, `Compustat annual ACT`, `Compustat annual IVAO`, `Compustat annual LT`, `Compustat annual LCT`, `Compustat annual DLTT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dNco; independently, quintiles on dNco crossed with micro/small/big size terciles into 15 Me-dNco portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low increases in net noncurrent operating assets earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.17 |

[^ summary table](#summary)

<a id="dnoa"></a>

### Changes in Net Operating Assets - `dnoa`

The annual change in net operating assets (operating assets minus operating liabilities, as defined for Noa) scaled by lagged total assets; captures balance-sheet growth from accruals and investment that predicts lower returns.

**Construction**

```
dNoa = ΔNet Operating Assets / AT_{t-1}, i.e. the change from the fiscal year ending in t−2 to the fiscal year ending in t−1 in (AT − CHE) − (AT − DLC − DLTT − MIB − PSTK − CEQ), scaled by 1-year-lagged total assets.
```

| | |
|---|---|
| **Inputs** | `Compustat annual AT`, `Compustat annual CHE`, `Compustat annual DLC`, `Compustat annual DLTT`, `Compustat annual MIB`, `Compustat annual PSTK`, `Compustat annual CEQ` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dNoa for the fiscal year ending in t−1; independently, quintiles on dNoa crossed with micro/small/big size terciles into 15 Me-dNoa portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with smaller increases in net operating assets earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.5 |

[^ summary table](#summary)

<a id="dnca"></a>

### Changes in Non-current Operating Assets - `dnca`

The change in noncurrent operating assets alone (total assets less current assets and long-term investments), a component of the noncurrent-operating accrual.

**Construction**

```
dNca = ΔNca, where Nca = AT − ACT − IVAO (missing ΔIVAO set to 0). The change is for the fiscal year ending in t−1, scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual AT`, `Compustat annual ACT`, `Compustat annual IVAO` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dNca; independently, quintiles on dNca crossed with micro/small/big size terciles into 15 Me-dNca portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low increases in noncurrent operating assets earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.17 |

[^ summary table](#summary)

<a id="dpia"></a>

### Changes in PP&E and Inventory-to-Assets - `dpia`

Captures the combined annual growth in fixed capital (gross property, plant and equipment) and inventory, scaled by lagged total assets — a broad measure of the physical-capital investment rate.

**Construction**

```
dPia = [ΔPPEGT + ΔINVT] / AT_{t-2}, where the changes are for the fiscal year ending in calendar year t−1 (i.e., from t−2 to t−1), scaled by 1-year-lagged (t−2) total assets.
```

| | |
|---|---|
| **Inputs** | `Compustat annual PPEGT`, `Compustat annual INVT`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dPia for the fiscal year ending in t−1; independently, quintiles on dPia crossed with micro/small/big size terciles into 15 Me-dPia portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with smaller increases in fixed capital and inventory earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.4 |

[^ summary table](#summary)

<a id="cei"></a>

### Composite Equity Issuance - `cei`

Captures the portion of a firm's 5-year market-equity growth that is not explained by its own stock return, i.e., growth attributable to net share issuance — a broad measure of external equity financing that predicts lower subsequent returns.

**Construction**

```
Cei = ln(Me_t / Me_{t-5}) − r(t−5, t), where r(t−5,t) is the cumulative log stock return from July of year t−5 to June of year t, and Me_t is CRSP market equity on the last trading day of June in year t. Requires all 60 monthly returns non-missing and free of the CRSP 'GP' flag (which marks months whose compounded return omits a large gap in daily prices).
```

| | |
|---|---|
| **Inputs** | `CRSP market equity (Me)`, `CRSP monthly stock returns` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Cei; independently, quintiles on Cei crossed with micro/small/big size terciles into 15 Me-Cei portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low composite equity issuance earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.11 |

[^ summary table](#summary)

<a id="dac"></a>

### Discretionary Accruals - `dac`

The residual (abnormal) component of operating accruals after removing the portion explained by sales growth net of receivables growth and by PP&E, estimated via cross-sectional industry-year regressions — the modified-Jones-model measure of earnings management.

**Construction**

```
Oa_it/AT_{it-1} = α1(1/AT_{it-1}) + α2[(ΔSALE_it − ΔREC_it)/AT_{it-1}] + α3(PPE_it/AT_{it-1}) + e_it. Dac = e_it, the regression residual. Estimated separately for each 2-digit SIC industry-year, separately for NYSE/AMEX and NASDAQ firms (at least 6 firms per regression); variables winsorized at the 1st and 99th percentiles each year.
```

| | |
|---|---|
| **Inputs** | `Operating accruals (Oa)`, `Compustat annual AT`, `Compustat annual SALE`, `Compustat annual RECT`, `Compustat annual PPEGT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Dac for the fiscal year ending in t−1; independently, quintiles on Dac crossed with micro/small/big size terciles into 15 Me-Dac portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low discretionary accruals earn higher returns than firms with high (income-inflating) discretionary accruals |
| **Series starts** | January 1967 |
| **Credited paper** | Dechow, Sloan, and Sweeney (1995) |
| **Technical document** | section 2.3.19 |

[^ summary table](#summary)

<a id="ivc"></a>

### Inventory Changes - `ivc`

The annual change in inventory scaled by average total assets, isolating inventory investment in asset-scaled (rather than growth-rate) terms.

**Construction**

```
Ivc = ΔINVT / [(AT_{t-2} + AT_{t-1})/2], the change in inventory for the fiscal year ending in t−1 minus t−2, scaled by the average of total assets for the fiscal years ending in t−2 and t−1. Firms carrying no inventory for the past 2 fiscal years are excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat annual INVT`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Ivc; independently, quintiles on Ivc crossed with micro/small/big size terciles into 15 Me-Ivc portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with smaller inventory build-ups earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.13 |

[^ summary table](#summary)

<a id="ivg"></a>

### Inventory Growth - `ivg`

The one-year growth rate in inventory, a component-level investment measure; firms building inventory rapidly tend to earn lower subsequent returns.

**Construction**

```
Ivg = INVT_{t-1} / INVT_{t-2} − 1, the annual growth rate in inventory from the fiscal year ending in calendar year t−2 to the fiscal year ending in t−1.
```

| | |
|---|---|
| **Inputs** | `Compustat annual INVT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Ivg; independently, quintiles on Ivg crossed with micro/small/big size terciles into 15 Me-Ivg portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low inventory growth earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.12 |

[^ summary table](#summary)

<a id="ig"></a>

### Investment Growth - `ig`

The one-year growth rate in capital expenditure, capturing the pace of capex expansion; firms ramping up capex sharply tend to earn lower subsequent returns.

**Construction**

```
Ig = CAPX_{t-1} / CAPX_{t-2} − 1, the growth rate from the fiscal year ending in calendar year t−2 to the fiscal year ending in t−1.
```

| | |
|---|---|
| **Inputs** | `Compustat annual CAPX` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Ig; independently, quintiles on Ig crossed with micro/small/big size terciles into 15 Me-Ig portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low (or negative) capex growth earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.7 |

[^ summary table](#summary)

<a id="ia"></a>

### Investment-to-Assets - `ia`

Measures a firm's one-year growth rate in total assets, a standard proxy for the corporate investment rate; per q-theory, firms that invest (grow assets) more aggressively earn lower subsequent returns.

**Construction**

```
I/A = AT_{t-1} / AT_{t-2} − 1, where AT is total assets for the fiscal years ending in calendar years t−1 and t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on I/A; independently, quintiles on I/A crossed with micro/small/big size terciles (NYSE 20th/50th Me percentiles) into 15 Me-I/A portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - low-asset-growth firms earn higher returns than high-investment firms |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.2 |

[^ summary table](#summary)

<a id="ndf"></a>

### Net Debt Financing - `ndf`

The net cash raised from long-term and current debt issuance less repayments, the debt-financing component of net external financing.

**Construction**

```
Ndf = DLTIS − DLTR + DLCCH (DLCCH zero if missing), measured for the fiscal year ending in t−1, scaled by the average of total assets (AT) for the fiscal years ending in t−2 and t−1.
```

| | |
|---|---|
| **Inputs** | `Compustat annual DLTIS`, `Compustat annual DLTR`, `Compustat annual DLCCH`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Ndf; independently, quintiles on Ndf crossed with micro/small/big size terciles into 15 Me-Ndf portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low net debt financing earn higher returns |
| **Series starts** | July 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.23 |

[^ summary table](#summary)

<a id="nxf"></a>

### Net External Financing - `nxf`

The sum of net equity financing and net debt financing raised over the year, a comprehensive measure of external capital raised; firms relying heavily on external financing tend to earn lower subsequent returns.

**Construction**

```
Nxf = Nef + Ndf. Nef = SSTK − PRSTKC − DV. Ndf = DLTIS − DLTR + DLCCH (DLCCH zero if missing). Measured for the fiscal year ending in t−1, scaled by the average of total assets (AT) for the fiscal years ending in t−2 and t−1.
```

| | |
|---|---|
| **Inputs** | `Compustat annual SSTK`, `Compustat annual PRSTKC`, `Compustat annual DV`, `Compustat annual DLTIS`, `Compustat annual DLTR`, `Compustat annual DLCCH`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Nxf; independently, quintiles on Nxf crossed with micro/small/big size terciles into 15 Me-Nxf portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low net external financing earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.23 |

[^ summary table](#summary)

<a id="noa"></a>

### Net Operating Assets - `noa`

Net operating assets is operating assets minus operating liabilities, scaled by lagged total assets; a high level reflects balance-sheet expansion driven by accruals and investment, which is associated with lower subsequent returns.

**Construction**

```
Noa = (Operating Assets − Operating Liabilities) / AT_{t-1}. Operating Assets = AT − CHE. Operating Liabilities = AT − DLC − DLTT − MIB − PSTK − CEQ (each zero if missing). Measured for the fiscal year ending in calendar year t−1, scaled by 1-year-lagged total assets.
```

| | |
|---|---|
| **Inputs** | `Compustat annual AT`, `Compustat annual CHE`, `Compustat annual DLC`, `Compustat annual DLTT`, `Compustat annual MIB`, `Compustat annual PSTK`, `Compustat annual CEQ` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Noa for the fiscal year ending in t−1; independently, quintiles on Noa crossed with micro/small/big size terciles into 15 Me-Noa portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low net operating assets earn higher returns than firms with bloated balance sheets |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.5 |

[^ summary table](#summary)

<a id="nsi"></a>

### Net Stock Issues - `nsi`

Measures net share issuance over the prior year via the log change in split-adjusted shares outstanding; firms issuing (diluting) shares tend to underperform, while firms repurchasing shares tend to outperform.

**Construction**

```
Nsi = ln(split-adjusted shares_{t-1} / split-adjusted shares_{t-2}), where split-adjusted shares outstanding = CSHO × AJEX, for the fiscal years ending in calendar years t−1 and t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual CSHO`, `Compustat annual AJEX` |
| **Portfolio sort** | Deciles formed at June-end of year t: negative Nsi split into 2 portfolios (1-2), zero Nsi into 1 portfolio (3), positive Nsi split into 7 portfolios (4-10); quintiles formed analogously (negative→1, zero→2, positive→3-5) crossed independently with micro/small/big size terciles into 15 Me-Nsi portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with negative net issuance (repurchasers) earn higher returns than share issuers |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.9 |

[^ summary table](#summary)

<a id="oa"></a>

### Operating Accruals - `oa`

Operating accruals capture the non-cash component of earnings (via a working-capital balance-sheet approach pre-1988, and directly from the cash-flow statement from 1988), used to detect low earnings quality / earnings management that predicts lower future returns (the accrual anomaly).

**Construction**

```
Pre-1988 (Sloan 1996): Oa = (ΔCA − ΔCASH) − (ΔCL − ΔSTD − ΔTP) − DP, where ΔCA = Δ ACT, ΔCASH = Δ CHE, ΔCL = Δ LCT, ΔSTD = Δ DLC, ΔTP = Δ TXP (missing ΔTP set to 0), DP = depreciation and amortization. From 1988 (Hribar and Collins 2002): Oa = NI − OANCF. Sorted on Oa for the fiscal year ending in t−1 scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual ACT`, `Compustat annual CHE`, `Compustat annual LCT`, `Compustat annual DLC`, `Compustat annual TXP`, `Compustat annual DP`, `Compustat annual NI`, `Compustat annual OANCF`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Oa (FY ending t−1) scaled by AT (FY ending t−2); independently, quintiles on the same measure crossed with micro/small/big size terciles into 15 Me-Oa portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low (or negative) operating accruals earn higher returns than high-accrual firms |
| **Series starts** | January 1967 |
| **Credited paper** | Sloan (1996) (pre-1988 balance-sheet method); Hribar and Collins (2002) (post-1988 cash-flow method) |
| **Technical document** | section 2.3.14 |

[^ summary table](#summary)

<a id="pda"></a>

### Percent Discretionary Accruals - `pda`

Discretionary accruals rescaled from a total-assets basis to an earnings basis, by multiplying Dac by lagged total assets and dividing by the absolute value of net income — the percent-accruals analogue of Dac.

**Construction**

```
Pda = Dac_{t-1} × AT_{t-2} / |NI_{t-1}|. See Dac (section 2.3.19) for the measurement of discretionary accruals.
```

| | |
|---|---|
| **Inputs** | `Discretionary accruals (Dac)`, `Compustat annual AT`, `Compustat annual NI` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Pda for the fiscal year ending in t−1; independently, quintiles on Pda crossed with micro/small/big size terciles into 15 Me-Pda portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low percent discretionary accruals earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Dechow, Sloan, and Sweeney (1995) (Dac); percent-scaling per Hafzalla, Lundholm, and Van Winkle (2011) |
| **Technical document** | section 2.3.22 |

[^ summary table](#summary)

<a id="poa"></a>

### Percent Operating Accruals - `poa`

Operating accruals scaled by the absolute value of net income rather than total assets; percent-scaling better isolates firms for which sophisticated and naive earnings forecasts diverge most.

**Construction**

```
Poa = Oa (fiscal year ending t−1) / |NI| (fiscal year ending t−1). See Oa (section 2.3.14) for the measurement of operating accruals.
```

| | |
|---|---|
| **Inputs** | `Operating accruals (Oa)`, `Compustat annual NI` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Poa for the fiscal year ending in t−1; independently, quintiles on Poa crossed with micro/small/big size terciles into 15 Me-Poa portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low percent operating accruals earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Hafzalla, Lundholm, and Van Winkle (2011) |
| **Technical document** | section 2.3.20 |

[^ summary table](#summary)

<a id="pta"></a>

### Percent Total Accruals - `pta`

Total accruals scaled by the absolute value of net income, the percent-accruals analogue of Ta, applying the same earnings-basis scaling idea used for Poa.

**Construction**

```
Pta = Ta (fiscal year ending t−1) / |NI| (fiscal year ending t−1). See Ta (section 2.3.15) for the measurement of total accruals.
```

| | |
|---|---|
| **Inputs** | `Total accruals (Ta)`, `Compustat annual NI` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Pta for the fiscal year ending in t−1; independently, quintiles on Pta crossed with micro/small/big size terciles into 15 Me-Pta portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low percent total accruals earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Hafzalla, Lundholm, and Van Winkle (2011) |
| **Technical document** | section 2.3.21 |

[^ summary table](#summary)

<a id="dii"></a>

### Percentage Change in Investment Relative to Industry - `dii`

Compares a firm's percentage change in capital investment (relative to its own 2-year average) against the same percentage change aggregated across its 2-digit SIC industry, isolating investment moves that are idiosyncratic rather than industry-wide.

**Construction**

```
dIi = %Δ(Investment) − %Δ(Industry investment), where %Δ(X_t) = [X_t − E[X_t]] / E[X_t] and E[X_t] = [X_{t-1} + X_{t-2}]/2. Investment = capital expenditure in PP&E (CAPXV). Industry investment aggregates CAPXV across all firms sharing the 2-digit SIC code. Firms with nonpositive E[Investment(t)] are excluded; each industry requires at least 2 firms.
```

| | |
|---|---|
| **Inputs** | `Compustat annual CAPXV`, `2-digit SIC industry code` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on dIi for the fiscal year ending in t−1; independently, quintiles on dIi crossed with micro/small/big size terciles into 15 Me-dIi portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms investing less than their industry peers earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Abarbanell and Bushee (1998) |
| **Technical document** | section 2.3.10 |

[^ summary table](#summary)

<a id="iaq-12"></a>

### Quarterly Investment-to-Assets (12m) - `iaq_12`

A quarterly, higher-frequency analogue of I/A measuring the growth in total assets over the trailing four fiscal quarters; sorted monthly, it captures short-horizon investment-driven mispricing.

**Construction**

```
Iaq = ATQ_t / ATQ_{t-4} − 1, quarterly total assets divided by 4-quarter-lagged quarterly total assets, using the latest fiscal quarter ending at least four months before month t. The 12-month decile return averages twelve overlapping subdecile returns, each initiated in a different one of the prior twelve months.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly ATQ` |
| **Portfolio sort** | NYSE deciles formed at the beginning of each month t on Iaq (latest quarter ending ≥4 months prior); independently, quintiles on Iaq crossed with micro/small/big size terciles into 15 Me-Iaq portfolios; overlapping subdecile portfolios averaged for the 12-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | Low - low quarterly-asset-growth firms earn higher returns |
| **Series starts** | January 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.3 |

[^ summary table](#summary)

<a id="iaq-1"></a>

### Quarterly Investment-to-Assets (1m) - `iaq_1`

A quarterly, higher-frequency analogue of I/A measuring the growth in total assets over the trailing four fiscal quarters; sorted monthly, it captures short-horizon investment-driven mispricing.

**Construction**

```
Iaq = ATQ_t / ATQ_{t-4} − 1, quarterly total assets divided by 4-quarter-lagged quarterly total assets, using the latest fiscal quarter ending at least four months before month t.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly ATQ` |
| **Portfolio sort** | NYSE deciles formed at the beginning of each month t on Iaq (latest quarter ending ≥4 months prior); independently, quintiles on Iaq crossed with micro/small/big size terciles into 15 Me-Iaq portfolios |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - low quarterly-asset-growth firms earn higher returns |
| **Series starts** | January 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.3 |

[^ summary table](#summary)

<a id="iaq-6"></a>

### Quarterly Investment-to-Assets (6m) - `iaq_6`

A quarterly, higher-frequency analogue of I/A measuring the growth in total assets over the trailing four fiscal quarters; sorted monthly, it captures short-horizon investment-driven mispricing.

**Construction**

```
Iaq = ATQ_t / ATQ_{t-4} − 1, quarterly total assets divided by 4-quarter-lagged quarterly total assets, using the latest fiscal quarter ending at least four months before month t. The 6-month decile return averages six overlapping subdecile returns, each initiated in a different one of the prior six months.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly ATQ` |
| **Portfolio sort** | NYSE deciles formed at the beginning of each month t on Iaq (latest quarter ending ≥4 months prior); independently, quintiles on Iaq crossed with micro/small/big size terciles into 15 Me-Iaq portfolios; overlapping subdecile portfolios averaged for the 6-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | Low - low quarterly-asset-growth firms earn higher returns |
| **Series starts** | January 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.3.3 |

[^ summary table](#summary)

<a id="ta"></a>

### Total Accruals - `ta`

Total accruals extend operating accruals by decomposing the balance sheet into working-capital, noncurrent-operating, and net-financial-asset components (Richardson, Sloan, Soliman, and Tuna 2005); from 1988 measured directly from cash-flow-statement financing and investing flows.

**Construction**

```
Pre-1988: Ta = dWc + dNco + dFin (see dWc, dNco, dFin definitions). From 1988: Ta = NI − (OANCF + IVNCF + FINCF) + SSTK − PRSTKC − DV (SSTK, PRSTKC, DV zero if missing). Sorted on Ta for the fiscal year ending in t−1 scaled by total assets (AT) for the fiscal year ending in t−2.
```

| | |
|---|---|
| **Inputs** | `Compustat annual NI`, `Compustat annual OANCF`, `Compustat annual IVNCF`, `Compustat annual FINCF`, `Compustat annual SSTK`, `Compustat annual PRSTKC`, `Compustat annual DV`, `Compustat annual AT` |
| **Portfolio sort** | NYSE deciles at June-end of year t based on Ta (FY ending t−1) scaled by AT (FY ending t−2); independently, quintiles on the same measure crossed with micro/small/big size terciles into 15 Me-Ta portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - firms with low total accruals earn higher returns than high-accrual firms |
| **Series starts** | January 1967 |
| **Credited paper** | Richardson, Sloan, Soliman, and Tuna (2005) |
| **Technical document** | section 2.3.15 |

[^ summary table](#summary)
