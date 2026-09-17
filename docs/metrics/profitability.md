# Profitability

Signals built from the level, the change and the forecast of profitability. The shared idea, again from q-theory, is that for a given amount of investment, more profitable firms must be discounted at a higher rate.

50 anomalies. Definitions from Kewei Hou, Chen Xue, and Lu Zhang, "Technical Document: Testing Portfolios," global-q.org, July 2026.

[<- back to the metric index](../METRICS.md)

## Summary

| Code | Metric | What it measures | Which end wins | Rebalance | Holding | Starts |
|---|---|---|---|---|---|---|
| `ato` | [Asset Turnover](#ato) | Asset turnover measures how efficiently a firm generates sales from its net operating assets. Higher turnover indicates more efficient use of operating assets and is hypothesized to predict higher future returns. | High | annual (June) | 12 months | January 1967 |
| `cto` | [Capital Turnover](#cto) | Capital turnover measures sales generated per dollar of total assets, indicating capital-use efficiency. More efficient firms are hypothesized to earn higher returns. | High | annual (June) | 12 months | January 1967 |
| `cop` | [Cash-Based Operating Profitability](#cop) | Cash-based operating profitability, following Ball, Gerakos, Linnainmaa, and Nikolaev (2016), adjusts operating profit for changes in working-capital accruals to approximate a cash-flow-based measure of profitability, scaled by current total assets. More cash-profitable firms are hypothesized to earn higher returns. | High | annual (June) | 12 months | January 1967 |
| `cla` | [Cash-Based Operating Profits-to-Lagged Assets](#cla) | Cash-based operating profits-to-lagged assets adjusts operating profit for working-capital accrual changes to approximate cash-flow profitability, scaled by lagged total assets. More cash-profitable firms are hypothesized to earn higher returns. | High | annual (June) | 12 months | January 1967 |
| `droa_1` | [Change in Return on Assets (1m)](#droa-1) | Change in return on assets is the 4-quarter change in Roa, capturing recent improvement or deterioration in asset profitability. | High | monthly | 1 month | January 1973 |
| `droa_6` | [Change in Return on Assets (6m)](#droa-6) | Change in return on assets is the 4-quarter change in Roa, capturing recent improvement or deterioration in asset profitability. | High | monthly | 6 months | January 1973 |
| `droe_12` | [Change in Return on Equity (12m)](#droe-12) | Change in return on equity is the 4-quarter change in Roe, capturing recent improvement or deterioration in profitability as an earnings-momentum-like signal. | High | monthly | 12 months | January 1967 |
| `droe_1` | [Change in Return on Equity (1m)](#droe-1) | Change in return on equity is the 4-quarter change in Roe, capturing recent improvement or deterioration in profitability as an earnings-momentum-like signal. | High | monthly | 1 month | January 1967 |
| `droe_6` | [Change in Return on Equity (6m)](#droe-6) | Change in return on equity is the 4-quarter change in Roe, capturing recent improvement or deterioration in profitability as an earnings-momentum-like signal. | High | monthly | 6 months | January 1967 |
| `eg_12` | [Expected Growth (12m)](#eg-12) | Expected growth, following Hou, Mo, Xue, and Zhang (2021), is the fitted value from monthly cross-sectional regressions forecasting one-year-ahead investment-to-assets change using Tobin's q, cash-based operating profitability, and the change in return on equity. Firms expected to grow investment more are hypothesized to earn higher returns, consistent with q-theory. | High | monthly | 12 months | January 1967 |
| `eg_1` | [Expected Growth (1m)](#eg-1) | Expected growth, following Hou, Mo, Xue, and Zhang (2021), is the fitted value from monthly cross-sectional regressions forecasting one-year-ahead investment-to-assets change using Tobin's q, cash-based operating profitability, and the change in return on equity. Firms expected to grow investment more are hypothesized to earn higher returns, consistent with q-theory. | High | monthly | 1 month | January 1967 |
| `eg_6` | [Expected Growth (6m)](#eg-6) | Expected growth, following Hou, Mo, Xue, and Zhang (2021), is the fitted value from monthly cross-sectional regressions forecasting one-year-ahead investment-to-assets change using Tobin's q, cash-based operating profitability, and the change in return on equity. Firms expected to grow investment more are hypothesized to earn higher returns, consistent with q-theory. | High | monthly | 6 months | January 1967 |
| `fp_6` | [Failure Probability (6m)](#fp-6) | Failure probability, from Campbell, Hilscher, and Szilagyi (2008), is a monthly distress-risk score combining profitability, leverage, past excess returns, volatility, size, liquidity, valuation, and price. It estimates a firm's likelihood of financial distress or bankruptcy. In the document this measure is labeled Fp and the resulting decile portfolio is Fpm6. | Low | monthly | 6 months | January 1976 |
| `gpa` | [Gross Profits-to-Assets](#gpa) | Gross profits-to-assets measures gross profitability scaled by current total assets, capturing profitability before accounting distortions further down the income statement. Higher gross profitability is hypothesized to predict higher returns. | High | annual (June) | 12 months | January 1967 |
| `gla` | [Gross Profits-to-Lagged Assets](#gla) | Gross profits-to-lagged assets is gross profitability scaled by lagged total assets rather than current assets, addressing the mechanical link between current profit and current asset growth. Higher gross profitability is hypothesized to predict higher returns. | High | annual (June) | 12 months | January 1967 |
| `opa` | [Operating Profits-to-Assets](#opa) | Operating profits-to-assets, following Ball, Gerakos, Linnainmaa, and Nikolaev (2015), measures operating profitability with R&D added back as an operating expense, scaled by current total assets. More profitable firms are hypothesized to earn higher returns. | High | annual (June) | 12 months | January 1967 |
| `ope` | [Operating Profits-to-Equity](#ope) | Operating profits-to-equity, following Fama and French (2015), measures operating profitability scaled by book equity — the profitability leg of the Fama-French five-factor model. More profitable firms are hypothesized to earn higher returns. | High | annual (June) | 12 months | January 1967 |
| `atoq_12` | [Quarterly Asset Turnover (12m)](#atoq-12) | Quarterly asset turnover measures sales generated per dollar of net operating assets at quarterly frequency. Higher turnover indicates more efficient use of operating assets and is hypothesized to predict higher future returns. | High | monthly | 12 months | January 1972 |
| `atoq_1` | [Quarterly Asset Turnover (1m)](#atoq-1) | Quarterly asset turnover measures sales generated per dollar of net operating assets at quarterly frequency. Higher turnover indicates more efficient use of operating assets and is hypothesized to predict higher future returns. | High | monthly | 1 month | January 1972 |
| `atoq_6` | [Quarterly Asset Turnover (6m)](#atoq-6) | Quarterly asset turnover measures sales generated per dollar of net operating assets at quarterly frequency. Higher turnover indicates more efficient use of operating assets and is hypothesized to predict higher future returns. | High | monthly | 6 months | January 1972 |
| `ctoq_12` | [Quarterly Capital Turnover (12m)](#ctoq-12) | Quarterly capital turnover measures sales generated per dollar of total assets at quarterly frequency, an efficiency signal hypothesized to predict higher returns. | High | monthly | 12 months | January 1972 |
| `ctoq_1` | [Quarterly Capital Turnover (1m)](#ctoq-1) | Quarterly capital turnover measures sales generated per dollar of total assets at quarterly frequency, an efficiency signal hypothesized to predict higher returns. | High | monthly | 1 month | January 1972 |
| `ctoq_6` | [Quarterly Capital Turnover (6m)](#ctoq-6) | Quarterly capital turnover measures sales generated per dollar of total assets at quarterly frequency, an efficiency signal hypothesized to predict higher returns. | High | monthly | 6 months | January 1972 |
| `claq_12` | [Quarterly Cash-Based Operating Profits-to-Lagged Assets (12m)](#claq-12) | Quarterly cash-based operating profits-to-lagged assets is the quarterly version of Cla, scaling quarterly cash-adjusted operating profit by lagged total assets. More cash-profitable firms are hypothesized to earn higher returns. | High | monthly | 12 months | January 1976 |
| `claq_1` | [Quarterly Cash-Based Operating Profits-to-Lagged Assets (1m)](#claq-1) | Quarterly cash-based operating profits-to-lagged assets is the quarterly version of Cla, scaling quarterly cash-adjusted operating profit by lagged total assets. More cash-profitable firms are hypothesized to earn higher returns. | High | monthly | 1 month | January 1976 |
| `claq_6` | [Quarterly Cash-Based Operating Profits-to-Lagged Assets (6m)](#claq-6) | Quarterly cash-based operating profits-to-lagged assets is the quarterly version of Cla, scaling quarterly cash-adjusted operating profit by lagged total assets. More cash-profitable firms are hypothesized to earn higher returns. | High | monthly | 6 months | January 1976 |
| `fq_12` | [Quarterly F-Score (12m)](#fq-12) | The quarterly F-score is a quarterly-frequency adaptation of Piotroski's (2000) nine-signal fundamental score, combining profitability, capital-structure/liquidity, and operating-efficiency signals into one composite. Financially healthier firms (higher score) are hypothesized to earn higher returns. | High | monthly | 12 months | January 1985 |
| `fq_1` | [Quarterly F-Score (1m)](#fq-1) | The quarterly F-score is a quarterly-frequency adaptation of Piotroski's (2000) nine-signal fundamental score, combining profitability, capital-structure/liquidity, and operating-efficiency signals into one composite. Financially healthier firms (higher score) are hypothesized to earn higher returns. | High | monthly | 1 month | January 1985 |
| `fq_6` | [Quarterly F-Score (6m)](#fq-6) | The quarterly F-score is a quarterly-frequency adaptation of Piotroski's (2000) nine-signal fundamental score, combining profitability, capital-structure/liquidity, and operating-efficiency signals into one composite. Financially healthier firms (higher score) are hypothesized to earn higher returns. | High | monthly | 6 months | January 1985 |
| `glaq_12` | [Quarterly Gross Profits-to-Lagged Assets (12m)](#glaq-12) | Quarterly gross profits-to-lagged assets is the quarterly version of Gla, scaling quarterly gross profit by 1-quarter-lagged total assets. Higher gross profitability is hypothesized to predict higher returns. | High | monthly | 12 months | January 1976 |
| `glaq_1` | [Quarterly Gross Profits-to-Lagged Assets (1m)](#glaq-1) | Quarterly gross profits-to-lagged assets is the quarterly version of Gla, scaling quarterly gross profit by 1-quarter-lagged total assets. Higher gross profitability is hypothesized to predict higher returns. | High | monthly | 1 month | January 1976 |
| `glaq_6` | [Quarterly Gross Profits-to-Lagged Assets (6m)](#glaq-6) | Quarterly gross profits-to-lagged assets is the quarterly version of Gla, scaling quarterly gross profit by 1-quarter-lagged total assets. Higher gross profitability is hypothesized to predict higher returns. | High | monthly | 6 months | January 1976 |
| `oq_1` | [Quarterly O-Score (1m)](#oq-1) | The quarterly O-score is an accounting-based bankruptcy-risk score combining firm size, leverage, liquidity, profitability, and earnings-trend variables, estimating the probability of financial distress. | Low | monthly | 1 month | January 1976 |
| `olaq_12` | [Quarterly Operating Profits-to-Lagged Assets (12m)](#olaq-12) | Quarterly operating profits-to-lagged assets is the quarterly version of Opa, scaling quarterly operating profit (with R&D added back) by 1-quarter-lagged total assets. More profitable firms are hypothesized to earn higher returns. | High | monthly | 12 months | January 1976 |
| `olaq_1` | [Quarterly Operating Profits-to-Lagged Assets (1m)](#olaq-1) | Quarterly operating profits-to-lagged assets is the quarterly version of Opa, scaling quarterly operating profit (with R&D added back) by 1-quarter-lagged total assets. More profitable firms are hypothesized to earn higher returns. | High | monthly | 1 month | January 1976 |
| `olaq_6` | [Quarterly Operating Profits-to-Lagged Assets (6m)](#olaq-6) | Quarterly operating profits-to-lagged assets is the quarterly version of Opa, scaling quarterly operating profit (with R&D added back) by 1-quarter-lagged total assets. More profitable firms are hypothesized to earn higher returns. | High | monthly | 6 months | January 1976 |
| `oleq_12` | [Quarterly Operating Profits-to-Lagged Equity (12m)](#oleq-12) | Quarterly operating profits-to-lagged equity is the quarterly version of Ope, scaling quarterly operating profit by 1-quarter-lagged book equity. More profitable firms are hypothesized to earn higher returns. | High | monthly | 12 months | January 1972 |
| `oleq_1` | [Quarterly Operating Profits-to-Lagged Equity (1m)](#oleq-1) | Quarterly operating profits-to-lagged equity is the quarterly version of Ope, scaling quarterly operating profit by 1-quarter-lagged book equity. More profitable firms are hypothesized to earn higher returns. | High | monthly | 1 month | January 1972 |
| `oleq_6` | [Quarterly Operating Profits-to-Lagged Equity (6m)](#oleq-6) | Quarterly operating profits-to-lagged equity is the quarterly version of Ope, scaling quarterly operating profit by 1-quarter-lagged book equity. More profitable firms are hypothesized to earn higher returns. | High | monthly | 6 months | January 1972 |
| `pmq_1` | [Quarterly Profit Margin (1m)](#pmq-1) | Quarterly profit margin measures operating income earned per dollar of sales, a margin-based profitability signal hypothesized to predict higher returns. | High | monthly | 1 month | January 1967 |
| `rnaq_12` | [Quarterly Return on Net Operating Assets (12m)](#rnaq-12) | Quarterly return on net operating assets measures operating profitability relative to the net operating assets used to generate it. Firms earning higher returns on their operating asset base are hypothesized to earn higher stock returns. | High | monthly | 12 months | January 1976 |
| `rnaq_1` | [Quarterly Return on Net Operating Assets (1m)](#rnaq-1) | Quarterly return on net operating assets measures operating profitability relative to the net operating assets used to generate it. Firms earning higher returns on their operating asset base are hypothesized to earn higher stock returns. | High | monthly | 1 month | January 1976 |
| `rnaq_6` | [Quarterly Return on Net Operating Assets (6m)](#rnaq-6) | Quarterly return on net operating assets measures operating profitability relative to the net operating assets used to generate it. Firms earning higher returns on their operating asset base are hypothesized to earn higher stock returns. | High | monthly | 6 months | January 1976 |
| `sgq_1` | [Quarterly Sales Growth (1m)](#sgq-1) | Quarterly sales growth measures the year-over-year growth rate in quarterly sales, a growth/glamour signal rather than a pure profitability level. | Low | monthly | 1 month | January 1967 |
| `tbiq_12` | [Quarterly Taxable Income-to-Book Income (12m)](#tbiq-12) | Quarterly taxable income-to-book income measures the ratio of pretax income to net (book) income, an earnings-quality/conservatism signal. | High | monthly | 12 months | January 1967 |
| `tbiq_6` | [Quarterly Taxable Income-to-Book Income (6m)](#tbiq-6) | Quarterly taxable income-to-book income measures the ratio of pretax income to net (book) income, an earnings-quality/conservatism signal. | High | monthly | 6 months | January 1967 |
| `roa_1` | [Return on Assets (1m)](#roa-1) | Return on assets measures profitability per dollar of total assets, a quality signal independent of capital structure. More profitable firms are hypothesized to earn higher returns. | High | monthly | 1 month | January 1972 |
| `roa_6` | [Return on Assets (6m)](#roa-6) | Return on assets measures profitability per dollar of total assets, a quality signal independent of capital structure. More profitable firms are hypothesized to earn higher returns. | High | monthly | 6 months | January 1972 |
| `roe_1` | [Return on Equity (1m)](#roe-1) | Return on equity measures a firm's profitability relative to its shareholders' equity. Firms earning more per unit of book equity are considered higher quality and are hypothesized to earn higher future stock returns. | High | monthly | 1 month | January 1967 |
| `roe_6` | [Return on Equity (6m)](#roe-6) | Return on equity measures a firm's profitability relative to its shareholders' equity. Firms earning more per unit of book equity are considered higher quality and are hypothesized to earn higher future stock returns. | High | monthly | 6 months | January 1967 |

## Detail

<a id="ato"></a>

### Asset Turnover - `ato`

Asset turnover measures how efficiently a firm generates sales from its net operating assets. Higher turnover indicates more efficient use of operating assets and is hypothesized to predict higher future returns.

**Construction**

```
Ato = sales (Compustat annual item SALE, fiscal year ending in t-1) / net operating assets (Noa, fiscal year ending in t-2). Noa = operating assets minus operating liabilities. Operating assets = total assets (AT) - cash and short-term investments (CHE) - other investments and advances (IVAO, zero if missing). Operating liabilities = total assets - debt in current liabilities (DLC, zero if missing) - long-term debt (DLTT, zero if missing) - minority interest (MIB, zero if missing) - preferred stock (PSTK, zero if missing) - common equity (CEQ). Firms with nonpositive Noa in year t-2 are excluded.
```

| | |
|---|---|
| **Inputs** | `SALE`, `AT`, `CHE`, `IVAO`, `DLC`, `DLTT`, `MIB`, `PSTK`, `CEQ` |
| **Portfolio sort** | NYSE deciles at the end of June of year t on Ato; also independent quintile x size (micro/small/big, NYSE 20th/50th Me percentiles) intersections forming 15 Me-Ato portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - more efficient use of operating assets predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.5 |

[^ summary table](#summary)

<a id="cto"></a>

### Capital Turnover - `cto`

Capital turnover measures sales generated per dollar of total assets, indicating capital-use efficiency. More efficient firms are hypothesized to earn higher returns.

**Construction**

```
Cto = sales (Compustat annual item SALE, fiscal year ending in t-1) / total assets (AT, fiscal year ending in t-2).
```

| | |
|---|---|
| **Inputs** | `SALE`, `AT` |
| **Portfolio sort** | NYSE deciles at end of June of year t on Cto; also Me-Cto 15-portfolio intersections |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - more efficient use of capital predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.6 |

[^ summary table](#summary)

<a id="cop"></a>

### Cash-Based Operating Profitability - `cop`

Cash-based operating profitability, following Ball, Gerakos, Linnainmaa, and Nikolaev (2016), adjusts operating profit for changes in working-capital accruals to approximate a cash-flow-based measure of profitability, scaled by current total assets. More cash-profitable firms are hypothesized to earn higher returns.

**Construction**

```
Cop = [total revenue (REVT) - COGS - XSGA + R&D (XRD, zero if missing) - change in accounts receivable (RECT) - change in inventory (INVT) - change in prepaid expenses (XPP) + change in deferred revenue (DRC + DRLT) + change in trade accounts payable (AP) + change in accrued expenses (XACC)] / total assets (AT, current, not lagged). All changes are annual; missing changes set to zero.
```

| | |
|---|---|
| **Inputs** | `REVT`, `COGS`, `XSGA`, `XRD`, `RECT`, `INVT`, `XPP`, `DRC`, `DRLT`, `AP`, `XACC`, `AT` |
| **Portfolio sort** | NYSE deciles at end of June of year t on Cop (fiscal year ending in t-1); also Me-Cop 15-portfolio intersections |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - higher cash-based operating profitability predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Ball, Gerakos, Linnainmaa, and Nikolaev (2016) |
| **Technical document** | section 2.4.16 |

[^ summary table](#summary)

<a id="cla"></a>

### Cash-Based Operating Profits-to-Lagged Assets - `cla`

Cash-based operating profits-to-lagged assets adjusts operating profit for working-capital accrual changes to approximate cash-flow profitability, scaled by lagged total assets. More cash-profitable firms are hypothesized to earn higher returns.

**Construction**

```
Cla = [total revenue (REVT) - cost of goods sold (COGS) - SG&A (XSGA) + R&D (XRD, zero if missing) - change in accounts receivable (RECT) - change in inventory (INVT) - change in prepaid expenses (XPP) + change in deferred revenue (DRC + DRLT) + change in trade accounts payable (AP) + change in accrued expenses (XACC)] / 1-year-lagged total assets (AT). All changes are annual; missing changes set to zero.
```

| | |
|---|---|
| **Inputs** | `REVT`, `COGS`, `XSGA`, `XRD`, `RECT`, `INVT`, `XPP`, `DRC`, `DRLT`, `AP`, `XACC`, `AT` |
| **Portfolio sort** | NYSE deciles at end of June of year t on Cla (fiscal year ending in t-1); also Me-Cla 15-portfolio intersections |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - higher cash-based operating profitability predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.17 |

[^ summary table](#summary)

<a id="droa-1"></a>

### Change in Return on Assets (1m) - `droa_1`

Change in return on assets is the 4-quarter change in Roa, capturing recent improvement or deterioration in asset profitability.

**Construction**

```
dRoa = Roa(current quarter) - Roa(4 quarters ago), where Roa = income before extraordinary items (IBQ) / 1-quarter-lagged total assets (ATQ), computed from the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `ATQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on dRoa (fiscal quarter ending within 6 months prior), monthly rebalance; also Me-dRoa 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - improving asset profitability predicts higher returns |
| **Series starts** | January 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.4 |

[^ summary table](#summary)

<a id="droa-6"></a>

### Change in Return on Assets (6m) - `droa_6`

Change in return on assets is the 4-quarter change in Roa, capturing recent improvement or deterioration in asset profitability.

**Construction**

```
dRoa = Roa(current quarter) - Roa(4 quarters ago), where Roa = income before extraordinary items (IBQ) / 1-quarter-lagged total assets (ATQ), computed from the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `ATQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on dRoa (fiscal quarter ending within 6 months prior), monthly rebalance; also Me-dRoa 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - improving asset profitability predicts higher returns |
| **Series starts** | January 1973 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.4 |

[^ summary table](#summary)

<a id="droe-12"></a>

### Change in Return on Equity (12m) - `droe_12`

Change in return on equity is the 4-quarter change in Roe, capturing recent improvement or deterioration in profitability as an earnings-momentum-like signal.

**Construction**

```
dRoe = Roe(current quarter) - Roe(4 quarters ago), where Roe = income before extraordinary items (IBQ) / 1-quarter-lagged book equity (see Roe, section 2.4.1), computed from the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `SEQQ/CEQQ/ATQ/LTQ`, `TXDITCQ`, `PSTKQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on dRoe (fiscal quarter ending within 6 months prior), monthly rebalance; also Me-dRoe 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - improving profitability predicts higher future returns |
| **Series starts** | January 1967 |
| **Credited paper** | Hou, Xue, and Zhang (2015) |
| **Technical document** | section 2.4.2 |

[^ summary table](#summary)

<a id="droe-1"></a>

### Change in Return on Equity (1m) - `droe_1`

Change in return on equity is the 4-quarter change in Roe, capturing recent improvement or deterioration in profitability as an earnings-momentum-like signal.

**Construction**

```
dRoe = Roe(current quarter) - Roe(4 quarters ago), where Roe = income before extraordinary items (IBQ) / 1-quarter-lagged book equity (see Roe, section 2.4.1), computed from the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `SEQQ/CEQQ/ATQ/LTQ`, `TXDITCQ`, `PSTKQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on dRoe (fiscal quarter ending within 6 months prior), monthly rebalance; also Me-dRoe 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - improving profitability predicts higher future returns |
| **Series starts** | January 1967 |
| **Credited paper** | Hou, Xue, and Zhang (2015) |
| **Technical document** | section 2.4.2 |

[^ summary table](#summary)

<a id="droe-6"></a>

### Change in Return on Equity (6m) - `droe_6`

Change in return on equity is the 4-quarter change in Roe, capturing recent improvement or deterioration in profitability as an earnings-momentum-like signal.

**Construction**

```
dRoe = Roe(current quarter) - Roe(4 quarters ago), where Roe = income before extraordinary items (IBQ) / 1-quarter-lagged book equity (see Roe, section 2.4.1), computed from the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `SEQQ/CEQQ/ATQ/LTQ`, `TXDITCQ`, `PSTKQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on dRoe (fiscal quarter ending within 6 months prior), monthly rebalance; also Me-dRoe 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - improving profitability predicts higher future returns |
| **Series starts** | January 1967 |
| **Credited paper** | Hou, Xue, and Zhang (2015) |
| **Technical document** | section 2.4.2 |

[^ summary table](#summary)

<a id="eg-12"></a>

### Expected Growth (12m) - `eg_12`

Expected growth, following Hou, Mo, Xue, and Zhang (2021), is the fitted value from monthly cross-sectional regressions forecasting one-year-ahead investment-to-assets change using Tobin's q, cash-based operating profitability, and the change in return on equity. Firms expected to grow investment more are hypothesized to earn higher returns, consistent with q-theory.

**Construction**

```
Regress next-year investment-to-assets change, d1I/A, on ln(Tobin's q), Cop, and dRoe cross-sectionally each month using a rolling 120-month window (30-month minimum), with regressors lagged 12 months to avoid look-ahead. Et[d1I/A] = fitted value using the most recent ln(q), Cop, dRoe and the averaged historical slopes. ln(q) = log[(market equity + long-term debt (DLTT) + short-term debt (DLC)) / book assets (AT)]. Cop is defined as in section 2.4.16. dRoe = Roe - Roe(4 quarters ago). All regressors winsorized at 1st/99th percentiles monthly; missing dRoe set to zero.
```

| | |
|---|---|
| **Inputs** | `AT`, `DLTT`, `DLC`, `market equity (CRSP)`, `REVT`, `COGS`, `XSGA`, `XRD`, `RECT`, `INVT`, `XPP`, `DRC`, `DRLT`, `AP`, `XACC`, `IBQ`, `book equity`, `RDQ` |
| **Portfolio sort** | NYSE deciles on expected growth Et[d1I/A], monthly rebalance; also Me-Eg 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - firms with higher expected investment growth earn higher expected returns (q-theory) |
| **Series starts** | January 1967 |
| **Credited paper** | Hou, Mo, Xue, and Zhang (2021), "An Augmented q-Factor Model with Expected Growth", Review of Finance |
| **Technical document** | section 2.4.24 |

[^ summary table](#summary)

<a id="eg-1"></a>

### Expected Growth (1m) - `eg_1`

Expected growth, following Hou, Mo, Xue, and Zhang (2021), is the fitted value from monthly cross-sectional regressions forecasting one-year-ahead investment-to-assets change using Tobin's q, cash-based operating profitability, and the change in return on equity. Firms expected to grow investment more are hypothesized to earn higher returns, consistent with q-theory.

**Construction**

```
Regress next-year investment-to-assets change, d1I/A, on ln(Tobin's q), Cop, and dRoe cross-sectionally each month using a rolling 120-month window (30-month minimum), with regressors lagged 12 months to avoid look-ahead. Et[d1I/A] = fitted value using the most recent ln(q), Cop, dRoe and the averaged historical slopes. ln(q) = log[(market equity + long-term debt (DLTT) + short-term debt (DLC)) / book assets (AT)]. Cop is defined as in section 2.4.16. dRoe = Roe - Roe(4 quarters ago). All regressors winsorized at 1st/99th percentiles monthly; missing dRoe set to zero.
```

| | |
|---|---|
| **Inputs** | `AT`, `DLTT`, `DLC`, `market equity (CRSP)`, `REVT`, `COGS`, `XSGA`, `XRD`, `RECT`, `INVT`, `XPP`, `DRC`, `DRLT`, `AP`, `XACC`, `IBQ`, `book equity`, `RDQ` |
| **Portfolio sort** | NYSE deciles on expected growth Et[d1I/A], monthly rebalance; also Me-Eg 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - firms with higher expected investment growth earn higher expected returns (q-theory) |
| **Series starts** | January 1967 |
| **Credited paper** | Hou, Mo, Xue, and Zhang (2021), "An Augmented q-Factor Model with Expected Growth", Review of Finance |
| **Technical document** | section 2.4.24 |

[^ summary table](#summary)

<a id="eg-6"></a>

### Expected Growth (6m) - `eg_6`

Expected growth, following Hou, Mo, Xue, and Zhang (2021), is the fitted value from monthly cross-sectional regressions forecasting one-year-ahead investment-to-assets change using Tobin's q, cash-based operating profitability, and the change in return on equity. Firms expected to grow investment more are hypothesized to earn higher returns, consistent with q-theory.

**Construction**

```
Regress next-year investment-to-assets change, d1I/A, on ln(Tobin's q), Cop, and dRoe cross-sectionally each month using a rolling 120-month window (30-month minimum), with regressors lagged 12 months to avoid look-ahead. Et[d1I/A] = fitted value using the most recent ln(q), Cop, dRoe and the averaged historical slopes. ln(q) = log[(market equity + long-term debt (DLTT) + short-term debt (DLC)) / book assets (AT)]. Cop is defined as in section 2.4.16. dRoe = Roe - Roe(4 quarters ago). All regressors winsorized at 1st/99th percentiles monthly; missing dRoe set to zero.
```

| | |
|---|---|
| **Inputs** | `AT`, `DLTT`, `DLC`, `market equity (CRSP)`, `REVT`, `COGS`, `XSGA`, `XRD`, `RECT`, `INVT`, `XPP`, `DRC`, `DRLT`, `AP`, `XACC`, `IBQ`, `book equity`, `RDQ` |
| **Portfolio sort** | NYSE deciles on expected growth Et[d1I/A], monthly rebalance; also Me-Eg 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - firms with higher expected investment growth earn higher expected returns (q-theory) |
| **Series starts** | January 1967 |
| **Credited paper** | Hou, Mo, Xue, and Zhang (2021), "An Augmented q-Factor Model with Expected Growth", Review of Finance |
| **Technical document** | section 2.4.24 |

[^ summary table](#summary)

<a id="fp-6"></a>

### Failure Probability (6m) - `fp_6`

Failure probability, from Campbell, Hilscher, and Szilagyi (2008), is a monthly distress-risk score combining profitability, leverage, past excess returns, volatility, size, liquidity, valuation, and price. It estimates a firm's likelihood of financial distress or bankruptcy. In the document this measure is labeled Fp and the resulting decile portfolio is Fpm6.

**Construction**

```
Fp = -9.164 - 20.264*NIMTAAVG + 1.416*TLMTA - 7.129*EXRETAVG + 1.411*SIGMA - 0.045*RSIZE - 2.132*CASHMTA + 0.075*MB - 0.058*PRICE. NIMTAAVG and EXRETAVG are geometrically-declining (phi = 2^(-1/3)) 12-month moving averages of NIMTA = net income (NIQ) / (market equity + total liabilities (LTQ)) and EXRET = log(1+firm return) - log(1+S&P500 return). TLMTA = total liabilities / (market equity + total liabilities). SIGMA = annualized 3-month rolling daily-return volatility (missing if fewer than 5 nonzero daily observations). RSIZE = log(firm market equity / S&P 500 market equity). CASHMTA = cash and short-term investments (CHEQ) / (market equity + total liabilities). MB = market-to-book equity with a 10% adjustment for small/negative book equity ($1 floor). PRICE = log share price, capped at $15; stocks priced below $1 are excluded. All right-hand variables winsorized at 1st/99th percentiles monthly.
```

| | |
|---|---|
| **Inputs** | `NIQ`, `LTQ`, `market equity (CRSP price x shares)`, `CRSP daily and monthly returns`, `S&P 500 index return`, `CHEQ`, `book equity` |
| **Portfolio sort** | NYSE deciles on Fp (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Fp 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | Low - high failure probability (distressed) firms earn lower returns (the distress anomaly) |
| **Series starts** | January 1976 |
| **Credited paper** | Campbell, Hilscher, and Szilagyi (2008) |
| **Technical document** | section 2.4.20 |

[^ summary table](#summary)

<a id="gpa"></a>

### Gross Profits-to-Assets - `gpa`

Gross profits-to-assets measures gross profitability scaled by current total assets, capturing profitability before accounting distortions further down the income statement. Higher gross profitability is hypothesized to predict higher returns.

**Construction**

```
Gpa = [total revenue (REVT) - cost of goods sold (COGS)] / total assets (AT, current, not lagged).
```

| | |
|---|---|
| **Inputs** | `REVT`, `COGS`, `AT` |
| **Portfolio sort** | NYSE deciles at end of June of year t on Gpa (fiscal year ending in t-1); also Me-Gpa 15-portfolio intersections |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - higher gross profitability predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.9 |

[^ summary table](#summary)

<a id="gla"></a>

### Gross Profits-to-Lagged Assets - `gla`

Gross profits-to-lagged assets is gross profitability scaled by lagged total assets rather than current assets, addressing the mechanical link between current profit and current asset growth. Higher gross profitability is hypothesized to predict higher returns.

**Construction**

```
Gla = [total revenue (REVT) - cost of goods sold (COGS)] / 1-year-lagged total assets (AT).
```

| | |
|---|---|
| **Inputs** | `REVT`, `COGS`, `AT` |
| **Portfolio sort** | NYSE deciles at end of June of year t on Gla (fiscal year ending in t-1); also Me-Gla 15-portfolio intersections |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - higher gross profitability predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.10 |

[^ summary table](#summary)

<a id="opa"></a>

### Operating Profits-to-Assets - `opa`

Operating profits-to-assets, following Ball, Gerakos, Linnainmaa, and Nikolaev (2015), measures operating profitability with R&D added back as an operating expense, scaled by current total assets. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Opa = [total revenue (REVT) - COGS - XSGA + R&D (XRD, zero if missing)] / total assets (AT, current, not lagged).
```

| | |
|---|---|
| **Inputs** | `REVT`, `COGS`, `XSGA`, `XRD`, `AT` |
| **Portfolio sort** | NYSE deciles at end of June of year t on Opa (fiscal year ending in t-1); also Me-Opa 15-portfolio intersections |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - higher operating profitability predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Ball, Gerakos, Linnainmaa, and Nikolaev (2015) |
| **Technical document** | section 2.4.14 |

[^ summary table](#summary)

<a id="ope"></a>

### Operating Profits-to-Equity - `ope`

Operating profits-to-equity, following Fama and French (2015), measures operating profitability scaled by book equity — the profitability leg of the Fama-French five-factor model. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Ope = [total revenue (REVT) - COGS (zero if missing) - SG&A (XSGA, zero if missing) - interest expense (XINT, zero if missing)] / book equity (current, not lagged). At least one of COGS, XSGA, XINT must be nonmissing. Book equity is stockholders' equity (SEQ, or CEQ+PSTK, or AT-LT) plus deferred taxes/ITC (TXDITC) minus preferred stock (using redemption PSTKRV, liquidating PSTKL, or par PSTK value, in that order).
```

| | |
|---|---|
| **Inputs** | `REVT`, `COGS`, `XSGA`, `XINT`, `SEQ/CEQ/AT/LT`, `TXDITC`, `PSTK/PSTKRV/PSTKL` |
| **Portfolio sort** | NYSE deciles at end of June of year t on Ope (fiscal year ending in t-1); also Me-Ope 15-portfolio intersections |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - higher operating profitability relative to equity predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Fama and French (2015) |
| **Technical document** | section 2.4.12 |

[^ summary table](#summary)

<a id="atoq-12"></a>

### Quarterly Asset Turnover (12m) - `atoq_12`

Quarterly asset turnover measures sales generated per dollar of net operating assets at quarterly frequency. Higher turnover indicates more efficient use of operating assets and is hypothesized to predict higher future returns.

**Construction**

```
Atoq = quarterly sales (SALEQ) / 1-quarter-lagged net operating assets (Noa). Noa = operating assets minus operating liabilities: operating assets = ATQ - CHEQ - IVAOQ (zero if missing); operating liabilities = ATQ - DLCQ - DLTTQ - MIBQ - PSTKQ (each zero if missing) - CEQQ. Sales are taken as of the most recent earnings announcement date (RDQ). Firms with nonpositive lagged Noa are excluded.
```

| | |
|---|---|
| **Inputs** | `SALEQ`, `ATQ`, `CHEQ`, `IVAOQ`, `DLCQ`, `DLTTQ`, `MIBQ`, `PSTKQ`, `CEQQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on Atoq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Atoq 15-portfolio intersections with NYSE size terciles |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - more efficient use of operating assets predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.7 |

[^ summary table](#summary)

<a id="atoq-1"></a>

### Quarterly Asset Turnover (1m) - `atoq_1`

Quarterly asset turnover measures sales generated per dollar of net operating assets at quarterly frequency. Higher turnover indicates more efficient use of operating assets and is hypothesized to predict higher future returns.

**Construction**

```
Atoq = quarterly sales (SALEQ) / 1-quarter-lagged net operating assets (Noa). Noa = operating assets minus operating liabilities: operating assets = ATQ - CHEQ - IVAOQ (zero if missing); operating liabilities = ATQ - DLCQ - DLTTQ - MIBQ - PSTKQ (each zero if missing) - CEQQ. Sales are taken as of the most recent earnings announcement date (RDQ). Firms with nonpositive lagged Noa are excluded.
```

| | |
|---|---|
| **Inputs** | `SALEQ`, `ATQ`, `CHEQ`, `IVAOQ`, `DLCQ`, `DLTTQ`, `MIBQ`, `PSTKQ`, `CEQQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on Atoq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Atoq 15-portfolio intersections with NYSE size terciles |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - more efficient use of operating assets predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.7 |

[^ summary table](#summary)

<a id="atoq-6"></a>

### Quarterly Asset Turnover (6m) - `atoq_6`

Quarterly asset turnover measures sales generated per dollar of net operating assets at quarterly frequency. Higher turnover indicates more efficient use of operating assets and is hypothesized to predict higher future returns.

**Construction**

```
Atoq = quarterly sales (SALEQ) / 1-quarter-lagged net operating assets (Noa). Noa = operating assets minus operating liabilities: operating assets = ATQ - CHEQ - IVAOQ (zero if missing); operating liabilities = ATQ - DLCQ - DLTTQ - MIBQ - PSTKQ (each zero if missing) - CEQQ. Sales are taken as of the most recent earnings announcement date (RDQ). Firms with nonpositive lagged Noa are excluded.
```

| | |
|---|---|
| **Inputs** | `SALEQ`, `ATQ`, `CHEQ`, `IVAOQ`, `DLCQ`, `DLTTQ`, `MIBQ`, `PSTKQ`, `CEQQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on Atoq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Atoq 15-portfolio intersections with NYSE size terciles |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - more efficient use of operating assets predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.7 |

[^ summary table](#summary)

<a id="ctoq-12"></a>

### Quarterly Capital Turnover (12m) - `ctoq_12`

Quarterly capital turnover measures sales generated per dollar of total assets at quarterly frequency, an efficiency signal hypothesized to predict higher returns.

**Construction**

```
Ctoq = quarterly sales (SALEQ) / 1-quarter-lagged total assets (ATQ), using sales as of the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `SALEQ`, `ATQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on Ctoq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Ctoq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - more efficient use of capital predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.8 |

[^ summary table](#summary)

<a id="ctoq-1"></a>

### Quarterly Capital Turnover (1m) - `ctoq_1`

Quarterly capital turnover measures sales generated per dollar of total assets at quarterly frequency, an efficiency signal hypothesized to predict higher returns.

**Construction**

```
Ctoq = quarterly sales (SALEQ) / 1-quarter-lagged total assets (ATQ), using sales as of the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `SALEQ`, `ATQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on Ctoq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Ctoq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - more efficient use of capital predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.8 |

[^ summary table](#summary)

<a id="ctoq-6"></a>

### Quarterly Capital Turnover (6m) - `ctoq_6`

Quarterly capital turnover measures sales generated per dollar of total assets at quarterly frequency, an efficiency signal hypothesized to predict higher returns.

**Construction**

```
Ctoq = quarterly sales (SALEQ) / 1-quarter-lagged total assets (ATQ), using sales as of the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `SALEQ`, `ATQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on Ctoq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Ctoq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - more efficient use of capital predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.8 |

[^ summary table](#summary)

<a id="claq-12"></a>

### Quarterly Cash-Based Operating Profits-to-Lagged Assets (12m) - `claq_12`

Quarterly cash-based operating profits-to-lagged assets is the quarterly version of Cla, scaling quarterly cash-adjusted operating profit by lagged total assets. More cash-profitable firms are hypothesized to earn higher returns.

**Construction**

```
Claq = [quarterly total revenue (REVTQ) - COGSQ - XSGAQ + R&D (XRDQ, zero if missing) - change in accounts receivable (RECTQ) - change in inventory (INVTQ) + change in deferred revenue (DRCQ + DRLTQ) + change in trade accounts payable (APQ)] / 1-quarter-lagged total assets (ATQ). All changes are quarterly; missing changes set to zero.
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XRDQ`, `RECTQ`, `INVTQ`, `DRCQ`, `DRLTQ`, `APQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Claq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Claq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - higher cash-based operating profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.18 |

[^ summary table](#summary)

<a id="claq-1"></a>

### Quarterly Cash-Based Operating Profits-to-Lagged Assets (1m) - `claq_1`

Quarterly cash-based operating profits-to-lagged assets is the quarterly version of Cla, scaling quarterly cash-adjusted operating profit by lagged total assets. More cash-profitable firms are hypothesized to earn higher returns.

**Construction**

```
Claq = [quarterly total revenue (REVTQ) - COGSQ - XSGAQ + R&D (XRDQ, zero if missing) - change in accounts receivable (RECTQ) - change in inventory (INVTQ) + change in deferred revenue (DRCQ + DRLTQ) + change in trade accounts payable (APQ)] / 1-quarter-lagged total assets (ATQ). All changes are quarterly; missing changes set to zero.
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XRDQ`, `RECTQ`, `INVTQ`, `DRCQ`, `DRLTQ`, `APQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Claq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Claq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher cash-based operating profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.18 |

[^ summary table](#summary)

<a id="claq-6"></a>

### Quarterly Cash-Based Operating Profits-to-Lagged Assets (6m) - `claq_6`

Quarterly cash-based operating profits-to-lagged assets is the quarterly version of Cla, scaling quarterly cash-adjusted operating profit by lagged total assets. More cash-profitable firms are hypothesized to earn higher returns.

**Construction**

```
Claq = [quarterly total revenue (REVTQ) - COGSQ - XSGAQ + R&D (XRDQ, zero if missing) - change in accounts receivable (RECTQ) - change in inventory (INVTQ) + change in deferred revenue (DRCQ + DRLTQ) + change in trade accounts payable (APQ)] / 1-quarter-lagged total assets (ATQ). All changes are quarterly; missing changes set to zero.
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XRDQ`, `RECTQ`, `INVTQ`, `DRCQ`, `DRLTQ`, `APQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Claq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Claq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - higher cash-based operating profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.18 |

[^ summary table](#summary)

<a id="fq-12"></a>

### Quarterly F-Score (12m) - `fq_12`

The quarterly F-score is a quarterly-frequency adaptation of Piotroski's (2000) nine-signal fundamental score, combining profitability, capital-structure/liquidity, and operating-efficiency signals into one composite. Financially healthier firms (higher score) are hypothesized to earn higher returns.

**Construction**

```
Fq = FRoa + FdRoa + FCf/A + FAcc + FdMargin + FdTurn + FdLever + FdLiquid + Eq, the sum of nine binary (0/1) indicators: FRoa=1 if quarterly Roa (IBQ/lagged ATQ) is positive; FCf/A=1 if quarterly cash flow from operations (OANCFY change, or FOPTY change minus WCAPQ change) scaled by lagged ATQ is positive; FdRoa=1 if dRoa (4Q change in Roa) is positive; FAcc=1 if Cf/A > Roa; FdMargin=1 if the change in gross margin (SALEQ-COGSQ)/SALEQ over 4 quarters is positive; FdTurn=1 if the change in asset turnover (SALEQ/lagged ATQ) over 4 quarters is positive; FdLever=1 if leverage (DLTTQ / average of current and lagged ATQ) falls over 4 quarters; FdLiquid=1 if the current ratio (ACTQ/LCTQ) improves over 4 quarters; Eq=1 if no common equity was issued (SSTKY change net of preferred stock increases) in the past 4 quarters.
```

| | |
|---|---|
| **Inputs** | `IBQ`, `ATQ`, `OANCFY or (FOPTY, WCAPQ)`, `DLTTQ`, `ACTQ`, `LCTQ`, `PSTKQ`, `SSTKY`, `SALEQ`, `COGSQ` |
| **Portfolio sort** | Sort into 7 portfolios by Fq score for the fiscal quarter ending at least 4 months prior: low (0-2), 3, 4, 5, 6, 7, high (8-9); also independent 5-group Fq x 3-group size (Me) intersections yielding 15 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - a higher composite fundamental (financial-strength) score predicts higher returns |
| **Series starts** | January 1985 |
| **Credited paper** | Piotroski (2000) |
| **Technical document** | section 2.4.19 |

[^ summary table](#summary)

<a id="fq-1"></a>

### Quarterly F-Score (1m) - `fq_1`

The quarterly F-score is a quarterly-frequency adaptation of Piotroski's (2000) nine-signal fundamental score, combining profitability, capital-structure/liquidity, and operating-efficiency signals into one composite. Financially healthier firms (higher score) are hypothesized to earn higher returns.

**Construction**

```
Fq = FRoa + FdRoa + FCf/A + FAcc + FdMargin + FdTurn + FdLever + FdLiquid + Eq, the sum of nine binary (0/1) indicators: FRoa=1 if quarterly Roa (IBQ/lagged ATQ) is positive; FCf/A=1 if quarterly cash flow from operations (OANCFY change, or FOPTY change minus WCAPQ change) scaled by lagged ATQ is positive; FdRoa=1 if dRoa (4Q change in Roa) is positive; FAcc=1 if Cf/A > Roa; FdMargin=1 if the change in gross margin (SALEQ-COGSQ)/SALEQ over 4 quarters is positive; FdTurn=1 if the change in asset turnover (SALEQ/lagged ATQ) over 4 quarters is positive; FdLever=1 if leverage (DLTTQ / average of current and lagged ATQ) falls over 4 quarters; FdLiquid=1 if the current ratio (ACTQ/LCTQ) improves over 4 quarters; Eq=1 if no common equity was issued (SSTKY change net of preferred stock increases) in the past 4 quarters.
```

| | |
|---|---|
| **Inputs** | `IBQ`, `ATQ`, `OANCFY or (FOPTY, WCAPQ)`, `DLTTQ`, `ACTQ`, `LCTQ`, `PSTKQ`, `SSTKY`, `SALEQ`, `COGSQ` |
| **Portfolio sort** | Sort into 7 portfolios by Fq score for the fiscal quarter ending at least 4 months prior: low (0-2), 3, 4, 5, 6, 7, high (8-9); also independent 5-group Fq x 3-group size (Me) intersections yielding 15 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - a higher composite fundamental (financial-strength) score predicts higher returns |
| **Series starts** | January 1985 |
| **Credited paper** | Piotroski (2000) |
| **Technical document** | section 2.4.19 |

[^ summary table](#summary)

<a id="fq-6"></a>

### Quarterly F-Score (6m) - `fq_6`

The quarterly F-score is a quarterly-frequency adaptation of Piotroski's (2000) nine-signal fundamental score, combining profitability, capital-structure/liquidity, and operating-efficiency signals into one composite. Financially healthier firms (higher score) are hypothesized to earn higher returns.

**Construction**

```
Fq = FRoa + FdRoa + FCf/A + FAcc + FdMargin + FdTurn + FdLever + FdLiquid + Eq, the sum of nine binary (0/1) indicators: FRoa=1 if quarterly Roa (IBQ/lagged ATQ) is positive; FCf/A=1 if quarterly cash flow from operations (OANCFY change, or FOPTY change minus WCAPQ change) scaled by lagged ATQ is positive; FdRoa=1 if dRoa (4Q change in Roa) is positive; FAcc=1 if Cf/A > Roa; FdMargin=1 if the change in gross margin (SALEQ-COGSQ)/SALEQ over 4 quarters is positive; FdTurn=1 if the change in asset turnover (SALEQ/lagged ATQ) over 4 quarters is positive; FdLever=1 if leverage (DLTTQ / average of current and lagged ATQ) falls over 4 quarters; FdLiquid=1 if the current ratio (ACTQ/LCTQ) improves over 4 quarters; Eq=1 if no common equity was issued (SSTKY change net of preferred stock increases) in the past 4 quarters.
```

| | |
|---|---|
| **Inputs** | `IBQ`, `ATQ`, `OANCFY or (FOPTY, WCAPQ)`, `DLTTQ`, `ACTQ`, `LCTQ`, `PSTKQ`, `SSTKY`, `SALEQ`, `COGSQ` |
| **Portfolio sort** | Sort into 7 portfolios by Fq score for the fiscal quarter ending at least 4 months prior: low (0-2), 3, 4, 5, 6, 7, high (8-9); also independent 5-group Fq x 3-group size (Me) intersections yielding 15 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - a higher composite fundamental (financial-strength) score predicts higher returns |
| **Series starts** | January 1985 |
| **Credited paper** | Piotroski (2000) |
| **Technical document** | section 2.4.19 |

[^ summary table](#summary)

<a id="glaq-12"></a>

### Quarterly Gross Profits-to-Lagged Assets (12m) - `glaq_12`

Quarterly gross profits-to-lagged assets is the quarterly version of Gla, scaling quarterly gross profit by 1-quarter-lagged total assets. Higher gross profitability is hypothesized to predict higher returns.

**Construction**

```
Glaq = [quarterly total revenue (REVTQ) - quarterly cost of goods sold (COGSQ)] / 1-quarter-lagged total assets (ATQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Glaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Glaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - higher gross profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.11 |

[^ summary table](#summary)

<a id="glaq-1"></a>

### Quarterly Gross Profits-to-Lagged Assets (1m) - `glaq_1`

Quarterly gross profits-to-lagged assets is the quarterly version of Gla, scaling quarterly gross profit by 1-quarter-lagged total assets. Higher gross profitability is hypothesized to predict higher returns.

**Construction**

```
Glaq = [quarterly total revenue (REVTQ) - quarterly cost of goods sold (COGSQ)] / 1-quarter-lagged total assets (ATQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Glaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Glaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher gross profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.11 |

[^ summary table](#summary)

<a id="glaq-6"></a>

### Quarterly Gross Profits-to-Lagged Assets (6m) - `glaq_6`

Quarterly gross profits-to-lagged assets is the quarterly version of Gla, scaling quarterly gross profit by 1-quarter-lagged total assets. Higher gross profitability is hypothesized to predict higher returns.

**Construction**

```
Glaq = [quarterly total revenue (REVTQ) - quarterly cost of goods sold (COGSQ)] / 1-quarter-lagged total assets (ATQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Glaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Glaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - higher gross profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.11 |

[^ summary table](#summary)

<a id="oq-1"></a>

### Quarterly O-Score (1m) - `oq_1`

The quarterly O-score is an accounting-based bankruptcy-risk score combining firm size, leverage, liquidity, profitability, and earnings-trend variables, estimating the probability of financial distress.

**Construction**

```
Oq = -1.32 - 0.407*log(TAq) + 6.03*TLTAq - 1.43*WCTAq + 0.076*CLCAq - 1.72*OENEGq - 2.37*NITAq - 1.83*FUTLq + 0.285*IN2q - 0.521*CHINq. TAq=total assets (ATQ); TLTAq= total debt (DLCQ+DLTTQ)/total assets; WCTAq=working capital (ACTQ-LCTQ)/total assets; CLCAq=current liabilities (LCTQ)/current assets (ACTQ); OENEGq=1 if total liabilities (LTQ) exceed total assets, else 0; NITAq=trailing 4-quarter net income (NIQ)/total assets; FUTLq=trailing 4-quarter funds from operations (PIQ+DPQ)/total liabilities; IN2q=1 if net income is negative in both the current and 4-quarters-ago quarter, else 0; CHINq=(NIQ_t - NIQ_t-4)/(|NIQ_t|+|NIQ_t-4|). Nondummy variables winsorized at 1st/99th percentiles monthly.
```

| | |
|---|---|
| **Inputs** | `ATQ`, `DLCQ`, `DLTTQ`, `ACTQ`, `LCTQ`, `LTQ`, `NIQ`, `PIQ`, `DPQ` |
| **Portfolio sort** | NYSE deciles on Oq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Oq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - higher bankruptcy-risk (O-score) firms earn lower returns (the distress anomaly) |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.21 |

[^ summary table](#summary)

<a id="olaq-12"></a>

### Quarterly Operating Profits-to-Lagged Assets (12m) - `olaq_12`

Quarterly operating profits-to-lagged assets is the quarterly version of Opa, scaling quarterly operating profit (with R&D added back) by 1-quarter-lagged total assets. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Olaq = [quarterly total revenue (REVTQ) - COGSQ - XSGAQ + R&D (XRDQ, zero if missing)] / 1-quarter-lagged total assets (ATQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XRDQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Olaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Olaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - higher operating profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.15 |

[^ summary table](#summary)

<a id="olaq-1"></a>

### Quarterly Operating Profits-to-Lagged Assets (1m) - `olaq_1`

Quarterly operating profits-to-lagged assets is the quarterly version of Opa, scaling quarterly operating profit (with R&D added back) by 1-quarter-lagged total assets. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Olaq = [quarterly total revenue (REVTQ) - COGSQ - XSGAQ + R&D (XRDQ, zero if missing)] / 1-quarter-lagged total assets (ATQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XRDQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Olaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Olaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher operating profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.15 |

[^ summary table](#summary)

<a id="olaq-6"></a>

### Quarterly Operating Profits-to-Lagged Assets (6m) - `olaq_6`

Quarterly operating profits-to-lagged assets is the quarterly version of Opa, scaling quarterly operating profit (with R&D added back) by 1-quarter-lagged total assets. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Olaq = [quarterly total revenue (REVTQ) - COGSQ - XSGAQ + R&D (XRDQ, zero if missing)] / 1-quarter-lagged total assets (ATQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XRDQ`, `ATQ` |
| **Portfolio sort** | NYSE deciles on Olaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Olaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - higher operating profitability predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.15 |

[^ summary table](#summary)

<a id="oleq-12"></a>

### Quarterly Operating Profits-to-Lagged Equity (12m) - `oleq_12`

Quarterly operating profits-to-lagged equity is the quarterly version of Ope, scaling quarterly operating profit by 1-quarter-lagged book equity. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Oleq = [quarterly total revenue (REVTQ) - COGSQ (zero if missing) - XSGAQ (zero if missing) - interest expense (XINTQ, zero if missing)] / 1-quarter-lagged book equity. At least one of COGSQ, XSGAQ, XINTQ must be nonmissing. Book equity is defined as in Roe (section 2.4.1): stockholders' equity (SEQQ, or CEQQ+PSTKQ, or ATQ-LTQ) plus deferred taxes/ITC (TXDITCQ) minus preferred stock (PSTKQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XINTQ`, `SEQQ/CEQQ/ATQ/LTQ`, `TXDITCQ`, `PSTKQ` |
| **Portfolio sort** | NYSE deciles on Oleq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Oleq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - higher operating profitability relative to equity predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.13 |

[^ summary table](#summary)

<a id="oleq-1"></a>

### Quarterly Operating Profits-to-Lagged Equity (1m) - `oleq_1`

Quarterly operating profits-to-lagged equity is the quarterly version of Ope, scaling quarterly operating profit by 1-quarter-lagged book equity. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Oleq = [quarterly total revenue (REVTQ) - COGSQ (zero if missing) - XSGAQ (zero if missing) - interest expense (XINTQ, zero if missing)] / 1-quarter-lagged book equity. At least one of COGSQ, XSGAQ, XINTQ must be nonmissing. Book equity is defined as in Roe (section 2.4.1): stockholders' equity (SEQQ, or CEQQ+PSTKQ, or ATQ-LTQ) plus deferred taxes/ITC (TXDITCQ) minus preferred stock (PSTKQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XINTQ`, `SEQQ/CEQQ/ATQ/LTQ`, `TXDITCQ`, `PSTKQ` |
| **Portfolio sort** | NYSE deciles on Oleq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Oleq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher operating profitability relative to equity predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.13 |

[^ summary table](#summary)

<a id="oleq-6"></a>

### Quarterly Operating Profits-to-Lagged Equity (6m) - `oleq_6`

Quarterly operating profits-to-lagged equity is the quarterly version of Ope, scaling quarterly operating profit by 1-quarter-lagged book equity. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Oleq = [quarterly total revenue (REVTQ) - COGSQ (zero if missing) - XSGAQ (zero if missing) - interest expense (XINTQ, zero if missing)] / 1-quarter-lagged book equity. At least one of COGSQ, XSGAQ, XINTQ must be nonmissing. Book equity is defined as in Roe (section 2.4.1): stockholders' equity (SEQQ, or CEQQ+PSTKQ, or ATQ-LTQ) plus deferred taxes/ITC (TXDITCQ) minus preferred stock (PSTKQ).
```

| | |
|---|---|
| **Inputs** | `REVTQ`, `COGSQ`, `XSGAQ`, `XINTQ`, `SEQQ/CEQQ/ATQ/LTQ`, `TXDITCQ`, `PSTKQ` |
| **Portfolio sort** | NYSE deciles on Oleq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Oleq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - higher operating profitability relative to equity predicts higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.13 |

[^ summary table](#summary)

<a id="pmq-1"></a>

### Quarterly Profit Margin (1m) - `pmq_1`

Quarterly profit margin measures operating income earned per dollar of sales, a margin-based profitability signal hypothesized to predict higher returns.

**Construction**

```
Pmq = quarterly operating income after depreciation (OIADPQ) / quarterly sales (SALEQ), for the latest fiscal quarter ending at least 4 months ago.
```

| | |
|---|---|
| **Inputs** | `OIADPQ`, `SALEQ` |
| **Portfolio sort** | NYSE deciles on Pmq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Pmq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - a higher profit margin predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.7 |

[^ summary table](#summary)

<a id="rnaq-12"></a>

### Quarterly Return on Net Operating Assets (12m) - `rnaq_12`

Quarterly return on net operating assets measures operating profitability relative to the net operating assets used to generate it. Firms earning higher returns on their operating asset base are hypothesized to earn higher stock returns.

**Construction**

```
Rnaq = quarterly operating income after depreciation (OIADPQ) / 1-quarter-lagged net operating assets (Noa). Noa = operating assets (ATQ - CHEQ - IVAOQ, zero if missing) minus operating liabilities (ATQ - DLCQ - DLTTQ - MIBQ - PSTKQ, each zero if missing, - CEQQ). Firms with nonpositive lagged Noa are excluded.
```

| | |
|---|---|
| **Inputs** | `OIADPQ`, `ATQ`, `CHEQ`, `IVAOQ`, `DLCQ`, `DLTTQ`, `MIBQ`, `PSTKQ`, `CEQQ` |
| **Portfolio sort** | NYSE deciles on Rnaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Rnaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - higher return on net operating assets predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.7 |

[^ summary table](#summary)

<a id="rnaq-1"></a>

### Quarterly Return on Net Operating Assets (1m) - `rnaq_1`

Quarterly return on net operating assets measures operating profitability relative to the net operating assets used to generate it. Firms earning higher returns on their operating asset base are hypothesized to earn higher stock returns.

**Construction**

```
Rnaq = quarterly operating income after depreciation (OIADPQ) / 1-quarter-lagged net operating assets (Noa). Noa = operating assets (ATQ - CHEQ - IVAOQ, zero if missing) minus operating liabilities (ATQ - DLCQ - DLTTQ - MIBQ - PSTKQ, each zero if missing, - CEQQ). Firms with nonpositive lagged Noa are excluded.
```

| | |
|---|---|
| **Inputs** | `OIADPQ`, `ATQ`, `CHEQ`, `IVAOQ`, `DLCQ`, `DLTTQ`, `MIBQ`, `PSTKQ`, `CEQQ` |
| **Portfolio sort** | NYSE deciles on Rnaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Rnaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - higher return on net operating assets predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.7 |

[^ summary table](#summary)

<a id="rnaq-6"></a>

### Quarterly Return on Net Operating Assets (6m) - `rnaq_6`

Quarterly return on net operating assets measures operating profitability relative to the net operating assets used to generate it. Firms earning higher returns on their operating asset base are hypothesized to earn higher stock returns.

**Construction**

```
Rnaq = quarterly operating income after depreciation (OIADPQ) / 1-quarter-lagged net operating assets (Noa). Noa = operating assets (ATQ - CHEQ - IVAOQ, zero if missing) minus operating liabilities (ATQ - DLCQ - DLTTQ - MIBQ - PSTKQ, each zero if missing, - CEQQ). Firms with nonpositive lagged Noa are excluded.
```

| | |
|---|---|
| **Inputs** | `OIADPQ`, `ATQ`, `CHEQ`, `IVAOQ`, `DLCQ`, `DLTTQ`, `MIBQ`, `PSTKQ`, `CEQQ` |
| **Portfolio sort** | NYSE deciles on Rnaq (fiscal quarter ending at least 4 months prior), monthly rebalance; also Me-Rnaq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - higher return on net operating assets predicts higher returns |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.7 |

[^ summary table](#summary)

<a id="sgq-1"></a>

### Quarterly Sales Growth (1m) - `sgq_1`

Quarterly sales growth measures the year-over-year growth rate in quarterly sales, a growth/glamour signal rather than a pure profitability level.

**Construction**

```
Sgq = quarterly sales (SALEQ) / sales four quarters ago, using the most recent quarterly earnings announcement date (RDQ) from 1972 onward.
```

| | |
|---|---|
| **Inputs** | `SALEQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on latest Sgq (fiscal quarter ending within 6 months prior), monthly rebalance; also Me-Sgq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - firms with high past sales growth (glamour) tend to earn lower future returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.23 |

[^ summary table](#summary)

<a id="tbiq-12"></a>

### Quarterly Taxable Income-to-Book Income (12m) - `tbiq_12`

Quarterly taxable income-to-book income measures the ratio of pretax income to net (book) income, an earnings-quality/conservatism signal.

**Construction**

```
Tbiq = quarterly pretax income (PIQ) / net income (NIQ), for the fiscal quarter ending at least 4 months ago. Firms with nonpositive pretax income or net income are excluded.
```

| | |
|---|---|
| **Inputs** | `PIQ`, `NIQ` |
| **Portfolio sort** | NYSE deciles on Tbiq, monthly rebalance; also Me-Tbiq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - a higher taxable-to-book income ratio signals higher earnings quality and predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.22 |

[^ summary table](#summary)

<a id="tbiq-6"></a>

### Quarterly Taxable Income-to-Book Income (6m) - `tbiq_6`

Quarterly taxable income-to-book income measures the ratio of pretax income to net (book) income, an earnings-quality/conservatism signal.

**Construction**

```
Tbiq = quarterly pretax income (PIQ) / net income (NIQ), for the fiscal quarter ending at least 4 months ago. Firms with nonpositive pretax income or net income are excluded.
```

| | |
|---|---|
| **Inputs** | `PIQ`, `NIQ` |
| **Portfolio sort** | NYSE deciles on Tbiq, monthly rebalance; also Me-Tbiq 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - a higher taxable-to-book income ratio signals higher earnings quality and predicts higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.22 |

[^ summary table](#summary)

<a id="roa-1"></a>

### Return on Assets (1m) - `roa_1`

Return on assets measures profitability per dollar of total assets, a quality signal independent of capital structure. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Roa = income before extraordinary items (IBQ) / 1-quarter-lagged total assets (ATQ), computed with quarterly earnings from the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `ATQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on Roa (fiscal quarter ending within 6 months prior), monthly rebalance; also Me-Roa 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - more profitable firms earn higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.3 |

[^ summary table](#summary)

<a id="roa-6"></a>

### Return on Assets (6m) - `roa_6`

Return on assets measures profitability per dollar of total assets, a quality signal independent of capital structure. More profitable firms are hypothesized to earn higher returns.

**Construction**

```
Roa = income before extraordinary items (IBQ) / 1-quarter-lagged total assets (ATQ), computed with quarterly earnings from the most recent earnings announcement date (RDQ).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `ATQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on Roa (fiscal quarter ending within 6 months prior), monthly rebalance; also Me-Roa 15-portfolio intersections |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - more profitable firms earn higher returns |
| **Series starts** | January 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.4.3 |

[^ summary table](#summary)

<a id="roe-1"></a>

### Return on Equity (1m) - `roe_1`

Return on equity measures a firm's profitability relative to its shareholders' equity. Firms earning more per unit of book equity are considered higher quality and are hypothesized to earn higher future stock returns.

**Construction**

```
Roe = income before extraordinary items (IBQ) / 1-quarter-lagged book equity. Book equity = stockholders' equity (SEQQ, or CEQQ + PSTKQ, or ATQ - LTQ, in that priority order) plus balance sheet deferred taxes and investment tax credit (TXDITCQ) if available, minus book value of preferred stock (PSTKQ). Before 1972, coverage is expanded using annual book equity and clean-surplus imputation (BEQt = BEQt-j + IBQt-j+1,t - DVQt-j+1,t, j up to 4 quarters).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `SEQQ/CEQQ/ATQ/LTQ`, `TXDITCQ`, `PSTKQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on most recent past Roe, monthly rebalance; also Me-Roe 15-portfolio intersections with NYSE size terciles |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - more profitable firms earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Hou, Xue, and Zhang (2015) |
| **Technical document** | section 2.4.1 |

[^ summary table](#summary)

<a id="roe-6"></a>

### Return on Equity (6m) - `roe_6`

Return on equity measures a firm's profitability relative to its shareholders' equity. Firms earning more per unit of book equity are considered higher quality and are hypothesized to earn higher future stock returns.

**Construction**

```
Roe = income before extraordinary items (IBQ) / 1-quarter-lagged book equity. Book equity = stockholders' equity (SEQQ, or CEQQ + PSTKQ, or ATQ - LTQ, in that priority order) plus balance sheet deferred taxes and investment tax credit (TXDITCQ) if available, minus book value of preferred stock (PSTKQ). Before 1972, coverage is expanded using annual book equity and clean-surplus imputation (BEQt = BEQt-j + IBQt-j+1,t - DVQt-j+1,t, j up to 4 quarters).
```

| | |
|---|---|
| **Inputs** | `IBQ`, `SEQQ/CEQQ/ATQ/LTQ`, `TXDITCQ`, `PSTKQ`, `RDQ` |
| **Portfolio sort** | NYSE deciles on most recent past Roe, monthly rebalance; also Me-Roe 15-portfolio intersections with NYSE size terciles |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - more profitable firms earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | Hou, Xue, and Zhang (2015) |
| **Technical document** | section 2.4.1 |

[^ summary table](#summary)
