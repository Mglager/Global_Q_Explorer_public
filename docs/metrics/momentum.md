# Momentum

Signals built from recent prices, recent earnings news and the news of economically linked firms. The shared idea is that good news is priced in slowly, so past winners keep winning for a while.

43 anomalies. Definitions from Kewei Hou, Chen Xue, and Lu Zhang, "Technical Document: Testing Portfolios," global-q.org, July 2026.

[<- back to the metric index](../METRICS.md)

## Summary

| Code | Metric | What it measures | Which end wins | Rebalance | Holding | Starts |
|---|---|---|---|---|---|---|
| `resid11_12` | [11-month Residual Momentum (12m)](#resid11-12) | Eleven-month residual momentum applies the same residual-return construction as the six-month version but over the classic 11-month (12-1) formation window, isolating stock-specific momentum from factor-driven momentum over the longer horizon. | High | monthly | 12 months | January 1967 |
| `resid11_1` | [11-month Residual Momentum (1m)](#resid11-1) | Eleven-month residual momentum applies the same residual-return construction as the six-month version but over the classic 11-month (12-1) formation window, isolating stock-specific momentum from factor-driven momentum over the longer horizon. | High | monthly | 1 month | January 1967 |
| `resid11_6` | [11-month Residual Momentum (6m)](#resid11-6) | Eleven-month residual momentum applies the same residual-return construction as the six-month version but over the classic 11-month (12-1) formation window, isolating stock-specific momentum from factor-driven momentum over the longer horizon. | High | monthly | 6 months | January 1967 |
| `p52w_12` | [52-week High (12m)](#p52w-12) | The 52-week High ratio compares a stock's current price to its highest price over the trailing year. Stocks trading near their 52-week high tend to keep outperforming, consistent with investors anchoring on the high as a reference point and being slow to update as good news accumulates. | High | monthly | 12 months | January 1967 |
| `p52w_6` | [52-week High (6m)](#p52w-6) | The 52-week High ratio compares a stock's current price to its highest price over the trailing year. Stocks trading near their 52-week high tend to keep outperforming, consistent with investors anchoring on the high as a reference point and being slow to update as good news accumulates. | High | monthly | 6 months | January 1967 |
| `def_12` | [Changes in Analyst Earnings Forecasts (12m)](#def-12) | dEf captures the most recent month-over-month change in analysts' consensus EPS forecast, scaled by the average absolute forecast level, testing whether the freshest forecast revision (as opposed to Re's 6-month average) predicts near-term returns through investor underreaction. | High | monthly | 12 months | March 1976 |
| `def_1` | [Changes in Analyst Earnings Forecasts (1m)](#def-1) | dEf captures the most recent month-over-month change in analysts' consensus EPS forecast, scaled by the average absolute forecast level, testing whether the freshest forecast revision (as opposed to Re's 6-month average) predicts near-term returns through investor underreaction. | High | monthly | 1 month | March 1976 |
| `def_6` | [Changes in Analyst Earnings Forecasts (6m)](#def-6) | dEf captures the most recent month-over-month change in analysts' consensus EPS forecast, scaled by the average absolute forecast level, testing whether the freshest forecast revision (as opposed to Re's 6-month average) predicts near-term returns through investor underreaction. | High | monthly | 6 months | March 1976 |
| `abr_12` | [Cumulative Abnormal Return Around Earnings Announcement (12m)](#abr-12) | Abr captures the market's abnormal price reaction in the days immediately around a firm's quarterly earnings announcement, cumulating stock returns in excess of the broad market return from 2 days before to 1 day after the announcement. Persistently high or low abnormal announcement returns tend to continue (announcement drift). | High | monthly | 12 months | January 1972 |
| `abr_1` | [Cumulative Abnormal Return Around Earnings Announcement (1m)](#abr-1) | Abr captures the market's abnormal price reaction in the days immediately around a firm's quarterly earnings announcement, cumulating stock returns in excess of the broad market return from 2 days before to 1 day after the announcement. Persistently high or low abnormal announcement returns tend to continue (announcement drift). | High | monthly | 1 month | January 1972 |
| `abr_6` | [Cumulative Abnormal Return Around Earnings Announcement (6m)](#abr-6) | Abr captures the market's abnormal price reaction in the days immediately around a firm's quarterly earnings announcement, cumulating stock returns in excess of the broad market return from 2 days before to 1 day after the announcement. Persistently high or low abnormal announcement returns tend to continue (announcement drift). | High | monthly | 6 months | January 1972 |
| `cim_12` | [Customer Industries Momentum (12m)](#cim-12) | Customer industries momentum is the mirror image of supplier industries momentum: an industry's future return is predicted by the recent return of the industries it sells its output to (its customers), using the same BEA input-output linkages. | High | monthly (industry-to-BEA linkages reconstituted annually in June) | 12 months | January 1967 |
| `cim_1` | [Customer Industries Momentum (1m)](#cim-1) | Customer industries momentum is the mirror image of supplier industries momentum: an industry's future return is predicted by the recent return of the industries it sells its output to (its customers), using the same BEA input-output linkages. | High | monthly (industry-to-BEA linkages reconstituted annually in June) | 1 month | January 1967 |
| `cim_6` | [Customer Industries Momentum (6m)](#cim-6) | Customer industries momentum is the mirror image of supplier industries momentum: an industry's future return is predicted by the recent return of the industries it sells its output to (its customers), using the same BEA input-output linkages. | High | monthly (industry-to-BEA linkages reconstituted annually in June) | 6 months | January 1967 |
| `cm_12` | [Customer Momentum (12m)](#cm-12) | Customer momentum tests whether a supplier firm's stock underreacts to recent returns of its known corporate customers, since investors often fail to trace economic links across the supply chain; a supplier's future return is predicted by its customers' recent stock performance. | High | monthly (customer portfolios reconstituted annually in June) | 12 months | July 1979 |
| `cm_1` | [Customer Momentum (1m)](#cm-1) | Customer momentum tests whether a supplier firm's stock underreacts to recent returns of its known corporate customers, since investors often fail to trace economic links across the supply chain; a supplier's future return is predicted by its customers' recent stock performance. | High | monthly (customer portfolios reconstituted annually in June) | 1 month | July 1979 |
| `cm_6` | [Customer Momentum (6m)](#cm-6) | Customer momentum tests whether a supplier firm's stock underreacts to recent returns of its known corporate customers, since investors often fail to trace economic links across the supply chain; a supplier's future return is predicted by its customers' recent stock performance. | High | monthly (customer portfolios reconstituted annually in June) | 6 months | July 1979 |
| `ile_1` | [Industry Lead-Lag Effect in Earnings Surprises (1m)](#ile-1) | Industry lead-lag in earnings surprises is the earnings-news analogue of Ilr: it uses the average earnings surprise (Sue) of an industry's largest firms to predict the whole industry's future return, on the idea that big firms' earnings news diffuses slowly to the rest of the industry. | High | monthly | 1 month | January 1967 |
| `ilr_12` | [Industry Lead-Lag Effect in Prior Returns (12m)](#ilr-12) | Industry lead-lag in returns tests whether an industry's large, closely followed firms lead its smaller firms: the recent return of an industry's biggest 30% of firms is used to predict the return of the whole industry, capturing gradual information diffusion from large to small firms. | High | monthly | 12 months | January 1967 |
| `ilr_1` | [Industry Lead-Lag Effect in Prior Returns (1m)](#ilr-1) | Industry lead-lag in returns tests whether an industry's large, closely followed firms lead its smaller firms: the recent return of an industry's biggest 30% of firms is used to predict the return of the whole industry, capturing gradual information diffusion from large to small firms. | High | monthly | 1 month | January 1967 |
| `ilr_6` | [Industry Lead-Lag Effect in Prior Returns (6m)](#ilr-6) | Industry lead-lag in returns tests whether an industry's large, closely followed firms lead its smaller firms: the recent return of an industry's biggest 30% of firms is used to predict the return of the whole industry, capturing gradual information diffusion from large to small firms. | High | monthly | 6 months | January 1967 |
| `im_12` | [Industry Momentum (12m)](#im-12) | Industry momentum groups industries — not individual stocks — by their own recent 6-month return, testing whether industry-level return persistence, a slower-moving analogue of individual-stock momentum, predicts future industry returns. | High | monthly | 12 months | January 1967 |
| `im_1` | [Industry Momentum (1m)](#im-1) | Industry momentum groups industries — not individual stocks — by their own recent 6-month return, testing whether industry-level return persistence, a slower-moving analogue of individual-stock momentum, predicts future industry returns. | High | monthly | 1 month | January 1967 |
| `im_6` | [Industry Momentum (6m)](#im-6) | Industry momentum groups industries — not individual stocks — by their own recent 6-month return, testing whether industry-level return persistence, a slower-moving analogue of individual-stock momentum, predicts future industry returns. | High | monthly | 6 months | January 1967 |
| `nei_1` | [Number of Consecutive Quarters with Earnings Increase (1m)](#nei-1) | Nei counts how many consecutive quarters (up to eight) a firm has posted a year-over-year earnings increase, testing whether a longer streak of earnings growth — a simple persistence/quality measure — predicts continued outperformance. | High | monthly | 1 month | January 1969 |
| `r11_12` | [Prior 11-month Return (12m)](#r11-12) | R11 is a firm's raw compounded return over the prior eleven months, skipping the most recent month — the standard 12-months-minus-1 momentum formation window used in the classic momentum literature. | High | monthly | 12 months | January 1967 |
| `r11_1` | [Prior 11-month Return (1m)](#r11-1) | R11 is a firm's raw compounded return over the prior eleven months, skipping the most recent month — the standard 12-months-minus-1 momentum formation window used in the classic momentum literature. | High | monthly | 1 month | January 1967 |
| `r11_6` | [Prior 11-month Return (6m)](#r11-6) | R11 is a firm's raw compounded return over the prior eleven months, skipping the most recent month — the standard 12-months-minus-1 momentum formation window used in the classic momentum literature. | High | monthly | 6 months | January 1967 |
| `r6_12` | [Prior Six-month Return (12m)](#r6-12) | R6 is a firm's raw compounded return over the prior six months, skipping the most recent month to avoid short-term reversal contamination — the classic intermediate-horizon momentum signal: recent winners tend to keep winning. | High | monthly | 12 months | January 1967 |
| `r6_1` | [Prior Six-month Return (1m)](#r6-1) | R6 is a firm's raw compounded return over the prior six months, skipping the most recent month to avoid short-term reversal contamination — the classic intermediate-horizon momentum signal: recent winners tend to keep winning. | High | monthly | 1 month | January 1967 |
| `r6_6` | [Prior Six-month Return (6m)](#r6-6) | R6 is a firm's raw compounded return over the prior six months, skipping the most recent month to avoid short-term reversal contamination — the classic intermediate-horizon momentum signal: recent winners tend to keep winning. | High | monthly | 6 months | January 1967 |
| `rs_1` | [Revenue Surprise (1m)](#rs-1) | Revenue Surprise measures how much a firm's quarterly revenue per share deviated from its year-ago level relative to the firm's own revenue volatility, mirroring Sue's construction but using revenue instead of earnings. It captures underreaction to top-line surprises, which carry information beyond earnings. | High | monthly | 1 month | January 1967 |
| `re_1` | [Revisions in Analyst Earnings Forecasts (1m)](#re-1) | Re measures earnings surprise via the direction and magnitude of recent analyst forecast revisions, averaging the monthly percentage changes in the consensus EPS forecast (scaled by share price) over the past six months. It reflects that investors underreact to the information embedded in analysts' updated forecasts. | High | monthly | 1 month | July 1976 |
| `re_6` | [Revisions in Analyst Earnings Forecasts (6m)](#re-6) | Re measures earnings surprise via the direction and magnitude of recent analyst forecast revisions, averaging the monthly percentage changes in the consensus EPS forecast (scaled by share price) over the past six months. It reflects that investors underreact to the information embedded in analysts' updated forecasts. | High | monthly | 6 months | July 1976 |
| `sm_12` | [Segment Momentum (12m)](#sm-12) | Segment momentum tests whether a diversified conglomerate's stock price lags the returns already realized by stand-alone firms operating in the same industry segments as the conglomerate's business lines, reflecting slow diffusion of information across a firm's economically linked market segments. | High | monthly (segment portfolios reconstituted annually in June) | 12 months | July 1977 |
| `sm_1` | [Segment Momentum (1m)](#sm-1) | Segment momentum tests whether a diversified conglomerate's stock price lags the returns already realized by stand-alone firms operating in the same industry segments as the conglomerate's business lines, reflecting slow diffusion of information across a firm's economically linked market segments. | High | monthly (segment portfolios reconstituted annually in June) | 1 month | July 1977 |
| `resid6_12` | [Six-month Residual Momentum (12m)](#resid6-12) | Six-month residual momentum measures a stock's average return over the prior six months after stripping out exposure to the Fama-French three factors, scaled by the volatility of those residuals. It isolates stock-specific return persistence from momentum that is merely a byproduct of factor exposures. | High | monthly | 12 months | January 1967 |
| `resid6_6` | [Six-month Residual Momentum (6m)](#resid6-6) | Six-month residual momentum measures a stock's average return over the prior six months after stripping out exposure to the Fama-French three factors, scaled by the volatility of those residuals. It isolates stock-specific return persistence from momentum that is merely a byproduct of factor exposures. | High | monthly | 6 months | January 1967 |
| `sue_1` | [Standardized Unexpected Earnings (1m)](#sue-1) | Standardized Unexpected Earnings measures how much a firm's latest quarterly EPS surprised relative to its own recent earnings volatility, computed as the year-over-year change in split-adjusted quarterly EPS scaled by the standard deviation of that change over the past two years. It captures the post-earnings-announcement-drift anomaly: markets underreact to earnings news and prices keep drifting toward the implied value. | High | monthly | 1 month | January 1967 |
| `sue_6` | [Standardized Unexpected Earnings (6m)](#sue-6) | Standardized Unexpected Earnings measures how much a firm's latest quarterly EPS surprised relative to its own recent earnings volatility, computed as the year-over-year change in split-adjusted quarterly EPS scaled by the standard deviation of that change over the past two years. It captures the post-earnings-announcement-drift anomaly: markets underreact to earnings news and prices keep drifting toward the implied value. | High | monthly | 6 months | January 1967 |
| `sim_12` | [Supplier Industries Momentum (12m)](#sim-12) | Supplier industries momentum tests whether an industry's future return can be predicted by the recent return of the industries it purchases inputs from (its suppliers), using input-output linkages from BEA data, reflecting gradual diffusion of information along supply chains. | High | monthly (industry-to-BEA linkages reconstituted annually in June) | 12 months | January 1967 |
| `sim_1` | [Supplier Industries Momentum (1m)](#sim-1) | Supplier industries momentum tests whether an industry's future return can be predicted by the recent return of the industries it purchases inputs from (its suppliers), using input-output linkages from BEA data, reflecting gradual diffusion of information along supply chains. | High | monthly (industry-to-BEA linkages reconstituted annually in June) | 1 month | January 1967 |
| `tes_1` | [Tax Expense Surprise (1m)](#tes-1) | Tax Expense Surprise measures the year-over-year change in a firm's quarterly tax expense per share, scaled by lagged assets per share. Because tax expense follows stricter tax-accounting rules and is harder to manage than book earnings, unexpected increases in taxes paid can signal genuine, sustainable earnings strength that the market is slow to price. | High | monthly | 1 month | January 1976 |

## Detail

<a id="resid11-12"></a>

### 11-month Residual Momentum (12m) - `resid11_12`

Eleven-month residual momentum applies the same residual-return construction as the six-month version but over the classic 11-month (12-1) formation window, isolating stock-specific momentum from factor-driven momentum over the longer horizon.

**Construction**

```
epsilon11 = average residual return from month t-12 to t-2 (month t-1 skipped), divided by its standard deviation over the same window. Residuals come from a Fama-French (1993) three-factor regression of excess stock returns, re-estimated each month over the trailing 36 months (t-36 to t-1); requires a full 36-month return history and only CRSP 'CR'/'MP' flagged returns.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns (36-month estimation window)`, `Fama-French three factors (1993)`, `CRSP return flags 'CR'/'MP'` |
| **Portfolio sort** | All stocks split into deciles based on epsilon11 at the beginning of each month t; for the 12-month holding period, each month's decile return averages subdeciles initiated in prior months. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - stocks with strong recent residual returns continue to outperform |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.13 |

[^ summary table](#summary)

<a id="resid11-1"></a>

### 11-month Residual Momentum (1m) - `resid11_1`

Eleven-month residual momentum applies the same residual-return construction as the six-month version but over the classic 11-month (12-1) formation window, isolating stock-specific momentum from factor-driven momentum over the longer horizon.

**Construction**

```
epsilon11 = average residual return from month t-12 to t-2 (month t-1 skipped), divided by its standard deviation over the same window. Residuals come from a Fama-French (1993) three-factor regression of excess stock returns, re-estimated each month over the trailing 36 months (t-36 to t-1); requires a full 36-month return history and only CRSP 'CR'/'MP' flagged returns.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns (36-month estimation window)`, `Fama-French three factors (1993)`, `CRSP return flags 'CR'/'MP'` |
| **Portfolio sort** | All stocks split into deciles based on epsilon11 at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - stocks with strong recent residual returns continue to outperform |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.13 |

[^ summary table](#summary)

<a id="resid11-6"></a>

### 11-month Residual Momentum (6m) - `resid11_6`

Eleven-month residual momentum applies the same residual-return construction as the six-month version but over the classic 11-month (12-1) formation window, isolating stock-specific momentum from factor-driven momentum over the longer horizon.

**Construction**

```
epsilon11 = average residual return from month t-12 to t-2 (month t-1 skipped), divided by its standard deviation over the same window. Residuals come from a Fama-French (1993) three-factor regression of excess stock returns, re-estimated each month over the trailing 36 months (t-36 to t-1); requires a full 36-month return history and only CRSP 'CR'/'MP' flagged returns.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns (36-month estimation window)`, `Fama-French three factors (1993)`, `CRSP return flags 'CR'/'MP'` |
| **Portfolio sort** | All stocks split into deciles based on epsilon11 at the beginning of each month t; for the 6-month holding period, each month's decile return averages six subdeciles initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - stocks with strong recent residual returns continue to outperform |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.13 |

[^ summary table](#summary)

<a id="p52w-12"></a>

### 52-week High (12m) - `p52w_12`

The 52-week High ratio compares a stock's current price to its highest price over the trailing year. Stocks trading near their 52-week high tend to keep outperforming, consistent with investors anchoring on the high as a reference point and being slow to update as good news accumulates.

**Construction**

```
52w = (split-adjusted price per share at the end of month t-1) / (highest daily split-adjusted price per share over the 12-month period ending on the last day of month t-1). Only 52w values below one are used to set portfolio breakpoints, to avoid missing observations when many stocks simultaneously sit at their high (52w = 1).
```

| | |
|---|---|
| **Inputs** | `CRSP daily split-adjusted stock prices`, `CRSP monthly prices` |
| **Portfolio sort** | All stocks split into deciles based on 52w (using only 52w<1 for breakpoints) at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - stocks near their 52-week high continue to outperform |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.11 |

[^ summary table](#summary)

<a id="p52w-6"></a>

### 52-week High (6m) - `p52w_6`

The 52-week High ratio compares a stock's current price to its highest price over the trailing year. Stocks trading near their 52-week high tend to keep outperforming, consistent with investors anchoring on the high as a reference point and being slow to update as good news accumulates.

**Construction**

```
52w = (split-adjusted price per share at the end of month t-1) / (highest daily split-adjusted price per share over the 12-month period ending on the last day of month t-1). Only 52w values below one are used to set portfolio breakpoints, to avoid missing observations when many stocks simultaneously sit at their high (52w = 1).
```

| | |
|---|---|
| **Inputs** | `CRSP daily split-adjusted stock prices`, `CRSP monthly prices` |
| **Portfolio sort** | All stocks split into deciles based on 52w (using only 52w<1 for breakpoints) at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - stocks near their 52-week high continue to outperform |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.11 |

[^ summary table](#summary)

<a id="def-12"></a>

### Changes in Analyst Earnings Forecasts (12m) - `def_12`

dEf captures the most recent month-over-month change in analysts' consensus EPS forecast, scaled by the average absolute forecast level, testing whether the freshest forecast revision (as opposed to Re's 6-month average) predicts near-term returns through investor underreaction.

**Construction**

```
dEf = (f_{t-1} - f_{t-2}) / (0.5|f_{t-1}| + 0.5|f_{t-2}|), where f is the consensus mean forecast (unadjusted IBES item MEANEST) for firm i's current fiscal year earnings issued in the given month; denominated in USD; adjusted for stock splits between t-2 and t-1. Firms with zero dEf are excluded.
```

| | |
|---|---|
| **Inputs** | `IBES unadjusted file MEANEST (consensus mean EPS forecast, FY1)`, `stock split adjustment data` |
| **Portfolio sort** | All stocks (excluding zero-dEf firms) split into deciles based on prior month dEf at the beginning of each month t; for the 12-month holding period, each month's decile return averages subdeciles initiated in prior months. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - upward forecast revisions predict continued outperformance |
| **Series starts** | March 1976 |
| **Credited paper** | Hawkins, Chamberlin, and Daniel (1984) |
| **Technical document** | section 2.1.9 |

[^ summary table](#summary)

<a id="def-1"></a>

### Changes in Analyst Earnings Forecasts (1m) - `def_1`

dEf captures the most recent month-over-month change in analysts' consensus EPS forecast, scaled by the average absolute forecast level, testing whether the freshest forecast revision (as opposed to Re's 6-month average) predicts near-term returns through investor underreaction.

**Construction**

```
dEf = (f_{t-1} - f_{t-2}) / (0.5|f_{t-1}| + 0.5|f_{t-2}|), where f is the consensus mean forecast (unadjusted IBES item MEANEST) for firm i's current fiscal year earnings issued in the given month; denominated in USD; adjusted for stock splits between t-2 and t-1. Firms with zero dEf are excluded.
```

| | |
|---|---|
| **Inputs** | `IBES unadjusted file MEANEST (consensus mean EPS forecast, FY1)`, `stock split adjustment data` |
| **Portfolio sort** | All stocks (excluding zero-dEf firms) split into deciles based on prior month dEf at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - upward forecast revisions predict continued outperformance |
| **Series starts** | March 1976 |
| **Credited paper** | Hawkins, Chamberlin, and Daniel (1984) |
| **Technical document** | section 2.1.9 |

[^ summary table](#summary)

<a id="def-6"></a>

### Changes in Analyst Earnings Forecasts (6m) - `def_6`

dEf captures the most recent month-over-month change in analysts' consensus EPS forecast, scaled by the average absolute forecast level, testing whether the freshest forecast revision (as opposed to Re's 6-month average) predicts near-term returns through investor underreaction.

**Construction**

```
dEf = (f_{t-1} - f_{t-2}) / (0.5|f_{t-1}| + 0.5|f_{t-2}|), where f is the consensus mean forecast (unadjusted IBES item MEANEST) for firm i's current fiscal year earnings issued in the given month; denominated in USD; adjusted for stock splits between t-2 and t-1. Firms with zero dEf are excluded.
```

| | |
|---|---|
| **Inputs** | `IBES unadjusted file MEANEST (consensus mean EPS forecast, FY1)`, `stock split adjustment data` |
| **Portfolio sort** | All stocks (excluding zero-dEf firms) split into deciles based on prior month dEf at the beginning of each month t; for the 6-month holding period, each month's decile return averages six subdeciles initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - upward forecast revisions predict continued outperformance |
| **Series starts** | March 1976 |
| **Credited paper** | Hawkins, Chamberlin, and Daniel (1984) |
| **Technical document** | section 2.1.9 |

[^ summary table](#summary)

<a id="abr-12"></a>

### Cumulative Abnormal Return Around Earnings Announcement (12m) - `abr_12`

Abr captures the market's abnormal price reaction in the days immediately around a firm's quarterly earnings announcement, cumulating stock returns in excess of the broad market return from 2 days before to 1 day after the announcement. Persistently high or low abnormal announcement returns tend to continue (announcement drift).

**Construction**

```
Abr_i = sum_{d=-2}^{+1} (r_id - r_md), where r_id is stock i's return on day d (day 0 = earnings announcement date, Compustat quarterly RDQ) and r_md is the value-weighted return of all domestic common stocks on NYSE, Amex and Nasdaq. Cumulation runs one trading day past the announcement to capture the 1-day-delayed reaction.
```

| | |
|---|---|
| **Inputs** | `CRSP daily stock returns`, `CRSP daily value-weighted market return (NYSE/Amex/Nasdaq)`, `Compustat quarterly RDQ` |
| **Portfolio sort** | All stocks split into deciles based on most recent past Abr at the beginning of each month t; for the 12-month holding period, each month's decile return averages twelve-minus-one style subdeciles (six subdeciles per the document's stated averaging window) initiated in prior months. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - stronger positive announcement-window returns continue to drift up |
| **Series starts** | January 1972 |
| **Credited paper** | Chan, Jegadeesh, and Lakonishok (1996) |
| **Technical document** | section 2.1.2 |

[^ summary table](#summary)

<a id="abr-1"></a>

### Cumulative Abnormal Return Around Earnings Announcement (1m) - `abr_1`

Abr captures the market's abnormal price reaction in the days immediately around a firm's quarterly earnings announcement, cumulating stock returns in excess of the broad market return from 2 days before to 1 day after the announcement. Persistently high or low abnormal announcement returns tend to continue (announcement drift).

**Construction**

```
Abr_i = sum_{d=-2}^{+1} (r_id - r_md), where r_id is stock i's return on day d (day 0 = earnings announcement date, Compustat quarterly RDQ) and r_md is the value-weighted return of all domestic common stocks on NYSE, Amex and Nasdaq. Cumulation runs one trading day past the announcement to capture the 1-day-delayed reaction.
```

| | |
|---|---|
| **Inputs** | `CRSP daily stock returns`, `CRSP daily value-weighted market return (NYSE/Amex/Nasdaq)`, `Compustat quarterly RDQ` |
| **Portfolio sort** | All stocks split into deciles based on most recent past Abr at the beginning of each month t; the fiscal quarter underlying the Abr must end within 6 months prior to formation and the RDQ must be after the fiscal quarter end. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - stronger positive announcement-window returns continue to drift up |
| **Series starts** | January 1972 |
| **Credited paper** | Chan, Jegadeesh, and Lakonishok (1996) |
| **Technical document** | section 2.1.2 |

[^ summary table](#summary)

<a id="abr-6"></a>

### Cumulative Abnormal Return Around Earnings Announcement (6m) - `abr_6`

Abr captures the market's abnormal price reaction in the days immediately around a firm's quarterly earnings announcement, cumulating stock returns in excess of the broad market return from 2 days before to 1 day after the announcement. Persistently high or low abnormal announcement returns tend to continue (announcement drift).

**Construction**

```
Abr_i = sum_{d=-2}^{+1} (r_id - r_md), where r_id is stock i's return on day d (day 0 = earnings announcement date, Compustat quarterly RDQ) and r_md is the value-weighted return of all domestic common stocks on NYSE, Amex and Nasdaq. Cumulation runs one trading day past the announcement to capture the 1-day-delayed reaction.
```

| | |
|---|---|
| **Inputs** | `CRSP daily stock returns`, `CRSP daily value-weighted market return (NYSE/Amex/Nasdaq)`, `Compustat quarterly RDQ` |
| **Portfolio sort** | All stocks split into deciles based on most recent past Abr at the beginning of each month t; for the 6-month holding period, each month's decile return averages six subdeciles initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - stronger positive announcement-window returns continue to drift up |
| **Series starts** | January 1972 |
| **Credited paper** | Chan, Jegadeesh, and Lakonishok (1996) |
| **Technical document** | section 2.1.2 |

[^ summary table](#summary)

<a id="cim-12"></a>

### Customer Industries Momentum (12m) - `cim_12`

Customer industries momentum is the mirror image of supplier industries momentum: an industry's future return is predicted by the recent return of the industries it sells its output to (its customers), using the same BEA input-output linkages.

**Construction**

```
Cim = decile rank of an industry's customer-portfolio return in month t-1; the customer portfolio return weights other industries by the given industry's share of total sales to them, per the BEA Input-Output Use Table (producers' prices). The decile ranking is assigned to the industry's member stocks.
```

| | |
|---|---|
| **Inputs** | `BEA Benchmark Input-Output Accounts (Use Table)`, `Compustat/CRSP SIC or NAICS industry codes`, `CRSP monthly value-weighted industry returns` |
| **Portfolio sort** | Industries sorted into deciles based on their customer-portfolio return (Cim) in month t-1 at the beginning of each month t; decile rank assigned to member stocks; for the 12-month holding period, each month's return averages subdeciles initiated in prior months. |
| **Rebalance** | monthly (industry-to-BEA linkages reconstituted annually in June) |
| **Holding period** | 12 months |
| **Which end wins** | High - industries linked to recently strong customer industries tend to rise too |
| **Series starts** | January 1967 |
| **Credited paper** | Menzly and Ozbas (2010) |
| **Technical document** | section 2.1.18 |

[^ summary table](#summary)

<a id="cim-1"></a>

### Customer Industries Momentum (1m) - `cim_1`

Customer industries momentum is the mirror image of supplier industries momentum: an industry's future return is predicted by the recent return of the industries it sells its output to (its customers), using the same BEA input-output linkages.

**Construction**

```
Cim = decile rank of an industry's customer-portfolio return in month t-1; the customer portfolio return weights other industries by the given industry's share of total sales to them, per the BEA Input-Output Use Table (producers' prices). The decile ranking is assigned to the industry's member stocks.
```

| | |
|---|---|
| **Inputs** | `BEA Benchmark Input-Output Accounts (Use Table)`, `Compustat/CRSP SIC or NAICS industry codes`, `CRSP monthly value-weighted industry returns` |
| **Portfolio sort** | Industries sorted into deciles based on their customer-portfolio return (Cim) in month t-1 at the beginning of each month t; decile rank assigned to member stocks. Industry-to-BEA-account mapping is set each June based on fiscal-year SIC/NAICS codes. |
| **Rebalance** | monthly (industry-to-BEA linkages reconstituted annually in June) |
| **Holding period** | 1 month |
| **Which end wins** | High - industries linked to recently strong customer industries tend to rise too |
| **Series starts** | January 1967 |
| **Credited paper** | Menzly and Ozbas (2010) |
| **Technical document** | section 2.1.18 |

[^ summary table](#summary)

<a id="cim-6"></a>

### Customer Industries Momentum (6m) - `cim_6`

Customer industries momentum is the mirror image of supplier industries momentum: an industry's future return is predicted by the recent return of the industries it sells its output to (its customers), using the same BEA input-output linkages.

**Construction**

```
Cim = decile rank of an industry's customer-portfolio return in month t-1; the customer portfolio return weights other industries by the given industry's share of total sales to them, per the BEA Input-Output Use Table (producers' prices). The decile ranking is assigned to the industry's member stocks.
```

| | |
|---|---|
| **Inputs** | `BEA Benchmark Input-Output Accounts (Use Table)`, `Compustat/CRSP SIC or NAICS industry codes`, `CRSP monthly value-weighted industry returns` |
| **Portfolio sort** | Industries sorted into deciles based on their customer-portfolio return (Cim) in month t-1 at the beginning of each month t; decile rank assigned to member stocks; for the 6-month holding period, each month's return averages six subdeciles initiated in the prior six months. |
| **Rebalance** | monthly (industry-to-BEA linkages reconstituted annually in June) |
| **Holding period** | 6 months |
| **Which end wins** | High - industries linked to recently strong customer industries tend to rise too |
| **Series starts** | January 1967 |
| **Credited paper** | Menzly and Ozbas (2010) |
| **Technical document** | section 2.1.18 |

[^ summary table](#summary)

<a id="cm-12"></a>

### Customer Momentum (12m) - `cm_12`

Customer momentum tests whether a supplier firm's stock underreacts to recent returns of its known corporate customers, since investors often fail to trace economic links across the supply chain; a supplier's future return is predicted by its customers' recent stock performance.

**Construction**

```
Cm = return in month t-1 of a firm's customer portfolio, an equal-weighted portfolio (when multiple customers exist) of its identified principal customer firms, reconstituted at the end of June each year from Compustat segment-file customer disclosures matched to CRSP permnos for the fiscal year ending in calendar year t-1.
```

| | |
|---|---|
| **Inputs** | `Compustat segment files (principal customer identification)`, `CRSP permno matching`, `CRSP monthly stock returns` |
| **Portfolio sort** | Stocks sorted into quintiles based on Cm at the beginning of each month t; for the 12-month holding period, each month's quintile return averages subquintiles initiated in prior months. |
| **Rebalance** | monthly (customer portfolios reconstituted annually in June) |
| **Holding period** | 12 months |
| **Which end wins** | High - suppliers of customers whose stock rose recently tend to rise too |
| **Series starts** | July 1979 |
| **Credited paper** | Cohen and Frazzini (2008) |
| **Technical document** | section 2.1.17 |

[^ summary table](#summary)

<a id="cm-1"></a>

### Customer Momentum (1m) - `cm_1`

Customer momentum tests whether a supplier firm's stock underreacts to recent returns of its known corporate customers, since investors often fail to trace economic links across the supply chain; a supplier's future return is predicted by its customers' recent stock performance.

**Construction**

```
Cm = return in month t-1 of a firm's customer portfolio, an equal-weighted portfolio (when multiple customers exist) of its identified principal customer firms, reconstituted at the end of June each year from Compustat segment-file customer disclosures matched to CRSP permnos for the fiscal year ending in calendar year t-1.
```

| | |
|---|---|
| **Inputs** | `Compustat segment files (principal customer identification)`, `CRSP permno matching`, `CRSP monthly stock returns` |
| **Portfolio sort** | Stocks sorted into quintiles (not deciles, to avoid too few portfolios in months with duplicate Cm values) based on Cm at the beginning of each month t. |
| **Rebalance** | monthly (customer portfolios reconstituted annually in June) |
| **Holding period** | 1 month |
| **Which end wins** | High - suppliers of customers whose stock rose recently tend to rise too |
| **Series starts** | July 1979 |
| **Credited paper** | Cohen and Frazzini (2008) |
| **Technical document** | section 2.1.17 |

[^ summary table](#summary)

<a id="cm-6"></a>

### Customer Momentum (6m) - `cm_6`

Customer momentum tests whether a supplier firm's stock underreacts to recent returns of its known corporate customers, since investors often fail to trace economic links across the supply chain; a supplier's future return is predicted by its customers' recent stock performance.

**Construction**

```
Cm = return in month t-1 of a firm's customer portfolio, an equal-weighted portfolio (when multiple customers exist) of its identified principal customer firms, reconstituted at the end of June each year from Compustat segment-file customer disclosures matched to CRSP permnos for the fiscal year ending in calendar year t-1.
```

| | |
|---|---|
| **Inputs** | `Compustat segment files (principal customer identification)`, `CRSP permno matching`, `CRSP monthly stock returns` |
| **Portfolio sort** | Stocks sorted into quintiles based on Cm at the beginning of each month t; for the 6-month holding period, each month's quintile return averages six subquintiles initiated in the prior six months. |
| **Rebalance** | monthly (customer portfolios reconstituted annually in June) |
| **Holding period** | 6 months |
| **Which end wins** | High - suppliers of customers whose stock rose recently tend to rise too |
| **Series starts** | July 1979 |
| **Credited paper** | Cohen and Frazzini (2008) |
| **Technical document** | section 2.1.17 |

[^ summary table](#summary)

<a id="ile-1"></a>

### Industry Lead-Lag Effect in Earnings Surprises (1m) - `ile_1`

Industry lead-lag in earnings surprises is the earnings-news analogue of Ilr: it uses the average earnings surprise (Sue) of an industry's largest firms to predict the whole industry's future return, on the idea that big firms' earnings news diffuses slowly to the rest of the industry.

**Construction**

```
Ile = most recent past Sue (defined identically to the Sue factor: change in split-adjusted quarterly EPS from four quarters ago, scaled by its standard deviation over the prior eight quarters, minimum six) averaged across the largest 30% (by market equity) firms within a given industry, winsorized at the 1st and 99th percentiles of its distribution each month.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly EPSPXQ`, `Compustat quarterly AJEXQ`, `Compustat quarterly RDQ`, `CRSP market equity for within-industry firm-size ranking` |
| **Portfolio sort** | 45 non-financial industries (Fama-French 49 classification) sorted into 9 groups of 5 based on Ile at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - industries whose large-cap leaders posted strong earnings surprises keep rising |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.16 |

[^ summary table](#summary)

<a id="ilr-12"></a>

### Industry Lead-Lag Effect in Prior Returns (12m) - `ilr_12`

Industry lead-lag in returns tests whether an industry's large, closely followed firms lead its smaller firms: the recent return of an industry's biggest 30% of firms is used to predict the return of the whole industry, capturing gradual information diffusion from large to small firms.

**Construction**

```
Ilr = month t-1 value-weighted return of the portfolio of the largest 30% (by market equity) firms within a Fama-French 49-industry group (45 groups after excluding financials).
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns and market equity`, `Fama-French 49-industry classification (SIC-based)` |
| **Portfolio sort** | 45 non-financial industries sorted into 9 groups of 5 based on Ilr at the beginning of each month t; for the 12-month holding period, each month's portfolio return averages subportfolios initiated in prior months. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - industries whose large-cap leaders rose recently keep rising (gradual diffusion) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.15 |

[^ summary table](#summary)

<a id="ilr-1"></a>

### Industry Lead-Lag Effect in Prior Returns (1m) - `ilr_1`

Industry lead-lag in returns tests whether an industry's large, closely followed firms lead its smaller firms: the recent return of an industry's biggest 30% of firms is used to predict the return of the whole industry, capturing gradual information diffusion from large to small firms.

**Construction**

```
Ilr = month t-1 value-weighted return of the portfolio of the largest 30% (by market equity) firms within a Fama-French 49-industry group (45 groups after excluding financials).
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns and market equity`, `Fama-French 49-industry classification (SIC-based)` |
| **Portfolio sort** | 45 non-financial industries sorted into 9 groups of 5 based on Ilr at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - industries whose large-cap leaders rose recently keep rising (gradual diffusion) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.15 |

[^ summary table](#summary)

<a id="ilr-6"></a>

### Industry Lead-Lag Effect in Prior Returns (6m) - `ilr_6`

Industry lead-lag in returns tests whether an industry's large, closely followed firms lead its smaller firms: the recent return of an industry's biggest 30% of firms is used to predict the return of the whole industry, capturing gradual information diffusion from large to small firms.

**Construction**

```
Ilr = month t-1 value-weighted return of the portfolio of the largest 30% (by market equity) firms within a Fama-French 49-industry group (45 groups after excluding financials).
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns and market equity`, `Fama-French 49-industry classification (SIC-based)` |
| **Portfolio sort** | 45 non-financial industries sorted into 9 groups of 5 based on Ilr at the beginning of each month t; for the 6-month holding period, each month's portfolio return averages six subportfolios initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - industries whose large-cap leaders rose recently keep rising (gradual diffusion) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.15 |

[^ summary table](#summary)

<a id="im-12"></a>

### Industry Momentum (12m) - `im_12`

Industry momentum groups industries — not individual stocks — by their own recent 6-month return, testing whether industry-level return persistence, a slower-moving analogue of individual-stock momentum, predicts future industry returns.

**Construction**

```
Im = prior 6-month value-weighted return of a Fama-French 49-industry group (45 groups after excluding financials), from month t-6 to t-1, with month t-1 not skipped (following Moskowitz and Grinblatt 1999). Industries are grouped into 9 portfolios of 5 industries each; a portfolio's return is the simple average of its 5 member-industry returns.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns`, `Fama-French 49-industry classification (SIC-based)` |
| **Portfolio sort** | 45 non-financial industries sorted into 9 groups of 5 based on Im at the beginning of each month t; for the 12-month holding period, each month's portfolio return averages subportfolios initiated in the prior twelve months. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - industries with strong recent returns keep outperforming |
| **Series starts** | January 1967 |
| **Credited paper** | Moskowitz and Grinblatt (1999) |
| **Technical document** | section 2.1.6 |

[^ summary table](#summary)

<a id="im-1"></a>

### Industry Momentum (1m) - `im_1`

Industry momentum groups industries — not individual stocks — by their own recent 6-month return, testing whether industry-level return persistence, a slower-moving analogue of individual-stock momentum, predicts future industry returns.

**Construction**

```
Im = prior 6-month value-weighted return of a Fama-French 49-industry group (45 groups after excluding financials), from month t-6 to t-1, with month t-1 not skipped (following Moskowitz and Grinblatt 1999). Industries are grouped into 9 portfolios of 5 industries each; a portfolio's return is the simple average of its 5 member-industry returns.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns`, `Fama-French 49-industry classification (SIC-based)` |
| **Portfolio sort** | 45 non-financial industries sorted into 9 groups of 5 based on Im at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - industries with strong recent returns keep outperforming |
| **Series starts** | January 1967 |
| **Credited paper** | Moskowitz and Grinblatt (1999) |
| **Technical document** | section 2.1.6 |

[^ summary table](#summary)

<a id="im-6"></a>

### Industry Momentum (6m) - `im_6`

Industry momentum groups industries — not individual stocks — by their own recent 6-month return, testing whether industry-level return persistence, a slower-moving analogue of individual-stock momentum, predicts future industry returns.

**Construction**

```
Im = prior 6-month value-weighted return of a Fama-French 49-industry group (45 groups after excluding financials), from month t-6 to t-1, with month t-1 not skipped (following Moskowitz and Grinblatt 1999). Industries are grouped into 9 portfolios of 5 industries each; a portfolio's return is the simple average of its 5 member-industry returns.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly returns`, `Fama-French 49-industry classification (SIC-based)` |
| **Portfolio sort** | 45 non-financial industries sorted into 9 groups of 5 based on Im at the beginning of each month t; for the 6-month holding period, each month's portfolio return averages six subportfolios initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - industries with strong recent returns keep outperforming |
| **Series starts** | January 1967 |
| **Credited paper** | Moskowitz and Grinblatt (1999) |
| **Technical document** | section 2.1.6 |

[^ summary table](#summary)

<a id="nei-1"></a>

### Number of Consecutive Quarters with Earnings Increase (1m) - `nei_1`

Nei counts how many consecutive quarters (up to eight) a firm has posted a year-over-year earnings increase, testing whether a longer streak of earnings growth — a simple persistence/quality measure — predicts continued outperformance.

**Construction**

```
Nei = number of consecutive quarters (capped at 8) in which Compustat quarterly earnings (item IBQ) exceed the same fiscal quarter one year earlier. Before 1972 uses fiscal-quarter-lagged earnings; from 1972 uses RDQ-based timing, with the same 6-month staleness restriction as Sue.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly IBQ`, `Compustat quarterly RDQ` |
| **Portfolio sort** | Stocks sorted into 9 groups (Nei = 0, 1, 2, ..., 8) based on their most recent past Nei at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - longer earnings-increase streaks predict continued outperformance |
| **Series starts** | January 1969 |
| **Credited paper** | Barth, Elliott, and Finn (1999) |
| **Technical document** | section 2.1.10 |

[^ summary table](#summary)

<a id="r11-12"></a>

### Prior 11-month Return (12m) - `r11_12`

R11 is a firm's raw compounded return over the prior eleven months, skipping the most recent month — the standard 12-months-minus-1 momentum formation window used in the classic momentum literature.

**Construction**

```
R11 = compounded stock return from month t-12 to t-2 (month t-1 is skipped); requires a valid price at the end of month t-13 and at the end of month t-2, and all monthly returns from t-12 to t-2 non-missing and free of the CRSP return flag 'GP'.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns`, `CRSP monthly prices`, `CRSP return flag 'GP'` |
| **Portfolio sort** | All stocks split into deciles based on R11 at the beginning of each month t; for the 12-month holding period, each month's decile return averages subdeciles initiated in prior months. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - past winners keep outperforming (momentum) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.5 |

[^ summary table](#summary)

<a id="r11-1"></a>

### Prior 11-month Return (1m) - `r11_1`

R11 is a firm's raw compounded return over the prior eleven months, skipping the most recent month — the standard 12-months-minus-1 momentum formation window used in the classic momentum literature.

**Construction**

```
R11 = compounded stock return from month t-12 to t-2 (month t-1 is skipped); requires a valid price at the end of month t-13 and at the end of month t-2, and all monthly returns from t-12 to t-2 non-missing and free of the CRSP return flag 'GP'.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns`, `CRSP monthly prices`, `CRSP return flag 'GP'` |
| **Portfolio sort** | All stocks split into deciles based on R11 at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - past winners keep outperforming (momentum) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.5 |

[^ summary table](#summary)

<a id="r11-6"></a>

### Prior 11-month Return (6m) - `r11_6`

R11 is a firm's raw compounded return over the prior eleven months, skipping the most recent month — the standard 12-months-minus-1 momentum formation window used in the classic momentum literature.

**Construction**

```
R11 = compounded stock return from month t-12 to t-2 (month t-1 is skipped); requires a valid price at the end of month t-13 and at the end of month t-2, and all monthly returns from t-12 to t-2 non-missing and free of the CRSP return flag 'GP'.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns`, `CRSP monthly prices`, `CRSP return flag 'GP'` |
| **Portfolio sort** | All stocks split into deciles based on R11 at the beginning of each month t; for the 6-month holding period, each month's decile return averages six subdeciles initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - past winners keep outperforming (momentum) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.5 |

[^ summary table](#summary)

<a id="r6-12"></a>

### Prior Six-month Return (12m) - `r6_12`

R6 is a firm's raw compounded return over the prior six months, skipping the most recent month to avoid short-term reversal contamination — the classic intermediate-horizon momentum signal: recent winners tend to keep winning.

**Construction**

```
R6 = compounded stock return from month t-7 to t-2 (month t-1 is skipped); requires a valid price at the end of month t-8 and at the end of month t-2, and all monthly returns from t-7 to t-2 non-missing and free of the CRSP return flag 'GP'. No price-per-share screen is imposed.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns`, `CRSP monthly prices`, `CRSP return flag 'GP'` |
| **Portfolio sort** | All stocks split into deciles based on R6 at the beginning of each month t; for the 12-month holding period, each month's decile return averages subdeciles initiated in prior months per the document's stated averaging scheme. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - past winners keep outperforming (momentum) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.4 |

[^ summary table](#summary)

<a id="r6-1"></a>

### Prior Six-month Return (1m) - `r6_1`

R6 is a firm's raw compounded return over the prior six months, skipping the most recent month to avoid short-term reversal contamination — the classic intermediate-horizon momentum signal: recent winners tend to keep winning.

**Construction**

```
R6 = compounded stock return from month t-7 to t-2 (month t-1 is skipped); requires a valid price at the end of month t-8 and at the end of month t-2, and all monthly returns from t-7 to t-2 non-missing and free of the CRSP return flag 'GP'. No price-per-share screen is imposed.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns`, `CRSP monthly prices`, `CRSP return flag 'GP'` |
| **Portfolio sort** | All stocks split into deciles based on R6 at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - past winners keep outperforming (momentum) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.4 |

[^ summary table](#summary)

<a id="r6-6"></a>

### Prior Six-month Return (6m) - `r6_6`

R6 is a firm's raw compounded return over the prior six months, skipping the most recent month to avoid short-term reversal contamination — the classic intermediate-horizon momentum signal: recent winners tend to keep winning.

**Construction**

```
R6 = compounded stock return from month t-7 to t-2 (month t-1 is skipped); requires a valid price at the end of month t-8 and at the end of month t-2, and all monthly returns from t-7 to t-2 non-missing and free of the CRSP return flag 'GP'. No price-per-share screen is imposed.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns`, `CRSP monthly prices`, `CRSP return flag 'GP'` |
| **Portfolio sort** | All stocks split into deciles based on R6 at the beginning of each month t; for the 6-month holding period, each month's decile return averages six subdeciles initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - past winners keep outperforming (momentum) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.4 |

[^ summary table](#summary)

<a id="rs-1"></a>

### Revenue Surprise (1m) - `rs_1`

Revenue Surprise measures how much a firm's quarterly revenue per share deviated from its year-ago level relative to the firm's own revenue volatility, mirroring Sue's construction but using revenue instead of earnings. It captures underreaction to top-line surprises, which carry information beyond earnings.

**Construction**

```
Rs = (Sales/share_q - Sales/share_{q-4}) / SD(change in Sales/share over prior 8 quarters, minimum 6), where Sales/share = Compustat quarterly SALEQ / (CSHPRQ x AJEXQ). Before 1972 uses fiscal-quarter-lagged Rs; from 1972 uses RDQ-based timing, with the same 6-month staleness restriction as Sue.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly SALEQ`, `Compustat quarterly CSHPRQ`, `Compustat quarterly AJEXQ`, `Compustat quarterly RDQ` |
| **Portfolio sort** | All stocks split into deciles based on most recent past Rs at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - positive revenue surprises predict continued outperformance |
| **Series starts** | January 1967 |
| **Credited paper** | Jegadeesh and Livnat (2006) |
| **Technical document** | section 2.1.7 |

[^ summary table](#summary)

<a id="re-1"></a>

### Revisions in Analyst Earnings Forecasts (1m) - `re_1`

Re measures earnings surprise via the direction and magnitude of recent analyst forecast revisions, averaging the monthly percentage changes in the consensus EPS forecast (scaled by share price) over the past six months. It reflects that investors underreact to the information embedded in analysts' updated forecasts.

**Construction**

```
Re_it = (1/6) * sum_{tau=1}^{6} [(f_{it-tau} - f_{it-tau-1}) / p_{it-tau-1}], where f is the consensus mean forecast (unadjusted IBES item MEANEST) for firm i's current fiscal year earnings issued in month t-tau, and p is the prior month's unadjusted share price (item PRICE); both must be in USD; adjusted for stock splits; requires a minimum of four monthly forecast changes.
```

| | |
|---|---|
| **Inputs** | `IBES unadjusted file MEANEST (consensus mean EPS forecast, FY1)`, `IBES unadjusted file PRICE`, `stock split adjustment data` |
| **Portfolio sort** | All stocks split into deciles based on Re at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - upward analyst forecast revisions predict continued outperformance |
| **Series starts** | July 1976 |
| **Credited paper** | Chan, Jegadeesh, and Lakonishok (1996) |
| **Technical document** | section 2.1.3 |

[^ summary table](#summary)

<a id="re-6"></a>

### Revisions in Analyst Earnings Forecasts (6m) - `re_6`

Re measures earnings surprise via the direction and magnitude of recent analyst forecast revisions, averaging the monthly percentage changes in the consensus EPS forecast (scaled by share price) over the past six months. It reflects that investors underreact to the information embedded in analysts' updated forecasts.

**Construction**

```
Re_it = (1/6) * sum_{tau=1}^{6} [(f_{it-tau} - f_{it-tau-1}) / p_{it-tau-1}], where f is the consensus mean forecast (unadjusted IBES item MEANEST) for firm i's current fiscal year earnings issued in month t-tau, and p is the prior month's unadjusted share price (item PRICE); both must be in USD; adjusted for stock splits; requires a minimum of four monthly forecast changes.
```

| | |
|---|---|
| **Inputs** | `IBES unadjusted file MEANEST (consensus mean EPS forecast, FY1)`, `IBES unadjusted file PRICE`, `stock split adjustment data` |
| **Portfolio sort** | All stocks split into deciles based on Re at the beginning of each month t; for the 6-month holding period, each month's decile return averages six subdeciles initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - upward analyst forecast revisions predict continued outperformance |
| **Series starts** | July 1976 |
| **Credited paper** | Chan, Jegadeesh, and Lakonishok (1996) |
| **Technical document** | section 2.1.3 |

[^ summary table](#summary)

<a id="sm-12"></a>

### Segment Momentum (12m) - `sm_12`

Segment momentum tests whether a diversified conglomerate's stock price lags the returns already realized by stand-alone firms operating in the same industry segments as the conglomerate's business lines, reflecting slow diffusion of information across a firm's economically linked market segments.

**Construction**

```
Sm = return in month t-1 of a conglomerate's pseudoconglomerate portfolio. The pseudoconglomerate, formed at the end of June each year, is built from value-weighted stand-alone-firm portfolios in each of the conglomerate's reported segment industries (2-digit SIC), weighted by each segment's share of the conglomerate's total reported sales. Stand-alone firms have one segment representing >80% of total sales; conglomerates have aggregate reported-segment sales >80% of total sales across multiple industries.
```

| | |
|---|---|
| **Inputs** | `Compustat segment files (segment sales by 2-digit SIC)`, `Compustat annual files (total sales)`, `CRSP monthly stock returns` |
| **Portfolio sort** | Conglomerate firms split into deciles based on Sm at the beginning of each month t (starting in July); for the 12-month holding period, each month's decile return averages twelve subdeciles initiated in the prior twelve months. |
| **Rebalance** | monthly (segment portfolios reconstituted annually in June) |
| **Holding period** | 12 months |
| **Which end wins** | High - conglomerates whose segment peers rose recently keep rising (gradual information diffusion) |
| **Series starts** | July 1977 |
| **Credited paper** | Cohen and Lou (2012) |
| **Technical document** | section 2.1.14 |

[^ summary table](#summary)

<a id="sm-1"></a>

### Segment Momentum (1m) - `sm_1`

Segment momentum tests whether a diversified conglomerate's stock price lags the returns already realized by stand-alone firms operating in the same industry segments as the conglomerate's business lines, reflecting slow diffusion of information across a firm's economically linked market segments.

**Construction**

```
Sm = return in month t-1 of a conglomerate's pseudoconglomerate portfolio. The pseudoconglomerate, formed at the end of June each year, is built from value-weighted stand-alone-firm portfolios in each of the conglomerate's reported segment industries (2-digit SIC), weighted by each segment's share of the conglomerate's total reported sales. Stand-alone firms have one segment representing >80% of total sales; conglomerates have aggregate reported-segment sales >80% of total sales across multiple industries.
```

| | |
|---|---|
| **Inputs** | `Compustat segment files (segment sales by 2-digit SIC)`, `Compustat annual files (total sales)`, `CRSP monthly stock returns` |
| **Portfolio sort** | Conglomerate firms split into deciles based on Sm at the beginning of each month t (starting in July); pseudoconglomerate portfolios are reconstituted each June. |
| **Rebalance** | monthly (segment portfolios reconstituted annually in June) |
| **Holding period** | 1 month |
| **Which end wins** | High - conglomerates whose segment peers rose recently keep rising (gradual information diffusion) |
| **Series starts** | July 1977 |
| **Credited paper** | Cohen and Lou (2012) |
| **Technical document** | section 2.1.14 |

[^ summary table](#summary)

<a id="resid6-12"></a>

### Six-month Residual Momentum (12m) - `resid6_12`

Six-month residual momentum measures a stock's average return over the prior six months after stripping out exposure to the Fama-French three factors, scaled by the volatility of those residuals. It isolates stock-specific return persistence from momentum that is merely a byproduct of factor exposures.

**Construction**

```
epsilon6 = average residual return from month t-7 to t-2 (month t-1 skipped), divided by its standard deviation over the same window. Residuals come from a Fama-French (1993) three-factor regression of excess stock returns, re-estimated each month over the trailing 36 months (t-36 to t-1); requires a full 36-month return history and only CRSP 'CR'/'MP' flagged returns.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns (36-month estimation window)`, `Fama-French three factors (1993)`, `CRSP return flags 'CR'/'MP'` |
| **Portfolio sort** | All stocks split into deciles based on epsilon6 at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - stocks with strong recent residual returns continue to outperform |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.12 |

[^ summary table](#summary)

<a id="resid6-6"></a>

### Six-month Residual Momentum (6m) - `resid6_6`

Six-month residual momentum measures a stock's average return over the prior six months after stripping out exposure to the Fama-French three factors, scaled by the volatility of those residuals. It isolates stock-specific return persistence from momentum that is merely a byproduct of factor exposures.

**Construction**

```
epsilon6 = average residual return from month t-7 to t-2 (month t-1 skipped), divided by its standard deviation over the same window. Residuals come from a Fama-French (1993) three-factor regression of excess stock returns, re-estimated each month over the trailing 36 months (t-36 to t-1); requires a full 36-month return history and only CRSP 'CR'/'MP' flagged returns.
```

| | |
|---|---|
| **Inputs** | `CRSP monthly stock returns (36-month estimation window)`, `Fama-French three factors (1993)`, `CRSP return flags 'CR'/'MP'` |
| **Portfolio sort** | All stocks split into deciles based on epsilon6 at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - stocks with strong recent residual returns continue to outperform |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.1.12 |

[^ summary table](#summary)

<a id="sue-1"></a>

### Standardized Unexpected Earnings (1m) - `sue_1`

Standardized Unexpected Earnings measures how much a firm's latest quarterly EPS surprised relative to its own recent earnings volatility, computed as the year-over-year change in split-adjusted quarterly EPS scaled by the standard deviation of that change over the past two years. It captures the post-earnings-announcement-drift anomaly: markets underreact to earnings news and prices keep drifting toward the implied value.

**Construction**

```
Sue = (EPS_q - EPS_{q-4}) / SD(change in EPS over prior 8 quarters, minimum 6), where EPS = Compustat quarterly EPSPXQ / AJEXQ (split-adjusted quarterly EPS). Before 1972 uses the most recent fiscal-quarter-lagged Sue; from 1972 uses the earnings-announcement-date (RDQ) based Sue. Requires the fiscal quarter end to be within 6 months of formation and RDQ to fall after the fiscal quarter end.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly EPSPXQ`, `Compustat quarterly AJEXQ`, `Compustat quarterly RDQ` |
| **Portfolio sort** | All stocks split into deciles based on most recent past Sue at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - stronger positive earnings surprises continue to drift up |
| **Series starts** | January 1967 |
| **Credited paper** | Foster, Olsen, and Shevlin (1984) |
| **Technical document** | section 2.1.1 |

[^ summary table](#summary)

<a id="sue-6"></a>

### Standardized Unexpected Earnings (6m) - `sue_6`

Standardized Unexpected Earnings measures how much a firm's latest quarterly EPS surprised relative to its own recent earnings volatility, computed as the year-over-year change in split-adjusted quarterly EPS scaled by the standard deviation of that change over the past two years. It captures the post-earnings-announcement-drift anomaly: markets underreact to earnings news and prices keep drifting toward the implied value.

**Construction**

```
Sue = (EPS_q - EPS_{q-4}) / SD(change in EPS over prior 8 quarters, minimum 6), where EPS = Compustat quarterly EPSPXQ / AJEXQ (split-adjusted quarterly EPS). Before 1972 uses the most recent fiscal-quarter-lagged Sue; from 1972 uses the earnings-announcement-date (RDQ) based Sue. Requires the fiscal quarter end to be within 6 months of formation and RDQ to fall after the fiscal quarter end.
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly EPSPXQ`, `Compustat quarterly AJEXQ`, `Compustat quarterly RDQ` |
| **Portfolio sort** | All stocks split into deciles based on most recent past Sue at the beginning of each month t; for the 6-month holding period, each month's decile return is the average of six subdeciles initiated in the prior six months. |
| **Rebalance** | monthly |
| **Holding period** | 6 months |
| **Which end wins** | High - stronger positive earnings surprises continue to drift up |
| **Series starts** | January 1967 |
| **Credited paper** | Foster, Olsen, and Shevlin (1984) |
| **Technical document** | section 2.1.1 |

[^ summary table](#summary)

<a id="sim-12"></a>

### Supplier Industries Momentum (12m) - `sim_12`

Supplier industries momentum tests whether an industry's future return can be predicted by the recent return of the industries it purchases inputs from (its suppliers), using input-output linkages from BEA data, reflecting gradual diffusion of information along supply chains.

**Construction**

```
Sim = decile rank of an industry's supplier-portfolio return in month t-1; the supplier portfolio return weights other industries by the given industry's share of total purchases from them, per the BEA Input-Output Use Table (producers' prices). The decile ranking is assigned to the industry's member stocks.
```

| | |
|---|---|
| **Inputs** | `BEA Benchmark Input-Output Accounts (Use Table)`, `Compustat/CRSP SIC or NAICS industry codes`, `CRSP monthly value-weighted industry returns` |
| **Portfolio sort** | Industries sorted into deciles based on their supplier-portfolio return (Sim) in month t-1 at the beginning of each month t; decile rank assigned to member stocks; for the 12-month holding period, each month's return averages subdeciles initiated in prior months. |
| **Rebalance** | monthly (industry-to-BEA linkages reconstituted annually in June) |
| **Holding period** | 12 months |
| **Which end wins** | High - industries linked to recently strong supplier industries tend to rise too |
| **Series starts** | January 1967 |
| **Credited paper** | Menzly and Ozbas (2010) |
| **Technical document** | section 2.1.18 |

[^ summary table](#summary)

<a id="sim-1"></a>

### Supplier Industries Momentum (1m) - `sim_1`

Supplier industries momentum tests whether an industry's future return can be predicted by the recent return of the industries it purchases inputs from (its suppliers), using input-output linkages from BEA data, reflecting gradual diffusion of information along supply chains.

**Construction**

```
Sim = decile rank of an industry's supplier-portfolio return in month t-1; the supplier portfolio return weights other industries by the given industry's share of total purchases from them, per the BEA Input-Output Use Table (producers' prices). The decile ranking is assigned to the industry's member stocks.
```

| | |
|---|---|
| **Inputs** | `BEA Benchmark Input-Output Accounts (Use Table)`, `Compustat/CRSP SIC or NAICS industry codes`, `CRSP monthly value-weighted industry returns` |
| **Portfolio sort** | Industries sorted into deciles based on their supplier-portfolio return (Sim) in month t-1 at the beginning of each month t; decile rank assigned to member stocks. Industry-to-BEA-account mapping is set each June based on fiscal-year SIC/NAICS codes. |
| **Rebalance** | monthly (industry-to-BEA linkages reconstituted annually in June) |
| **Holding period** | 1 month |
| **Which end wins** | High - industries linked to recently strong supplier industries tend to rise too |
| **Series starts** | January 1967 |
| **Credited paper** | Menzly and Ozbas (2010) |
| **Technical document** | section 2.1.18 |

[^ summary table](#summary)

<a id="tes-1"></a>

### Tax Expense Surprise (1m) - `tes_1`

Tax Expense Surprise measures the year-over-year change in a firm's quarterly tax expense per share, scaled by lagged assets per share. Because tax expense follows stricter tax-accounting rules and is harder to manage than book earnings, unexpected increases in taxes paid can signal genuine, sustainable earnings strength that the market is slow to price.

**Construction**

```
Tes = [TaxExp/share_q - TaxExp/share_{q-4}] / Assets/share_{q-4}, where TaxExp/share = Compustat quarterly TXTQ / (CSHPRQ x AJEXQ) and Assets/share = Compustat quarterly ATQ / (CSHPRQ x AJEXQ). Firms with zero Tes are excluded (most pay no taxes).
```

| | |
|---|---|
| **Inputs** | `Compustat quarterly TXTQ`, `Compustat quarterly CSHPRQ`, `Compustat quarterly AJEXQ`, `Compustat quarterly ATQ` |
| **Portfolio sort** | All stocks (excluding zero-Tes firms) split into deciles based on Tes, computed with data from at least four months prior, at the beginning of each month t. |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | High - larger tax-expense surprises signal harder-to-manage earnings strength |
| **Series starts** | January 1976 |
| **Credited paper** | Thomas and Zhang (2011) |
| **Technical document** | section 2.1.8 |

[^ summary table](#summary)
