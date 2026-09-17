"""Regenerate the metric documentation from data/metrics_catalog.json.

    python scripts/build_docs.py

Writes:
    docs/METRICS.md              index, conventions, how to read the files
    docs/metrics/<category>.md   one page per category, full detail per anomaly
    docs/REFERENCES.md           the papers behind the library

Nothing here talks to the network. The catalog is the single source of truth;
edit it (or re-extract it from the technical document) and re-run this.
"""

import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CATALOG = os.path.join(REPO, "data", "metrics_catalog.json")
DOCS = os.path.join(REPO, "docs")
DOCS_METRICS = os.path.join(DOCS, "metrics")

UMBRELLA_PREFIX = "Documented in Hou, Xue and Zhang (2020)"

ORDER = ["momentum", "value-growth", "investment", "profitability", "intangibles", "frictions"]

LABELS = {
    "momentum": "Momentum",
    "value-growth": "Value-versus-Growth",
    "investment": "Investment",
    "profitability": "Profitability",
    "intangibles": "Intangibles",
    "frictions": "Trading Frictions",
}

BLURBS = {
    "momentum": (
        "Signals built from recent prices, recent earnings news and the news of "
        "economically linked firms. The shared idea is that good news is priced in "
        "slowly, so past winners keep winning for a while."
    ),
    "value-growth": (
        "Signals that compare an accounting or cash-flow anchor to the market price. "
        "The shared idea is that a low price relative to fundamentals signals a higher "
        "expected return, whether because of risk or because of over-pessimism."
    ),
    "investment": (
        "Signals built from how fast the balance sheet is growing and how much of "
        "earnings is accrual rather than cash. The shared idea, from q-theory, is that "
        "firms invest more when their cost of capital is low, so heavy investors and "
        "heavy issuers earn less."
    ),
    "profitability": (
        "Signals built from the level, the change and the forecast of profitability. "
        "The shared idea, again from q-theory, is that for a given amount of "
        "investment, more profitable firms must be discounted at a higher rate."
    ),
    "intangibles": (
        "Signals built from assets that do not sit cleanly on the balance sheet - R&D, "
        "organisational capital, advertising, operating leverage - plus the return "
        "seasonality family."
    ),
    "frictions": (
        "Signals built from trading and risk characteristics rather than fundamentals: "
        "size, beta, volatility, skewness, liquidity, tail risk and short-term reversal."
    ),
}

CORE_PAPERS = """\
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

"""


def escape_cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def direction_short(direction):
    text = str(direction).strip()
    lowered = text.lower()
    if lowered.startswith("high"):
        end = "High"
    elif lowered.startswith("low"):
        end = "Low"
    else:
        return "-", text
    return end, text[len(end):].lstrip(" -\u2014\u2013:").strip()


def load():
    if not os.path.exists(CATALOG):
        sys.exit("No catalog at {} - nothing to build.".format(CATALOG))
    with open(CATALOG, encoding="utf-8") as fh:
        return json.load(fh)


def write_index(metrics, conv, by_cat):
    no_paper = sum(
        1 for m in metrics if str(m.get("source_paper", "")).startswith(UMBRELLA_PREFIX)
    )

    lines = [
        "# Metric documentation",
        "",
        "Every testing portfolio in this app is one of **{} anomalies** published at "
        "[global-q.org](https://global-q.org/testingportfolios.html). This page explains what "
        "each one measures, how it is built and where it comes from.".format(len(metrics)),
        "",
        "The definitions are taken from the library's own technical document:",
        "",
        "> {}".format(conv.get("citation", "global-q.org technical document")),
        "",
        "which documents the portfolios of Hou, Xue and Zhang (2020), *Replicating Anomalies*. "
        "Full citations are in [REFERENCES.md](REFERENCES.md).",
        "",
        "## Category pages",
        "",
        "| Category | Anomalies | What the category is about |",
        "|---|---:|---|",
    ]
    for cat in ORDER:
        lines.append("| [{}](metrics/{}.md) | {} | {} |".format(
            LABELS[cat], cat, len(by_cat.get(cat, [])), escape_cell(BLURBS[cat])))
    lines += ["| **Total** | **{}** | |".format(len(metrics)), ""]

    lines += [
        "## How the portfolios are built",
        "",
        "| | |",
        "|---|---|",
        "| **Stock sample** | {} |".format(escape_cell(conv.get("stock_sample", "-"))),
        "| **Sample period** | {} |".format(escape_cell(conv.get("sample_period", "-"))),
        "| **Breakpoints** | {} |".format(escape_cell(conv.get("breakpoints", "-"))),
        "| **Weighting** | {} |".format(escape_cell(conv.get("weighting", "-"))),
        "| **Two-way (size) sorts** | {} |".format(escape_cell(conv.get("two_way_sorts", "-"))),
        "| **Delisting** | {} |".format(escape_cell(conv.get("delisting_adjustment", "-"))),
        "",
        "### Which anomalies are included",
        "",
        escape_cell(conv.get("anomaly_selection", "-")),
        "",
        "## Reading the data files",
        "",
        "This app ships the **two-way, size-interacted** portfolios. One file per anomaly:",
        "",
        "```",
        "data/me_prof_monthly_2025/portf_me_roe_1_monthly_2025.csv",
        "     ^^^^^^^                      ^^^ ^          ^^^^",
        "     category folder              code holding   vintage",
        "                                       period",
        "```",
        "",
        "| Column | Meaning |",
        "|---|---|",
        "| `year`, `month` | Observation month |",
        "| `rank_ME` | Size group, 1 = micro-cap ... 3 = big-cap |",
        "| `rank_<CODE>` | Anomaly quintile, 1 = lowest signal ... 5 = highest |",
        "| `nstocks` | Number of stocks in that cell |",
        "| `ret_vw` | Value-weighted monthly return, **in percent** |",
        "",
        "`data/portf_me_monthly_<vintage>.csv` holds the size deciles used as the market "
        "reference, and `data/q5_factors_monthly_<vintage>.csv` holds the q5 factor returns "
        "used by the Factor Model Alphas view.",
        "",
        "### The trailing number in a code",
        "",
        "`roe_1`, `roe_6` and `roe_12` are the same signal held for 1, 6 and 12 months. A "
        "longer holding period means a slower-turning portfolio, so comparing them shows how "
        "quickly a signal decays.",
        "",
        "## Two cautions",
        "",
        "**Attribution.** The *Credited paper* field is filled in only where the technical "
        "document itself names an originating paper. For {} of the {} anomalies it does not, "
        "and those entries say so rather than guessing. Many are still well-known signals with "
        "an obvious home in the literature - book-to-market is the obvious case - but this "
        "documentation does not invent a citation the source does not make.".format(
            no_paper, len(metrics)),
        "",
        "**Direction.** The *Which end wins* field is an expected sign, not a result. The "
        "technical document mostly documents construction and not direction, so where it is "
        "silent the sign is the standard one from the literature. Use the **Factor Model "
        "Alphas** view to see what the data actually did.",
        "",
        "---",
        "",
        "*Generated by `scripts/build_docs.py` from `data/metrics_catalog.json`. "
        "See [UPDATING.md](UPDATING.md).*",
        "",
    ]

    with open(os.path.join(DOCS, "METRICS.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("wrote docs/METRICS.md")


def write_category(cat, entries, conv):
    out = [
        "# {}".format(LABELS[cat]),
        "",
        BLURBS[cat],
        "",
        "{} anomalies. Definitions from {}".format(
            len(entries),
            conv.get("citation", "the global-q.org technical document").rstrip(". ") + "."),
        "",
        "[<- back to the metric index](../METRICS.md)",
        "",
        "## Summary",
        "",
        "| Code | Metric | What it measures | Which end wins | Rebalance | Holding | Starts |",
        "|---|---|---|---|---|---|---|",
    ]
    for m in entries:
        end, _ = direction_short(m.get("direction", ""))
        out.append("| `{}` | [{}](#{}) | {} | {} | {} | {} | {} |".format(
            m["code"], escape_cell(m["name"]), m["code"].replace("_", "-"),
            escape_cell(m.get("definition", "")), end,
            escape_cell(m.get("rebalance", "-")),
            escape_cell(m.get("holding_period", "-")),
            escape_cell(m.get("start", "-"))))

    out += ["", "## Detail", ""]
    for m in entries:
        end, reason = direction_short(m.get("direction", ""))
        inputs = m.get("inputs", [])
        inputs_text = ", ".join("`{}`".format(i) for i in inputs) if isinstance(inputs, list) \
            else str(inputs)
        out += [
            '<a id="{}"></a>'.format(m["code"].replace("_", "-")),
            "",
            "### {} - `{}`".format(m["name"], m["code"]),
            "",
            m.get("definition", ""),
            "",
            "**Construction**",
            "",
            "```",
            str(m.get("formula", "")),
            "```",
            "",
            "| | |",
            "|---|---|",
            "| **Inputs** | {} |".format(escape_cell(inputs_text)),
            "| **Portfolio sort** | {} |".format(escape_cell(m.get("sort", "-"))),
            "| **Rebalance** | {} |".format(escape_cell(m.get("rebalance", "-"))),
            "| **Holding period** | {} |".format(escape_cell(m.get("holding_period", "-"))),
            "| **Which end wins** | {}{} |".format(
                end, " - {}".format(escape_cell(reason)) if reason else ""),
            "| **Series starts** | {} |".format(escape_cell(m.get("start", "-"))),
            "| **Credited paper** | {} |".format(escape_cell(m.get("source_paper", "-"))),
            "| **Technical document** | section {} |".format(escape_cell(m.get("doc_section", "-"))),
            "",
            "[^ summary table](#summary)",
            "",
        ]

    with open(os.path.join(DOCS_METRICS, "{}.md".format(cat)), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print("wrote docs/metrics/{}.md  ({} entries)".format(cat, len(entries)))


def write_references(metrics):
    counts = Counter()
    for m in metrics:
        paper = str(m.get("source_paper", "")).strip()
        if paper.startswith(UMBRELLA_PREFIX) or not paper:
            continue
        counts[paper] += 1

    named_total = sum(counts.values())

    lines = ["# References", "", CORE_PAPERS.rstrip(), "",
             "## Papers credited for individual anomalies", "",
             "The technical document names an originating paper for {} of the {} anomalies. "
             "Those credits are reproduced below exactly as the document gives them - author "
             "and year, without full bibliographic detail, because that is all the source "
             "provides. The remaining {} anomalies carry no named originating paper in the "
             "document and are marked as such in the metric pages.".format(
                 named_total, len(metrics), len(metrics) - named_total),
             "",
             "| Credited paper | Anomalies |",
             "|---|---:|"]

    for paper, n in sorted(counts.items()):
        lines.append("| {} | {} |".format(escape_cell(paper), n))

    lines += [
        "",
        "## Data",
        "",
        "| | |",
        "|---|---|",
        "| Testing portfolios | <https://global-q.org/testingportfolios.html> |",
        "| Factor returns | <https://global-q.org/factors.html> |",
        "| Terms of use | The library is free for academic and non-commercial use; "
        "check the site before redistributing. |",
        "",
        "---",
        "",
        "*Generated by `scripts/build_docs.py`.*",
        "",
    ]

    with open(os.path.join(DOCS, "REFERENCES.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("wrote docs/REFERENCES.md")


def main():
    payload = load()
    metrics = payload["metrics"]
    conv = payload.get("conventions", {})

    os.makedirs(DOCS_METRICS, exist_ok=True)

    by_cat = {}
    for m in metrics:
        by_cat.setdefault(m["category"], []).append(m)
    for cat in by_cat:
        by_cat[cat].sort(key=lambda m: m["name"])

    write_index(metrics, conv, by_cat)
    for cat in ORDER:
        write_category(cat, by_cat.get(cat, []), conv)
    write_references(metrics)
    print("\n{} metrics documented".format(len(metrics)))


if __name__ == "__main__":
    main()
