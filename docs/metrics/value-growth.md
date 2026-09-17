# Value-versus-Growth

Signals that compare an accounting or cash-flow anchor to the market price. The shared idea is that a low price relative to fundamentals signals a higher expected return, whether because of risk or because of over-pessimism.

32 anomalies. Definitions from Kewei Hou, Chen Xue, and Lu Zhang, "Technical Document: Testing Portfolios," global-q.org, July 2026.

[<- back to the metric index](../METRICS.md)

## Summary

| Code | Metric | What it measures | Which end wins | Rebalance | Holding | Starts |
|---|---|---|---|---|---|---|
| `vfp` | [Analyst Forecast-based Intrinsic Value-to-Market](#vfp) | Residual-income-model estimate of a firm's intrinsic value relative to its market value (Frankel and Lee 1998), using IBES analyst earnings forecasts to project future profitability instead of historical ROE. Stocks whose estimated intrinsic value is high relative to price (undervalued) are expected to earn higher returns. | High | annual (June) | 12 months | July 1976 |
| `bmj` | [Book-to-June-end Market Equity](#bmj) | A value measure using book equity per share divided by June-end share price rather than December market equity, aligning book and price more closely in time. Following Asness and Frazzini (2013), high Bmj (cheap) stocks are expected to earn higher returns. | High | annual (June) | 12 months | January 1967 |
| `bm` | [Book-to-Market Equity](#bm) | Measures value cheapness as accounting book equity relative to the market's valuation of equity. High book-to-market ('cheap') stocks are hypothesized to earn a value premium over low book-to-market ('growth') stocks. | High | annual (June) | 12 months | January 1967 |
| `cp` | [Cash Flow-to-Price](#cp) | Value measure using operating cash flow (approximated as earnings plus depreciation) relative to market value; high cash-flow yield (cheap) stocks are expected to earn a value premium. | High | annual (June) | 12 months | January 1967 |
| `dp` | [Dividend Yield](#dp) | Measures cash dividends paid over the prior year relative to current market value; a classic value/income signal where high-yield stocks are hypothesized to earn a premium. | High | annual (June) | 12 months | January 1967 |
| `ep` | [Earnings-to-Price](#ep) | Value measure comparing a firm's accounting earnings to its market value; high earnings yield (cheap) stocks are expected to earn a value premium over low-yield ('growth') stocks. | High | annual (June) | 12 months | January 1967 |
| `ebp` | [Enterprise Book-to-Price](#ebp) | Following Penman, Richardson, and Tuna (2007), measures value on an enterprise (operating-asset) basis: the book value of net operating assets relative to their market value, separating operating value from financing leverage effects. | High | annual (June) | 12 months | January 1967 |
| `em` | [Enterprise Multiple](#em) | Values a firm on an enterprise basis (equity plus net debt and preferred, minus cash) relative to operating income, capturing value net of capital structure. A low enterprise multiple (cheap on an EV basis) is expected to earn a value premium. | Low | annual (June) | 12 months | January 1967 |
| `dur` | [Equity Duration](#dur) | Following Dechow, Sloan, and Soliman (2004), measures the weighted-average timing of a firm's expected future cash distributions to equity holders, analogous to bond duration. Low-duration (near-term cash-heavy, value-like) stocks are expected to earn higher returns than high-duration (long-duration, growth-like) stocks. | Low | annual (June) | 12 months | January 1967 |
| `vhp` | [Historical Intrinsic Value-to-Market](#vhp) | Residual-income-model estimate of a firm's intrinsic value relative to its market value (Frankel and Lee 1998), using only the firm's historical return on equity to project future profitability. Stocks whose estimated intrinsic value is high relative to price (undervalued) are expected to earn higher returns. | High | annual (June) | 12 months | January 1967 |
| `ir` | [Intangible Return](#ir) | Isolates the part of a firm's past 5-year stock return not explained by its lagged book-to-market and its 5-year fundamental (book) return — the return attributable to intangible information rather than tangible book-value growth. High intangible return predicts continued outperformance. | High | annual (June) | 12 months | January 1967 |
| `rev_12` | [Long-term Reversal (12m)](#rev-12) | Captures the De Bondt and Thaler (1985) long-term reversal effect: stocks with low cumulative returns over the prior 5 years (months t-60 to t-13, skipping the most recent year) tend to subsequently outperform, while past long-term winners tend to underperform. | Low | monthly | 12 months | January 1967 |
| `rev_1` | [Long-term Reversal (1m)](#rev-1) | Captures the De Bondt and Thaler (1985) long-term reversal effect: stocks with low cumulative returns over the prior 5 years (months t-60 to t-13, skipping the most recent year) tend to subsequently outperform, while past long-term winners tend to underperform. | Low | monthly | 1 month | January 1967 |
| `rev_6` | [Long-term Reversal (6m)](#rev-6) | Captures the De Bondt and Thaler (1985) long-term reversal effect: stocks with low cumulative returns over the prior 5 years (months t-60 to t-13, skipping the most recent year) tend to subsequently outperform, while past long-term winners tend to underperform. | Low | monthly | 6 months | January 1967 |
| `nop` | [Net Payout Yield](#nop) | Measures net cash returned to shareholders — total payouts minus equity issuance — relative to market value. Per Boudoukh, Michaely, Richardson, and Roberts (2007), high net-payout-yield stocks are expected to earn higher returns. | High | annual (June) | 12 months | July 1972 |
| `ocp` | [Operating Cash Flow-to-Price](#ocp) | Value measure using operating cash flow taken directly from the cash flow statement, rather than earnings-based proxies, relative to market value. | High | annual (June) | 12 months | July 1972 |
| `op` | [Payout Yield](#op) | Measures total shareholder payouts (dividends plus share repurchases) relative to market value. Per Boudoukh, Michaely, Richardson, and Roberts (2007), high payout-yield stocks are expected to earn higher returns. | High | annual (June) | 12 months | July 1972 |
| `bmq_12` | [Quarterly Book-to-market Equity (12m)](#bmq-12) | A higher-frequency book-to-market measure using the latest available quarterly book equity, updated monthly, to capture value more promptly than the annual version. | High | monthly | 12 months | January 1967 |
| `cpq_12` | [Quarterly Cash Flow-to-Price (12m)](#cpq-12) | Higher-frequency cash-flow yield using the latest quarterly cash flow (quarterly earnings plus quarterly depreciation) relative to current market value. | High | monthly | 12 months | January 1967 |
| `cpq_1` | [Quarterly Cash Flow-to-Price (1m)](#cpq-1) | Higher-frequency cash-flow yield using the latest quarterly cash flow (quarterly earnings plus quarterly depreciation) relative to current market value. | High | monthly | 1 month | January 1967 |
| `cpq_6` | [Quarterly Cash Flow-to-Price (6m)](#cpq-6) | Higher-frequency cash-flow yield using the latest quarterly cash flow (quarterly earnings plus quarterly depreciation) relative to current market value. | High | monthly | 6 months | January 1967 |
| `epq_12` | [Quarterly Earnings-to-Price (12m)](#epq-12) | A higher-frequency earnings yield using the most recently announced quarterly earnings rather than annual earnings, capturing value more promptly using fresh accounting information. | High | monthly | 12 months | January 1967 |
| `epq_1` | [Quarterly Earnings-to-Price (1m)](#epq-1) | A higher-frequency earnings yield using the most recently announced quarterly earnings rather than annual earnings, capturing value more promptly using fresh accounting information. | High | monthly | 1 month | January 1967 |
| `epq_6` | [Quarterly Earnings-to-Price (6m)](#epq-6) | A higher-frequency earnings yield using the most recently announced quarterly earnings rather than annual earnings, capturing value more promptly using fresh accounting information. | High | monthly | 6 months | January 1967 |
| `emq_12` | [Quarterly Enterprise Multiple (12m)](#emq-12) | Higher-frequency enterprise multiple using the latest quarterly operating income and current market value/balance sheet items. | Low | monthly | 12 months | January 1976 |
| `emq_1` | [Quarterly Enterprise Multiple (1m)](#emq-1) | Higher-frequency enterprise multiple using the latest quarterly operating income and current market value/balance sheet items. | Low | monthly | 1 month | January 1976 |
| `emq_6` | [Quarterly Enterprise Multiple (6m)](#emq-6) | Higher-frequency enterprise multiple using the latest quarterly operating income and current market value/balance sheet items. | Low | monthly | 6 months | January 1976 |
| `ocpq_1` | [Quarterly Operating Cash Flow-to-Price (1m)](#ocpq-1) | Higher-frequency operating cash flow yield using the latest quarterly operating cash flow relative to current market value; the document constructs only a 1-month holding-period version. | High | monthly | 1 month | January 1985 |
| `spq_12` | [Quarterly Sales-to-Price (12m)](#spq-12) | Higher-frequency sales yield using the most recently announced quarterly sales relative to current market value. | High | monthly | 12 months | January 1967 |
| `spq_1` | [Quarterly Sales-to-Price (1m)](#spq-1) | Higher-frequency sales yield using the most recently announced quarterly sales relative to current market value. | High | monthly | 1 month | January 1967 |
| `spq_6` | [Quarterly Sales-to-Price (6m)](#spq-6) | Higher-frequency sales yield using the most recently announced quarterly sales relative to current market value. | High | monthly | 6 months | January 1967 |
| `sp` | [Sales-to-Price](#sp) | Value measure comparing total sales/revenue to market value; less affected by accounting accruals than earnings-based measures. High sales yield (cheap) stocks are expected to earn a value premium. | High | annual (June) | 12 months | January 1967 |

## Detail

<a id="vfp"></a>

### Analyst Forecast-based Intrinsic Value-to-Market - `vfp`

Residual-income-model estimate of a firm's intrinsic value relative to its market value (Frankel and Lee 1998), using IBES analyst earnings forecasts to project future profitability instead of historical ROE. Stocks whose estimated intrinsic value is high relative to price (undervalued) are expected to earn higher returns.

**Construction**

```
Vft = Bt + (E[Roe(t+1)]-r)/(1+r)*Bt + (E[Roe(t+2)]-r)/[(1+r)^2*r]*B(t+1) + (E[Roe(t+3)]-r)/[(1+r)^2*r]*B(t+2). Roe expectations from IBES consensus 1- and 2-year-ahead EPS forecasts (Fy1, Fy2, unadjusted MEANEST) and long-term growth forecast (Ltg): E[Roe(t+1)] = s*Fy1/[(B(t+1)+Bt)/2]; E[Roe(t+2)] = s*Fy2/[(B(t+2)+B(t+1))/2]; E[Roe(t+3)] = s*Fy2*(1+Ltg)/[(B(t+3)+B(t+2))/2] (= E[Roe(t+2)] if Ltg missing); s = shares outstanding from IBES (or CRSP SHROUT on the IBES pricing date). Firms excluded if expected Roe or payout ratio exceeds 100% or book equity is negative. Vfp = Vft / market equity (CRSP, end of June t).
```

| | |
|---|---|
| **Inputs** | `Compustat annual CEQ, DVC, IBCOM, AT`, `IBES consensus EPS forecasts (MEANEST, fiscal period 1 and 2)`, `IBES long-term growth forecast (MEANEST, fiscal period 0)`, `IBES/CRSP shares outstanding and pricing date`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Vfp formed at the end of June each year t; also 15 Me-Vfp portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - undervalued stocks (high intrinsic-value-to-price) earn a value premium |
| **Series starts** | July 1976 |
| **Credited paper** | Frankel and Lee (1998) |
| **Technical document** | section 2.2.18 |

[^ summary table](#summary)

<a id="bmj"></a>

### Book-to-June-end Market Equity - `bmj`

A value measure using book equity per share divided by June-end share price rather than December market equity, aligning book and price more closely in time. Following Asness and Frazzini (2013), high Bmj (cheap) stocks are expected to earn higher returns.

**Construction**

```
Bmj = book equity per share (fiscal year ending in calendar year t-1) / share price (CRSP) at end of June of year t, adjusted for stock splits between fiscal year end and June. Book equity per share = book equity / shares outstanding (CSHO). Book equity computed as in Bm (SEQ, or CEQ+PSTK, or AT-LT; plus TXDITC; minus preferred stock via PSTKRV/PSTKL/PSTK). Firms with nonpositive book equity excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat annual CSHO`, `Compustat annual SEQ/CEQ/PSTK/AT/LT`, `Compustat annual TXDITC`, `Compustat annual PSTKRV/PSTKL/PSTK`, `CRSP share price at June` |
| **Portfolio sort** | Deciles on Bmj formed at the end of June each year t; also independently 5x3 sorted with Me (NYSE 20th/50th percentile terciles) into 15 Me-Bmj portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high book-to-price) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Asness and Frazzini (2013) |
| **Technical document** | section 2.2.2 |

[^ summary table](#summary)

<a id="bm"></a>

### Book-to-Market Equity - `bm`

Measures value cheapness as accounting book equity relative to the market's valuation of equity. High book-to-market ('cheap') stocks are hypothesized to earn a value premium over low book-to-market ('growth') stocks.

**Construction**

```
Bm = book equity (fiscal year ending in calendar year t-1) / market equity (CRSP, end of December t-1). Book equity = stockholders' equity (SEQ), else CEQ + PSTK, else AT - LT; plus TXDITC if available; minus preferred stock (PSTKRV, else PSTKL, else PSTK). Firms with nonpositive book equity excluded; market equity of multiple share classes merged.
```

| | |
|---|---|
| **Inputs** | `Compustat annual SEQ`, `Compustat annual CEQ, PSTK, AT, LT`, `Compustat annual TXDITC`, `Compustat annual PSTKRV/PSTKL/PSTK`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Bm formed at the end of June each year t, rebalanced annually in June of t+1; also independently sorted 5 (Bm quintile) x 3 (NYSE 20th/50th percentile Me tercile) into 15 Me-Bm portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high book-to-market) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.1 |

[^ summary table](#summary)

<a id="cp"></a>

### Cash Flow-to-Price - `cp`

Value measure using operating cash flow (approximated as earnings plus depreciation) relative to market value; high cash-flow yield (cheap) stocks are expected to earn a value premium.

**Construction**

```
Cp = cash flow (IB + depreciation DP) for fiscal year ending in calendar year t-1 / market equity (CRSP) at end of December of t-1. Firms with nonpositive cash flows excluded; multiple share classes merged.
```

| | |
|---|---|
| **Inputs** | `Compustat annual IB`, `Compustat annual DP`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Cp formed at the end of June each year t; also 15 Me-Cp portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high cash-flow yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.7 |

[^ summary table](#summary)

<a id="dp"></a>

### Dividend Yield - `dp`

Measures cash dividends paid over the prior year relative to current market value; a classic value/income signal where high-yield stocks are hypothesized to earn a premium.

**Construction**

```
Dp = total dividends paid from July of t-1 to June of t / market equity (CRSP) at end of June of t. Daily dividends = prior trading day's market equity x (return with dividends - return without dividends), summed over the period. Firms that pay no dividends are excluded.
```

| | |
|---|---|
| **Inputs** | `CRSP daily returns with and without dividends`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Dp formed at the end of June each year t; also 15 Me-Dp portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - high dividend-yield stocks earn a value/income premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.9 |

[^ summary table](#summary)

<a id="ep"></a>

### Earnings-to-Price - `ep`

Value measure comparing a firm's accounting earnings to its market value; high earnings yield (cheap) stocks are expected to earn a value premium over low-yield ('growth') stocks.

**Construction**

```
Ep = income before extraordinary items (IB) for fiscal year ending in calendar year t-1 / market equity (CRSP) at end of December of t-1. Firms with nonpositive earnings excluded; multiple share classes merged.
```

| | |
|---|---|
| **Inputs** | `Compustat annual IB`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Ep formed at the end of June each year t; also independently 5x3 sorted with Me into 15 Me-Ep portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high earnings yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.5 |

[^ summary table](#summary)

<a id="ebp"></a>

### Enterprise Book-to-Price - `ebp`

Following Penman, Richardson, and Tuna (2007), measures value on an enterprise (operating-asset) basis: the book value of net operating assets relative to their market value, separating operating value from financing leverage effects.

**Construction**

```
Ebp = book value of net operating assets / market value of net operating assets. Net operating assets = net debt + equity (book, for Ebp). Net debt = financial liabilities (DLTT + DLC + PSTK + DVPA, less TSTKP) minus financial assets (CHE). Book equity = CEQ + TSTKP - DVPA. Market equity = shares outstanding x share price (CRSP). Firms with nonpositive book or market value of net operating assets excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat annual DLTT, DLC, PSTK, DVPA, TSTKP, CHE`, `Compustat annual CEQ`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Ebp formed at the end of June each year t; also 15 Me-Ebp portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high book-to-market on an enterprise basis) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Penman, Richardson, and Tuna (2007) |
| **Technical document** | section 2.2.19 |

[^ summary table](#summary)

<a id="em"></a>

### Enterprise Multiple - `em`

Values a firm on an enterprise basis (equity plus net debt and preferred, minus cash) relative to operating income, capturing value net of capital structure. A low enterprise multiple (cheap on an EV basis) is expected to earn a value premium.

**Construction**

```
Em = enterprise value / operating income before depreciation (OIBDP) for fiscal year ending in calendar year t-1. Enterprise value = market equity (CRSP, end of December t-1) + total debt (DLC + DLTT) + preferred stock (PSTKRV) - cash and short-term investments (CHE). Firms with nonpositive enterprise value or operating income excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat annual OIBDP`, `Compustat annual DLC, DLTT, PSTKRV, CHE`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Em formed at the end of June each year t; also 15 Me-Em portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - a low enterprise multiple (cheap relative to operating income) earns a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.11 |

[^ summary table](#summary)

<a id="dur"></a>

### Equity Duration - `dur`

Following Dechow, Sloan, and Soliman (2004), measures the weighted-average timing of a firm's expected future cash distributions to equity holders, analogous to bond duration. Low-duration (near-term cash-heavy, value-like) stocks are expected to earn higher returns than high-duration (long-duration, growth-like) stocks.

**Construction**

```
Dur = [sum_{t=1}^{T} t*CDt/(1+r)^t]/Me + [(T+1+r)/r]*[Me - sum_{t=1}^{T} CDt/(1+r)^t]/Me. CDt = B(t-1)*(Roet - gt), the net cash distribution; Me = market equity (PRCC_F x CSHO). Roe and book-equity growth g are forecast via AR(1) processes (Roe: autocorrelation 0.57, long-run mean 0.12; growth: autocorrelation 0.24, long-run mean 0.06), with starting values from IB / lagged CEQ (Roe) and the annual change in SALE (growth proxy). T = 10-year forecast horizon; r = 12% cost of equity. Firms excluded if book equity turns negative during the forecast period or Dur is nonpositive.
```

| | |
|---|---|
| **Inputs** | `Compustat annual PRCC_F, CSHO`, `Compustat annual IB, CEQ`, `Compustat annual SALE` |
| **Portfolio sort** | Deciles on Dur formed at the end of June each year t; also 15 Me-Dur portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - low equity duration (near-term, value-like cash flows) earns a premium over long-duration growth stocks |
| **Series starts** | January 1967 |
| **Credited paper** | Dechow, Sloan, and Soliman (2004) |
| **Technical document** | section 2.2.20 |

[^ summary table](#summary)

<a id="vhp"></a>

### Historical Intrinsic Value-to-Market - `vhp`

Residual-income-model estimate of a firm's intrinsic value relative to its market value (Frankel and Lee 1998), using only the firm's historical return on equity to project future profitability. Stocks whose estimated intrinsic value is high relative to price (undervalued) are expected to earn higher returns.

**Construction**

```
Vht = Bt + (E[Roe(t+1)]-r)/(1+r)*Bt + (E[Roe(t+2)]-r)/[(1+r)*r]*B(t+1), with all Roe expectations replaced by the most recent historical Roet = Nit/[(Bt+B(t-1))/2]. Bt = book equity (CEQ) for fiscal year ending t-1; future book equity via clean surplus: B(t+1) = (1+(1-k)*E[Roe(t+1)])*Bt; k = dividend payout ratio (DVC/IBCOM, or dividends/6% of average AT if earnings negative); r = 12% discount rate. Vhp = Vht / market equity (CRSP, end of December t-1).
```

| | |
|---|---|
| **Inputs** | `Compustat annual CEQ`, `Compustat annual DVC, IBCOM, AT`, `Compustat annual net income`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Vhp formed at the end of June each year t; also 15 Me-Vhp portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - undervalued stocks (high intrinsic-value-to-price) earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Frankel and Lee (1998) |
| **Technical document** | section 2.2.18 |

[^ summary table](#summary)

<a id="ir"></a>

### Intangible Return - `ir`

Isolates the part of a firm's past 5-year stock return not explained by its lagged book-to-market and its 5-year fundamental (book) return — the return attributable to intangible information rather than tangible book-value growth. High intangible return predicts continued outperformance.

**Construction**

```
Cross-sectional regression each June: r(t-5,t) = gamma0 + gamma1*bm(t-5) + gamma2*rB(t-5,t) + u. r(t-5,t) is the 5-year log stock return (end of year t-6 to t-1; requires all 60 monthly returns non-missing and free of the CRSP 'GP' flag). bm(t-5) = log(B(t-5)/M(t-5)), the 5-year-lagged log book-to-market. rB(t-5,t) = log(Bt/B(t-5)) + sum over s=t-5..t-1 of (stock return - log price return), the 5-year log book return. Book equity defined as in Bm. Ir is the firm's residual u from the regression.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns and prices`, `Compustat annual book equity items (SEQ/CEQ/PSTK/AT/LT/TXDITC)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Ir formed at the end of June each year t; also 15 Me-Ir portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - high intangible return (positive residual) predicts continued outperformance |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.17 |

[^ summary table](#summary)

<a id="rev-12"></a>

### Long-term Reversal (12m) - `rev_12`

Captures the De Bondt and Thaler (1985) long-term reversal effect: stocks with low cumulative returns over the prior 5 years (months t-60 to t-13, skipping the most recent year) tend to subsequently outperform, while past long-term winners tend to underperform.

**Construction**

```
Deciles based on cumulative return from month t-60 to t-13. Requires a valid price at end of month t-61 and t-13, and all monthly returns from t-60 to t-13 non-missing and free of the CRSP 'GP' flag.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns`, `CRSP monthly prices`, `CRSP return flags (GP)` |
| **Portfolio sort** | Deciles on prior return t-60 to t-13, formed at the beginning of each month t, held from month t to t+11 (12 months) as the average of 12 overlapping monthly subdeciles; also independently 5x3 sorted with Me into 15 Me-Rev12 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | Low - prior 5-year losers subsequently reverse upward and earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | De Bondt and Thaler (1985) |
| **Technical document** | section 2.2.4 |

[^ summary table](#summary)

<a id="rev-1"></a>

### Long-term Reversal (1m) - `rev_1`

Captures the De Bondt and Thaler (1985) long-term reversal effect: stocks with low cumulative returns over the prior 5 years (months t-60 to t-13, skipping the most recent year) tend to subsequently outperform, while past long-term winners tend to underperform.

**Construction**

```
Deciles based on cumulative return from month t-60 to t-13. Requires a valid price at end of month t-61 and t-13, and all monthly returns from t-60 to t-13 non-missing and free of the CRSP 'GP' flag (which marks months whose compounded return excludes a large price gap).
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns`, `CRSP monthly prices`, `CRSP return flags (GP)` |
| **Portfolio sort** | Deciles on prior return t-60 to t-13, formed at the beginning of each month t, held for 1 month (current month t); also independently 5x3 sorted with Me into 15 Me-Rev1 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - prior 5-year losers subsequently reverse upward and earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | De Bondt and Thaler (1985) |
| **Technical document** | section 2.2.4 |

[^ summary table](#summary)

<a id="rev-6"></a>

### Long-term Reversal (6m) - `rev_6`

Captures the De Bondt and Thaler (1985) long-term reversal effect: stocks with low cumulative returns over the prior 5 years (months t-60 to t-13, skipping the most recent year) tend to subsequently outperform, while past long-term winners tend to underperform.

**Construction**

```
Deciles based on cumulative return from month t-60 to t-13. Requires a valid price at end of month t-61 and t-13, and all monthly returns from t-60 to t-13 non-missing and free of the CRSP 'GP' flag.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns`, `CRSP monthly prices`, `CRSP return flags (GP)` |
| **Portfolio sort** | Deciles on prior return t-60 to t-13, formed at the beginning of each month t, held from month t to t+5 (6 months) as the average of 6 overlapping monthly subdeciles; also independently 5x3 sorted with Me into 15 Me-Rev6 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | Low - prior 5-year losers subsequently reverse upward and earn higher returns |
| **Series starts** | January 1967 |
| **Credited paper** | De Bondt and Thaler (1985) |
| **Technical document** | section 2.2.4 |

[^ summary table](#summary)

<a id="nop"></a>

### Net Payout Yield - `nop`

Measures net cash returned to shareholders — total payouts minus equity issuance — relative to market value. Per Boudoukh, Michaely, Richardson, and Roberts (2007), high net-payout-yield stocks are expected to earn higher returns.

**Construction**

```
Nop = net payouts (total payouts [DVC + PRSTKC + reduction in PSTKRV] minus equity issuances [sale of stock SSTK - increase in PSTKRV]) for fiscal year ending in calendar year t-1 / market equity (CRSP) at end of December of t-1. Firms with zero net payouts excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat annual DVC, PRSTKC, PSTKRV`, `Compustat annual SSTK`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Nop formed at the end of June each year t; also 15 Me-Nop portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - high net-payout-yield stocks earn a premium |
| **Series starts** | July 1972 |
| **Credited paper** | Boudoukh, Michaely, Richardson, and Roberts (2007) |
| **Technical document** | section 2.2.10 |

[^ summary table](#summary)

<a id="ocp"></a>

### Operating Cash Flow-to-Price - `ocp`

Value measure using operating cash flow taken directly from the cash flow statement, rather than earnings-based proxies, relative to market value.

**Construction**

```
Ocp = operating cash flow for fiscal year ending in calendar year t-1 / market equity (CRSP) at end of December of t-1. Operating cash flow = funds from operations (FOPT) minus change in working capital (WCAP) prior to 1988; net cash flow from operating activities (OANCF) from 1988 onward. Firms with nonpositive operating cash flows excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat annual FOPT, WCAP (pre-1988)`, `Compustat annual OANCF (1988+)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Ocp formed at the end of June each year t; also 15 Me-Ocp portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high operating-cash-flow yield) stocks earn a value premium |
| **Series starts** | July 1972 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.15 |

[^ summary table](#summary)

<a id="op"></a>

### Payout Yield - `op`

Measures total shareholder payouts (dividends plus share repurchases) relative to market value. Per Boudoukh, Michaely, Richardson, and Roberts (2007), high payout-yield stocks are expected to earn higher returns.

**Construction**

```
Op = total payouts (dividends on common stock DVC + repurchases [expenditure on purchase of common/preferred stock PRSTKC + reduction in preferred stock outstanding PSTKRV]) for fiscal year ending in calendar year t-1 / market equity (CRSP) at end of December of t-1. Firms with nonpositive total payouts excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat annual DVC`, `Compustat annual PRSTKC`, `Compustat annual PSTKRV`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Op formed at the end of June each year t; also 15 Me-Op portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - high payout-yield stocks earn a premium |
| **Series starts** | July 1972 |
| **Credited paper** | Boudoukh, Michaely, Richardson, and Roberts (2007) |
| **Technical document** | section 2.2.10 |

[^ summary table](#summary)

<a id="bmq-12"></a>

### Quarterly Book-to-market Equity (12m) - `bmq_12`

A higher-frequency book-to-market measure using the latest available quarterly book equity, updated monthly, to capture value more promptly than the annual version.

**Construction**

```
Bmq = book equity for the latest fiscal quarter ending at least 4 months ago / market equity (CRSP) at end of month t-1. Book equity = SEQQ, else CEQQ + preferred stock, else ATQ - LTQ, plus TXDITCQ if available, minus PSTKQ. Pre-1972 coverage supplemented with annual book equity; where both unavailable, imputed forward via clean-surplus accounting: BEQt = BEQ(t-j) + IBQ(t-j+1,t) - DVQ(t-j+1,t), for j<=4 quarters. Firms with nonpositive book equity excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly SEQQ/CEQQ/ATQ/LTQ/PSTKQ`, `Compustat quarterly TXDITCQ`, `Compustat annual book-equity items (SEQ/CEQ/PSTK/AT/LT/TXDITC) for Q4 supplementation`, `Compustat quarterly IBQ, DVPSXQ, CSHOQ, AJEXQ`, `CRSP market equity, SHROUT, MTHCFACSHR` |
| **Portfolio sort** | Deciles on Bmq formed at the beginning of each month t, held 12 months (Bmq12) as the average of 12 overlapping monthly subdeciles; also independently 5x3 sorted with Me into 15 Me-Bmq12 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high book-to-market) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.3 |

[^ summary table](#summary)

<a id="cpq-12"></a>

### Quarterly Cash Flow-to-Price (12m) - `cpq_12`

Higher-frequency cash-flow yield using the latest quarterly cash flow (quarterly earnings plus quarterly depreciation) relative to current market value.

**Construction**

```
Cpq = quarterly cash flow (IBQ + DPQ) for the latest fiscal quarter ending at least 4 months ago / market equity (CRSP) at end of month t-1. Firms with nonpositive cash flows excluded; multiple share classes merged.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly IBQ`, `Compustat quarterly DPQ`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Cpq formed at the beginning of each month t, held from month t to t+11 (12 months) as the average of 12 overlapping monthly subdeciles; also 15 Me-Cpq12 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high cash-flow yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.8 |

[^ summary table](#summary)

<a id="cpq-1"></a>

### Quarterly Cash Flow-to-Price (1m) - `cpq_1`

Higher-frequency cash-flow yield using the latest quarterly cash flow (quarterly earnings plus quarterly depreciation) relative to current market value.

**Construction**

```
Cpq = quarterly cash flow (IBQ + DPQ) for the latest fiscal quarter ending at least 4 months ago / market equity (CRSP) at end of month t-1. Firms with nonpositive cash flows excluded; multiple share classes merged.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly IBQ`, `Compustat quarterly DPQ`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Cpq formed at the beginning of each month t, held for 1 month (current month t); also 15 Me-Cpq1 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - cheap (high cash-flow yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.8 |

[^ summary table](#summary)

<a id="cpq-6"></a>

### Quarterly Cash Flow-to-Price (6m) - `cpq_6`

Higher-frequency cash-flow yield using the latest quarterly cash flow (quarterly earnings plus quarterly depreciation) relative to current market value.

**Construction**

```
Cpq = quarterly cash flow (IBQ + DPQ) for the latest fiscal quarter ending at least 4 months ago / market equity (CRSP) at end of month t-1. Firms with nonpositive cash flows excluded; multiple share classes merged.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly IBQ`, `Compustat quarterly DPQ`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Cpq formed at the beginning of each month t, held from month t to t+5 (6 months) as the average of 6 overlapping monthly subdeciles; also 15 Me-Cpq6 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - cheap (high cash-flow yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.8 |

[^ summary table](#summary)

<a id="epq-12"></a>

### Quarterly Earnings-to-Price (12m) - `epq_12`

A higher-frequency earnings yield using the most recently announced quarterly earnings rather than annual earnings, capturing value more promptly using fresh accounting information.

**Construction**

```
Epq = income before extraordinary items (IBQ) from the most recent quarterly earnings (post-1972, keyed to announcement date RDQ; pre-1972, quarter ending at least 4 months prior) / market equity (CRSP) at end of month t-1. Requires the corresponding fiscal quarter end within 6 months prior to formation and the announcement date after the fiscal quarter end. Firms with nonpositive earnings excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly IBQ`, `Compustat quarterly earnings announcement date (RDQ)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Epq formed at the beginning of each month t, held from month t to t+11 (12 months) as the average of 12 overlapping monthly subdeciles; also 15 Me-Epq12 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high earnings yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.6 |

[^ summary table](#summary)

<a id="epq-1"></a>

### Quarterly Earnings-to-Price (1m) - `epq_1`

A higher-frequency earnings yield using the most recently announced quarterly earnings rather than annual earnings, capturing value more promptly using fresh accounting information.

**Construction**

```
Epq = income before extraordinary items (IBQ) from the most recent quarterly earnings (post-1972, keyed to announcement date RDQ; pre-1972, quarter ending at least 4 months prior) / market equity (CRSP) at end of month t-1. Requires the corresponding fiscal quarter end within 6 months prior to formation and the announcement date after the fiscal quarter end. Firms with nonpositive earnings excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly IBQ`, `Compustat quarterly earnings announcement date (RDQ)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Epq formed at the beginning of each month t, held for 1 month (current month t); also 15 Me-Epq1 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - cheap (high earnings yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.6 |

[^ summary table](#summary)

<a id="epq-6"></a>

### Quarterly Earnings-to-Price (6m) - `epq_6`

A higher-frequency earnings yield using the most recently announced quarterly earnings rather than annual earnings, capturing value more promptly using fresh accounting information.

**Construction**

```
Epq = income before extraordinary items (IBQ) from the most recent quarterly earnings (post-1972, keyed to announcement date RDQ; pre-1972, quarter ending at least 4 months prior) / market equity (CRSP) at end of month t-1. Requires the corresponding fiscal quarter end within 6 months prior to formation and the announcement date after the fiscal quarter end. Firms with nonpositive earnings excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly IBQ`, `Compustat quarterly earnings announcement date (RDQ)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Epq formed at the beginning of each month t, held from month t to t+5 (6 months) as the average of 6 overlapping monthly subdeciles; also 15 Me-Epq6 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - cheap (high earnings yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.6 |

[^ summary table](#summary)

<a id="emq-12"></a>

### Quarterly Enterprise Multiple (12m) - `emq_12`

Higher-frequency enterprise multiple using the latest quarterly operating income and current market value/balance sheet items.

**Construction**

```
Emq = enterprise value / operating income before depreciation (OIBDPQ) for the latest fiscal quarter ending at least 4 months ago. Enterprise value = market equity (CRSP, end of month t-1) + total debt (DLCQ + DLTTQ) + preferred stock (PSTKQ) - cash and short-term investments (CHEQ). Firms with nonpositive enterprise value or operating income excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly OIBDPQ`, `Compustat quarterly DLCQ, DLTTQ, PSTKQ, CHEQ`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Emq formed at the beginning of each month t, held from month t to t+11 (12 months) as the average of 12 overlapping monthly subdeciles; also 15 Me-Emq12 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | Low - a low enterprise multiple (cheap relative to operating income) earns a value premium |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.12 |

[^ summary table](#summary)

<a id="emq-1"></a>

### Quarterly Enterprise Multiple (1m) - `emq_1`

Higher-frequency enterprise multiple using the latest quarterly operating income and current market value/balance sheet items.

**Construction**

```
Emq = enterprise value / operating income before depreciation (OIBDPQ) for the latest fiscal quarter ending at least 4 months ago. Enterprise value = market equity (CRSP, end of month t-1) + total debt (DLCQ + DLTTQ) + preferred stock (PSTKQ) - cash and short-term investments (CHEQ). Firms with nonpositive enterprise value or operating income excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly OIBDPQ`, `Compustat quarterly DLCQ, DLTTQ, PSTKQ, CHEQ`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Emq formed at the beginning of each month t, held for 1 month (current month t); also 15 Me-Emq1 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - a low enterprise multiple (cheap relative to operating income) earns a value premium |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.12 |

[^ summary table](#summary)

<a id="emq-6"></a>

### Quarterly Enterprise Multiple (6m) - `emq_6`

Higher-frequency enterprise multiple using the latest quarterly operating income and current market value/balance sheet items.

**Construction**

```
Emq = enterprise value / operating income before depreciation (OIBDPQ) for the latest fiscal quarter ending at least 4 months ago. Enterprise value = market equity (CRSP, end of month t-1) + total debt (DLCQ + DLTTQ) + preferred stock (PSTKQ) - cash and short-term investments (CHEQ). Firms with nonpositive enterprise value or operating income excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly OIBDPQ`, `Compustat quarterly DLCQ, DLTTQ, PSTKQ, CHEQ`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Emq formed at the beginning of each month t, held from month t to t+5 (6 months) as the average of 6 overlapping monthly subdeciles; also 15 Me-Emq6 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | Low - a low enterprise multiple (cheap relative to operating income) earns a value premium |
| **Series starts** | January 1976 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.12 |

[^ summary table](#summary)

<a id="ocpq-1"></a>

### Quarterly Operating Cash Flow-to-Price (1m) - `ocpq_1`

Higher-frequency operating cash flow yield using the latest quarterly operating cash flow relative to current market value; the document constructs only a 1-month holding-period version.

**Construction**

```
Ocpq = quarterly operating cash flow for the latest fiscal quarter ending at least 4 months ago / market equity (CRSP) at end of month t-1. Operating cash flow = quarterly change in year-to-date funds from operations (FOPTY) minus change in quarterly working capital (WCAPQ) prior to 1988; quarterly change in year-to-date net cash flow from operating activities (OANCFY) from 1988 onward. Firms with nonpositive operating cash flows excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly FOPTY, WCAPQ (pre-1988)`, `Compustat quarterly OANCFY (1988+)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Ocpq formed at the beginning of each month t, held for 1 month (current month t); also 15 Me-Ocpq1 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - cheap (high operating-cash-flow yield) stocks earn a value premium |
| **Series starts** | January 1985 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.16 |

[^ summary table](#summary)

<a id="spq-12"></a>

### Quarterly Sales-to-Price (12m) - `spq_12`

Higher-frequency sales yield using the most recently announced quarterly sales relative to current market value.

**Construction**

```
Spq = quarterly sales (SALEQ) from the most recent quarterly earnings announcement (post-1972, keyed to RDQ; pre-1972, quarter ending at least 4 months prior) / market equity (CRSP) at end of month t-1. Requires the fiscal quarter end within 6 months prior to formation and the announcement date after the fiscal quarter end. Firms with nonpositive sales excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly SALEQ`, `Compustat quarterly earnings announcement date (RDQ)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Spq formed at the beginning of each month t, held from month t to t+11 (12 months) as the average of 12 overlapping monthly subdeciles; also 15 Me-Spq12 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high sales yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.14 |

[^ summary table](#summary)

<a id="spq-1"></a>

### Quarterly Sales-to-Price (1m) - `spq_1`

Higher-frequency sales yield using the most recently announced quarterly sales relative to current market value.

**Construction**

```
Spq = quarterly sales (SALEQ) from the most recent quarterly earnings announcement (post-1972, keyed to RDQ; pre-1972, quarter ending at least 4 months prior) / market equity (CRSP) at end of month t-1. Requires the fiscal quarter end within 6 months prior to formation and the announcement date after the fiscal quarter end. Firms with nonpositive sales excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly SALEQ`, `Compustat quarterly earnings announcement date (RDQ)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Spq formed at the beginning of each month t, held for 1 month (current month t); also 15 Me-Spq1 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - cheap (high sales yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.14 |

[^ summary table](#summary)

<a id="spq-6"></a>

### Quarterly Sales-to-Price (6m) - `spq_6`

Higher-frequency sales yield using the most recently announced quarterly sales relative to current market value.

**Construction**

```
Spq = quarterly sales (SALEQ) from the most recent quarterly earnings announcement (post-1972, keyed to RDQ; pre-1972, quarter ending at least 4 months prior) / market equity (CRSP) at end of month t-1. Requires the fiscal quarter end within 6 months prior to formation and the announcement date after the fiscal quarter end. Firms with nonpositive sales excluded.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly SALEQ`, `Compustat quarterly earnings announcement date (RDQ)`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Spq formed at the beginning of each month t, held from month t to t+5 (6 months) as the average of 6 overlapping monthly subdeciles; also 15 Me-Spq6 portfolios |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - cheap (high sales yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.14 |

[^ summary table](#summary)

<a id="sp"></a>

### Sales-to-Price - `sp`

Value measure comparing total sales/revenue to market value; less affected by accounting accruals than earnings-based measures. High sales yield (cheap) stocks are expected to earn a value premium.

**Construction**

```
Sp = sales (SALE) for fiscal year ending in calendar year t-1 / market equity (CRSP) at end of December of t-1. Firms with nonpositive sales excluded; multiple share classes merged.
```

| | |
|---|---|
| **Inputs** | `Compustat annual SALE`, `CRSP market equity` |
| **Portfolio sort** | Deciles on Sp formed at the end of June each year t; also 15 Me-Sp portfolios |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | High - cheap (high sales yield) stocks earn a value premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.2.13 |

[^ summary table](#summary)
