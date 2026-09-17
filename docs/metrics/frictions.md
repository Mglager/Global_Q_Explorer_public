# Trading Frictions

Signals built from trading and risk characteristics rather than fundamentals: size, beta, volatility, skewness, liquidity, tail risk and short-term reversal.

11 anomalies. Definitions from Kewei Hou, Chen Xue, and Lu Zhang, "Technical Document: Testing Portfolios," global-q.org, July 2026.

[<- back to the metric index](../METRICS.md)

## Summary

| Code | Metric | What it measures | Which end wins | Rebalance | Holding | Starts |
|---|---|---|---|---|---|---|
| `dtv_12` | [Dollar Trading Volume (12m)](#dtv-12) | Dollar trading volume proxies for a stock's liquidity, computed as average daily dollar volume traded over the prior six months. It is a friction/liquidity measure: more heavily traded (more liquid) stocks tend to earn lower average returns than illiquid, thinly traded stocks. | Low | monthly | 12 months | January 1967 |
| `isff_1` | [Idiosyncratic Skewness per FF3 (1m)](#isff-1) | Idiosyncratic skewness measures the asymmetry of a stock's stock-specific (non-factor) return distribution, estimated from the Fama-French 3-factor model. Stocks with high positive idiosyncratic skewness behave like lottery tickets and are typically overpriced, earning lower subsequent returns. | Low | monthly | 1 month | January 1967 |
| `isq_1` | [Idiosyncratic Skewness per q-factor Model (1m)](#isq-1) | Idiosyncratic skewness estimated relative to the Hou-Xue-Zhang q-factor model rather than the Fama-French model. As with Isff, stocks with high positive idiosyncratic skewness are lottery-like and tend to be overpriced, earning lower subsequent returns. | Low | monthly | 1 month | February 1967 |
| `ivff_1` | [Idiosyncratic Volatility per FF3 (1m)](#ivff-1) | Idiosyncratic volatility is the stock-specific (non-factor) volatility left over after removing Fama-French 3-factor exposures. This captures the idiosyncratic volatility puzzle, where stocks with high firm-specific volatility have earned anomalously low average returns. | Low | monthly | 1 month | January 1967 |
| `ivq_1` | [Idiosyncratic Volatility per q-factor Model (1m)](#ivq-1) | Idiosyncratic volatility estimated relative to the Hou-Xue-Zhang q-factor model instead of Fama-French 3. As with Ivff, stocks with high firm-specific volatility have earned anomalously low average returns (the idiosyncratic volatility puzzle). | Low | monthly | 1 month | February 1967 |
| `beta_1` | [Market Beta (1m)](#beta-1) | Market beta measures a stock's sensitivity to overall market moves, estimated from five years of monthly returns. The betting-against-beta pattern in this friction category is that low-beta stocks have earned higher risk-adjusted returns than high-beta stocks, contrary to the CAPM. | Low | monthly | 1 month | January 1967 |
| `me` | [Market Equity (Size)](#me) | Market equity is a stock's total market capitalization, used as the classic size measure. Stocks are sorted into deciles each June and held for a year; small stocks have historically earned higher average returns than large stocks (the size premium). | Low | annual (June) | 12 months | January 1967 |
| `srev` | [Short-term Reversal](#srev) | Short-term reversal sorts stocks on their return over the immediately preceding month. It captures the tendency of last month's losers to outperform last month's winners over the following month, consistent with short-term overreaction or liquidity-provision effects. | Low | monthly | 1 month | January 1967 |
| `sv_1` | [Systematic Volatility Risk (1m)](#sv-1) | Systematic volatility risk measures a stock's sensitivity (beta) to shocks in aggregate market volatility (changes in the VIX index). Stocks that hedge aggregate volatility risk (moving positively with volatility shocks) tend to earn lower average returns because investors accept lower compensation for holding this hedge. | Low | monthly | 1 month | February 1990 |
| `tail_12` | [Tail Risk (12m)](#tail-12) | Tail risk measures a stock's sensitivity to common (market-wide) tail risk, the pooled extreme-loss behavior of daily stock returns. Stocks more exposed to systematic tail risk are riskier in crash states and should command a compensating risk premium. | High | monthly | 12 months | January 1967 |
| `tv_1` | [Total Volatility (1m)](#tv-1) | Total volatility is the overall (not just idiosyncratic) volatility of a stock's daily returns. Like idiosyncratic volatility, high total volatility stocks have earned anomalously low subsequent average returns (the volatility puzzle). | Low | monthly | 1 month | January 1967 |

## Detail

<a id="dtv-12"></a>

### Dollar Trading Volume (12m) - `dtv_12`

Dollar trading volume proxies for a stock's liquidity, computed as average daily dollar volume traded over the prior six months. It is a friction/liquidity measure: more heavily traded (more liquid) stocks tend to earn lower average returns than illiquid, thinly traded stocks.

**Construction**

```
Dtv = average daily dollar trading volume (share price x shares traded) over months t-6 to t-1; minimum 50 daily observations required. NASDAQ volume is adjusted per Gao and Ritter (2010) institutional-difference divisors before averaging.
```

| | |
|---|---|
| **Inputs** | `daily share price`, `daily shares traded`, `NASDAQ volume adjustment divisor (Gao and Ritter 2010)` |
| **Portfolio sort** | NYSE deciles on prior 6-month average daily dollar volume, monthly rebalance, 12-month holding period built from 12 overlapping monthly-formed subdeciles that are averaged |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | Low - low trading volume (illiquid) stocks earn a liquidity premium |
| **Series starts** | January 1967 |
| **Credited paper** | Gao and Ritter (2010) [NASDAQ volume adjustment]; Hou, Xue, and Zhang (2020), "Replicating Anomalies" |
| **Technical document** | section 2.6.7 |

[^ summary table](#summary)

<a id="isff-1"></a>

### Idiosyncratic Skewness per FF3 (1m) - `isff_1`

Idiosyncratic skewness measures the asymmetry of a stock's stock-specific (non-factor) return distribution, estimated from the Fama-French 3-factor model. Stocks with high positive idiosyncratic skewness behave like lottery tickets and are typically overpriced, earning lower subsequent returns.

**Construction**

```
Isff = skewness of the daily residuals from regressing a stock's excess returns on the Fama and French (1993) three factors, using daily observations from month t-1; minimum 15 daily returns required.
```

| | |
|---|---|
| **Inputs** | `daily stock excess returns`, `Fama-French 3 factors (MKT, SMB, HML)` |
| **Portfolio sort** | NYSE deciles on Isff (prior-month estimate), monthly rebalance, 1-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - high positively-skewed 'lottery' stocks are overpriced and earn lower returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.6.8 |

[^ summary table](#summary)

<a id="isq-1"></a>

### Idiosyncratic Skewness per q-factor Model (1m) - `isq_1`

Idiosyncratic skewness estimated relative to the Hou-Xue-Zhang q-factor model rather than the Fama-French model. As with Isff, stocks with high positive idiosyncratic skewness are lottery-like and tend to be overpriced, earning lower subsequent returns.

**Construction**

```
Isq = skewness of the daily residuals from regressing a stock's excess returns on the Hou, Xue, and Zhang (2015) q-factors, using daily observations from month t-1; minimum 15 daily returns required.
```

| | |
|---|---|
| **Inputs** | `daily stock excess returns`, `q-factors (Hou, Xue, and Zhang 2015 model)` |
| **Portfolio sort** | NYSE deciles on Isq (prior-month estimate), monthly rebalance, 1-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - high positively-skewed 'lottery' stocks are overpriced and earn lower returns |
| **Series starts** | February 1967 |
| **Credited paper** | Hou, Xue, and Zhang (2015), q-factor model; Hou, Xue, and Zhang (2020), "Replicating Anomalies" |
| **Technical document** | section 2.6.9 |

[^ summary table](#summary)

<a id="ivff-1"></a>

### Idiosyncratic Volatility per FF3 (1m) - `ivff_1`

Idiosyncratic volatility is the stock-specific (non-factor) volatility left over after removing Fama-French 3-factor exposures. This captures the idiosyncratic volatility puzzle, where stocks with high firm-specific volatility have earned anomalously low average returns.

**Construction**

```
Ivff = residual volatility from regressing a stock's daily excess returns on the Fama-French 3 factors, using daily returns from month t-1; minimum 15 daily returns required.
```

| | |
|---|---|
| **Inputs** | `daily stock excess returns`, `Fama-French 3 factors (MKT, SMB, HML)` |
| **Portfolio sort** | NYSE deciles on Ivff (prior-month estimate), monthly rebalance, 1-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - the idiosyncratic volatility puzzle: high-IVOL stocks earn lower returns |
| **Series starts** | January 1967 |
| **Credited paper** | Ang, Hodrick, Xing, and Zhang (2006) |
| **Technical document** | section 2.6.2 |

[^ summary table](#summary)

<a id="ivq-1"></a>

### Idiosyncratic Volatility per q-factor Model (1m) - `ivq_1`

Idiosyncratic volatility estimated relative to the Hou-Xue-Zhang q-factor model instead of Fama-French 3. As with Ivff, stocks with high firm-specific volatility have earned anomalously low average returns (the idiosyncratic volatility puzzle).

**Construction**

```
Ivq = residual volatility from regressing a stock's daily excess returns on the Hou, Xue, and Zhang (2015) q-factors, using daily returns from month t-1; minimum 15 daily returns required.
```

| | |
|---|---|
| **Inputs** | `daily stock excess returns`, `q-factors (Hou, Xue, and Zhang 2015 model)` |
| **Portfolio sort** | NYSE deciles on Ivq (prior-month estimate), monthly rebalance, 1-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - the idiosyncratic volatility puzzle: high-IVOL stocks earn lower returns |
| **Series starts** | February 1967 |
| **Credited paper** | Hou, Xue, and Zhang (2015), q-factor model |
| **Technical document** | section 2.6.3 |

[^ summary table](#summary)

<a id="beta-1"></a>

### Market Beta (1m) - `beta_1`

Market beta measures a stock's sensitivity to overall market moves, estimated from five years of monthly returns. The betting-against-beta pattern in this friction category is that low-beta stocks have earned higher risk-adjusted returns than high-beta stocks, contrary to the CAPM.

**Construction**

```
Beta (β) is estimated from a regression of monthly stock returns on the market return using months t-60 through t-1; minimum 24 monthly returns required, using only returns flagged 'CR' or 'MP' (compounded from prior month-end to current month-end).
```

| | |
|---|---|
| **Inputs** | `monthly stock returns (60-month window)`, `market factor return`, `return compounding flag (CR/MP)` |
| **Portfolio sort** | NYSE deciles on beta (60-month rolling estimate), monthly rebalance, 1-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - low-beta stocks earn higher risk-adjusted returns (betting-against-beta) |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.6.6 |

[^ summary table](#summary)

<a id="me"></a>

### Market Equity (Size) - `me`

Market equity is a stock's total market capitalization, used as the classic size measure. Stocks are sorted into deciles each June and held for a year; small stocks have historically earned higher average returns than large stocks (the size premium).

**Construction**

```
Me = price x shares outstanding, from CRSP, measured at the end of June of year t.
```

| | |
|---|---|
| **Inputs** | `stock price (CRSP)`, `shares outstanding (CRSP)` |
| **Portfolio sort** | NYSE deciles on June-end Me, annual rebalance in June |
| **Rebalance** | annual (June) |
| **Holding period** | 12 months |
| **Which end wins** | Low - small stocks earn a size premium |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.6.1 |

[^ summary table](#summary)

<a id="srev"></a>

### Short-term Reversal - `srev`

Short-term reversal sorts stocks on their return over the immediately preceding month. It captures the tendency of last month's losers to outperform last month's winners over the following month, consistent with short-term overreaction or liquidity-provision effects.

**Construction**

```
Srev sort variable = a stock's return in month t-1. To be included, a stock must have a valid price at the end of month t-2 and a valid month t-1 return flagged 'CR' or 'MP' (compounded from prior month-end to current month-end).
```

| | |
|---|---|
| **Inputs** | `monthly stock return (month t-1)`, `end-of-month price validity`, `return compounding flag (CR/MP)` |
| **Portfolio sort** | NYSE deciles on month t-1 return, monthly rebalance, 1-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - short-term reversal: prior-month losers outperform prior-month winners |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.6.11 |

[^ summary table](#summary)

<a id="sv-1"></a>

### Systematic Volatility Risk (1m) - `sv_1`

Systematic volatility risk measures a stock's sensitivity (beta) to shocks in aggregate market volatility (changes in the VIX index). Stocks that hedge aggregate volatility risk (moving positively with volatility shocks) tend to earn lower average returns because investors accept lower compensation for holding this hedge.

**Construction**

```
Sv = beta_dVIX from the bivariate regression r_id = beta_i0 + beta_iMKT*MKT_d + beta_idVIX*dVIX_d + e_id, where r_id is stock i's excess return on day d, MKT_d is the market factor return, and dVIX_d is the daily change in the CBOE VIX index. Estimated using daily returns from month t-1; minimum 15 daily returns required. (VXO was used before August 2021; the series now uses VIX.)
```

| | |
|---|---|
| **Inputs** | `daily stock excess returns`, `market factor return`, `daily change in VIX (formerly VXO) index` |
| **Portfolio sort** | NYSE deciles on beta_dVIX (prior-month estimate), monthly rebalance, 1-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - stocks that hedge aggregate volatility risk earn lower average returns |
| **Series starts** | February 1990 |
| **Credited paper** | Ang, Hodrick, Xing, and Zhang (2006) |
| **Technical document** | section 2.6.5 |

[^ summary table](#summary)

<a id="tail-12"></a>

### Tail Risk (12m) - `tail_12`

Tail risk measures a stock's sensitivity to common (market-wide) tail risk, the pooled extreme-loss behavior of daily stock returns. Stocks more exposed to systematic tail risk are riskier in crash states and should command a compensating risk premium.

**Construction**

```
Common tail risk lambda_t is estimated monthly by pooling daily returns across all stocks: lambda_t = (1/K_t) * sum_k=1..K_t log(R_kt / mu_t), where mu_t is the 5th percentile of all daily returns in month t, R_kt are the K_t daily returns below mu_t. A stock's Tail is then the slope from regressing its excess returns on 1-month-lagged lambda_t over the most recent 120 months (t-120 to t-1); minimum 36 monthly observations required, using only returns flagged 'CR' or 'MP'.
```

| | |
|---|---|
| **Inputs** | `pooled daily returns of all stocks (for common tail risk lambda_t)`, `monthly stock excess returns (120-month window)`, `return compounding flag (CR/MP)` |
| **Portfolio sort** | NYSE deciles on Tail (120-month rolling slope on lagged common tail risk), monthly rebalance, 12-month holding period built from 12 overlapping monthly-formed subdeciles that are averaged |
| **Rebalance** | monthly |
| **Holding period** | 12 months |
| **Which end wins** | High - greater sensitivity to systematic tail risk earns a risk premium |
| **Series starts** | January 1967 |
| **Credited paper** | Kelly and Jiang (2014) |
| **Technical document** | section 2.6.10 |

[^ summary table](#summary)

<a id="tv-1"></a>

### Total Volatility (1m) - `tv_1`

Total volatility is the overall (not just idiosyncratic) volatility of a stock's daily returns. Like idiosyncratic volatility, high total volatility stocks have earned anomalously low subsequent average returns (the volatility puzzle).

**Construction**

```
Tv = volatility of a stock's daily returns estimated from month t-1; minimum 15 daily returns required.
```

| | |
|---|---|
| **Inputs** | `daily stock returns` |
| **Portfolio sort** | NYSE deciles on Tv (prior-month estimate), monthly rebalance, 1-month holding period |
| **Rebalance** | monthly |
| **Holding period** | 1 month |
| **Which end wins** | Low - the volatility puzzle: high total-volatility stocks earn lower subsequent returns |
| **Series starts** | January 1967 |
| **Credited paper** | Documented in Hou, Xue and Zhang (2020); no originating paper named in the technical document |
| **Technical document** | section 2.6.4 |

[^ summary table](#summary)
