# References

## The q-factor papers

These four papers are the library itself: the factor models, the replication
study the testing portfolios come from, and the factor-selection work behind
them. Citations verified against Crossref and the authors' own reference list.

| Paper | Journal | DOI |
|---|---|---|
| Hou, K., C. Xue and L. Zhang (2015), "Digesting Anomalies: An Investment Approach" | *Review of Financial Studies* 28(3), 650-705 | [10.1093/rfs/hhu068](https://doi.org/10.1093/rfs/hhu068) |
| Hou, K., H. Mo, C. Xue and L. Zhang (2019), "Which Factors?" | *Review of Finance* 23(1), 1-35 | [10.1093/rof/rfy032](https://doi.org/10.1093/rof/rfy032) |
| Hou, K., C. Xue and L. Zhang (2020), "Replicating Anomalies" | *Review of Financial Studies* 33(5), 2019-2133 | [10.1093/rfs/hhy131](https://doi.org/10.1093/rfs/hhy131) |
| Hou, K., H. Mo, C. Xue and L. Zhang (2021), "An Augmented q-Factor Model with Expected Growth" | *Review of Finance* 25(1), 1-41 | [10.1093/rof/rfaa004](https://doi.org/10.1093/rof/rfaa004) |

**Digesting Anomalies (2015)** introduces the q-factor model: market, size,
investment and profitability. The economic story is q-theory of investment.
Firms invest heavily when their cost of capital is low, so high-investment firms
should earn lower returns; and for a given level of investment, more profitable
firms must be discounted at a higher rate, so they should earn more.

**Which Factors? (2019)** compares the q-factor model against the other
workhorse models and argues the investment and profitability factors do the work
that separate value, momentum and quality factors are usually asked to do.

**Replicating Anomalies (2020)** rebuilds 452 published anomalies on one
consistent data pipeline, with NYSE breakpoints and value weighting throughout.
Most stop being significant. The 201 anomalies shipped here are the survivors
plus a set kept for continuity and comparison - see
[METRICS.md](METRICS.md) for the exact selection rule.

**An Augmented q-Factor Model (2021)** adds a fifth factor, expected growth,
estimated by forecasting future investment-to-assets growth. This is the q5
model, and the `eg_1`, `eg_6` and `eg_12` portfolios in the profitability
category are its sorting variable.

## The technical documents

The construction detail in this repository's metric pages - every formula,
every Compustat item, every breakpoint - comes from the library's own technical
document, not from the journal articles:

> Hou, K., C. Xue and L. Zhang (July 2026), "Technical Document: Testing
> Portfolios", global-q.org.
> <https://global-q.org/testingportfolios.html>

A companion "Technical Document: Factors" on
<https://global-q.org/factors.html> documents the factor returns used by the
Factor Model Alphas view.

## Papers credited for individual anomalies

The technical document names an originating paper for 89 of the 201 anomalies. Those credits are reproduced below exactly as the document gives them - author and year, without full bibliographic detail, because that is all the source provides. The remaining 112 anomalies carry no named originating paper in the document and are marked as such in the metric pages.

| Credited paper | Anomalies |
|---|---:|
| Abarbanell and Bushee (1998) | 2 |
| Ang, Hodrick, Xing, and Zhang (2006) | 2 |
| Asness and Frazzini (2013) | 1 |
| Ball, Gerakos, Linnainmaa, and Nikolaev (2015) | 1 |
| Ball, Gerakos, Linnainmaa, and Nikolaev (2016) | 1 |
| Barth, Elliott, and Finn (1999) | 1 |
| Boudoukh, Michaely, Richardson, and Roberts (2007) | 2 |
| Campbell, Hilscher, and Szilagyi (2008) | 1 |
| Chan, Jegadeesh, and Lakonishok (1996) | 5 |
| Cohen and Frazzini (2008) | 3 |
| Cohen and Lou (2012) | 2 |
| Da and Warachka (2011) | 1 |
| De Bondt and Thaler (1985) | 3 |
| Dechow, Sloan, and Soliman (2004) | 1 |
| Dechow, Sloan, and Sweeney (1995) | 1 |
| Dechow, Sloan, and Sweeney (1995) (Dac); percent-scaling per Hafzalla, Lundholm, and Van Winkle (2011) | 1 |
| Eisfeldt and Papanikolaou (2013) | 2 |
| Fama and French (2015) | 1 |
| Foster, Olsen, and Shevlin (1984) | 2 |
| Francis, LaFond, Olsson, and Schipper (2004) | 2 |
| Frankel and Lee (1998) | 2 |
| Gao and Ritter (2010) [NASDAQ volume adjustment]; Hou, Xue, and Zhang (2020), "Replicating Anomalies" | 1 |
| Hafzalla, Lundholm, and Van Winkle (2011) | 2 |
| Hawkins, Chamberlin, and Daniel (1984) | 3 |
| Heston and Sadka (2008) | 8 |
| Hou and Robinson (2006) | 1 |
| Hou, Mo, Xue, and Zhang (2021), "An Augmented q-Factor Model with Expected Growth", Review of Finance | 3 |
| Hou, Xue, and Zhang (2015) | 5 |
| Hou, Xue, and Zhang (2015), q-factor model | 1 |
| Hou, Xue, and Zhang (2015), q-factor model; Hou, Xue, and Zhang (2020), "Replicating Anomalies" | 1 |
| Jegadeesh and Livnat (2006) | 1 |
| Kelly and Jiang (2014) | 1 |
| Li (2011) | 1 |
| Menzly and Ozbas (2010) | 5 |
| Moskowitz and Grinblatt (1999) | 3 |
| Penman, Richardson, and Tuna (2007) | 1 |
| Piotroski (2000) | 3 |
| Richardson, Sloan, Soliman, and Tuna (2005) | 9 |
| Sloan (1996) (pre-1988 balance-sheet method); Hribar and Collins (2002) (post-1988 cash-flow method) | 1 |
| Thomas and Zhang (2011) | 1 |
| Tuzel (2010) | 1 |

## Data

| | |
|---|---|
| Testing portfolios | <https://global-q.org/testingportfolios.html> |
| Factor returns | <https://global-q.org/factors.html> |
| Terms of use | The library is free for academic and non-commercial use; check the site before redistributing. |

---

*Generated by `scripts/build_docs.py`.*
