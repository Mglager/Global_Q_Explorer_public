"""The two reference views: Metric Reference and Factor Model Alphas.

These are kept out of app.py so the portfolio-analysis view there stays readable.
Both views work on their own and do not need a factor to be selected first.
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src import factor_models, metrics
from src.data_loader import DataLoader
from src.visualizations import PLOT_TEMPLATE, e_COLORS, e_COLOR_SEQUENCE

CATEGORY_ORDER = [
    "momentum",
    "value-growth",
    "investment",
    "profitability",
    "intangibles",
    "frictions",
]

DOCS_BASE = "https://github.com/Mglager/Global_Q_Explorer_public/blob/main/docs"


# ---------------------------------------------------------------- charts


def spread_plot(spread_frame, title, low_label="Low quintile", high_label="High quintile"):
    """Growth of 1 unit in each leg and in the long-short spread."""
    fig = go.Figure()

    for name, column, colour, width in [
        (low_label, "low", e_COLORS["nordic_beige"], 1.2),
        (high_label, "high", e_COLORS["nordic_blue"], 1.2),
    ]:
        fig.add_trace(
            go.Scatter(
                x=spread_frame.index,
                y=(1 + spread_frame[column]).cumprod(),
                name=name,
                line=dict(color=colour, width=width),
                hovertemplate="%{y:.2f}x",
            )
        )

    fig.add_trace(
        go.Scatter(
            x=spread_frame.index,
            y=(1 + spread_frame["spread"]).cumprod(),
            name="Long-short spread",
            line=dict(color=e_COLORS["ocean_blue"], width=2.2),
            hovertemplate="%{y:.2f}x",
        )
    )

    fig.update_layout(
        PLOT_TEMPLATE["layout"],
        title=title,
        xaxis_title="Date",
        yaxis_title="Growth of 1 (log scale)",
        yaxis_type="log",
        hovermode="x unified",
        showlegend=True,
        legend=dict(
            yanchor="top", y=0.99, xanchor="left", x=0.01,
            bgcolor="rgba(255, 255, 255, 0.9)",
            bordercolor=e_COLORS["light_grey"], borderwidth=1,
            font=dict(family="Arial, sans-serif", size=10, color=e_COLORS["ocean_blue"]),
        ),
    )
    return fig


def alpha_bar(df, value_col, label_col, title, x_title):
    """Horizontal bars, coloured by sign, for the category screener."""
    frame = df.sort_values(value_col)
    colours = [
        e_COLORS["nordic_blue"] if value >= 0 else e_COLORS["nordic_red"]
        for value in frame[value_col]
    ]

    fig = go.Figure(
        go.Bar(
            x=frame[value_col],
            y=frame[label_col],
            orientation="h",
            marker=dict(color=colours),
            hovertemplate="%{y}: %{x:.2f}<extra></extra>",
        )
    )
    fig.update_layout(
        PLOT_TEMPLATE["layout"],
        title=title,
        xaxis_title=x_title,
        yaxis_title="",
        showlegend=False,
        height=max(320, 18 * len(frame)),
        margin=dict(t=50, l=220, r=40, b=50),
    )
    fig.add_vline(x=0, line=dict(color=e_COLORS["grey"], width=1))
    return fig


# ------------------------------------------------------- metric reference


def _metric_detail(entry):
    """Render one catalog entry as a detail card."""
    st.markdown("#### {}  ·  `{}`".format(entry.get("name", ""), entry.get("code", "")))
    st.write(entry.get("definition", ""))

    st.markdown("**Construction**")
    st.code(entry.get("formula", ""), language=None)

    inputs = entry.get("inputs", [])
    inputs_text = ", ".join(inputs) if isinstance(inputs, list) else str(inputs)

    end, reason = _split_direction(entry.get("direction", ""))

    detail = pd.DataFrame(
        [
            ("Inputs", inputs_text),
            ("Portfolio sort", entry.get("sort", "")),
            ("Rebalance", entry.get("rebalance", "")),
            ("Holding period", entry.get("holding_period", "")),
            ("Which end wins", "{}{}".format(end, " — {}".format(reason) if reason else "")),
            ("Series starts", entry.get("start", "")),
            ("Credited paper", entry.get("source_paper", "")),
            ("Technical document", "section {}".format(entry.get("doc_section", ""))),
        ],
        columns=["Field", "Value"],
    )
    st.dataframe(detail, hide_index=True, use_container_width=True)


def _split_direction(direction):
    text = str(direction).strip()
    lowered = text.lower()
    if lowered.startswith("high"):
        end = "High"
    elif lowered.startswith("low"):
        end = "Low"
    else:
        return "—", text
    return end, text[len(end):].lstrip(" -—–:").strip()


def render_metric_reference(base_path="data"):
    """Searchable dictionary of every anomaly in the library."""
    catalog, conventions = metrics.load_catalog(base_path)

    st.title("Metric Reference")

    if not catalog:
        st.error(
            "No metric catalog found. Expected `data/metrics_catalog.json` — "
            "see docs/UPDATING.md for how to rebuild it."
        )
        return

    st.markdown(
        "Every portfolio in this app is one of **{} anomalies** from the "
        "[global-q.org](https://global-q.org/testingportfolios.html) testing-portfolio library. "
        "Definitions below are taken from the library's own technical document.".format(len(catalog))
    )

    counts = metrics.category_counts(base_path)
    columns = st.columns(len(counts))
    for column, (_, row) in zip(columns, counts.iterrows()):
        column.metric(row["Category"], int(row["Anomalies"]))

    with st.expander("How these portfolios are built", expanded=False):
        convention_rows = [
            ("Stock sample", conventions.get("stock_sample", "—")),
            ("Sample period", conventions.get("sample_period", "—")),
            ("Breakpoints", conventions.get("breakpoints", "—")),
            ("Weighting", conventions.get("weighting", "—")),
            ("Two-way (size) sorts", conventions.get("two_way_sorts", "—")),
            ("Delisting", conventions.get("delisting_adjustment", "—")),
            ("Anomaly selection", conventions.get("anomaly_selection", "—")),
        ]
        st.dataframe(
            pd.DataFrame(convention_rows, columns=["", "Detail"]),
            hide_index=True,
            use_container_width=True,
        )
        st.caption("Source: {}".format(conventions.get("citation", "global-q.org technical document")))

    st.markdown("---")

    search_col, category_col = st.columns([2, 3])
    with search_col:
        query = st.text_input(
            "Search",
            placeholder="accrual, Sloan, profitability, roe …",
            help="Matches the code, the name, the description, the construction and the credited paper.",
        )
    with category_col:
        chosen = st.multiselect(
            "Categories",
            options=CATEGORY_ORDER,
            format_func=lambda key: metrics.CATEGORY_LABELS.get(key, key),
        )

    results = metrics.search(query, chosen or None, base_path)
    st.caption("{} of {} anomalies".format(len(results), len(catalog)))

    if results.empty:
        st.info("Nothing matched that search.")
        return

    table = results[
        ["code", "name", "category_label", "definition", "direction",
         "rebalance", "holding_period", "start", "source_paper"]
    ].rename(
        columns={
            "code": "Code",
            "name": "Metric",
            "category_label": "Category",
            "definition": "What it measures",
            "direction": "Which end wins",
            "rebalance": "Rebalance",
            "holding_period": "Holding",
            "start": "Starts",
            "source_paper": "Credited paper",
        }
    )
    st.dataframe(table, hide_index=True, use_container_width=True, height=420)

    st.download_button(
        "Download this table as CSV",
        data=table.to_csv(index=False).encode("utf-8"),
        file_name="global_q_metrics.csv",
        mime="text/csv",
    )

    st.markdown("---")
    st.subheader("Metric detail")

    options = results["code"].tolist()
    labels = dict(zip(results["code"], results["name"]))
    selected = st.selectbox(
        "Pick a metric",
        options=options,
        format_func=lambda code: "{} — {}".format(code, labels.get(code, code)),
    )
    entry = metrics.get_metric(selected, base_path)
    if entry:
        _metric_detail(entry)

    st.caption(
        "Fuller write-ups, including every formula, live in "
        "[docs/METRICS.md]({}/METRICS.md). Where the technical document names no originating "
        "paper, the **Credited paper** field says so rather than guessing one.".format(DOCS_BASE)
    )


# ---------------------------------------------------- factor model alphas


def _group_options(data_dict):
    groups = [key for key in data_dict if key != "market_portfolio"]
    return sorted(groups, key=lambda g: CATEGORY_ORDER.index(DataLoader.group_to_category(g))
                  if DataLoader.group_to_category(g) in CATEGORY_ORDER else 99)


def render_factor_models(data_dict, base_path="data"):
    """Ask whether the q-factor models explain each anomaly's long-short spread."""
    st.title("Factor Model Alphas")

    factors = DataLoader.load_q5_factors(base_path)
    if factors is None:
        st.error(
            "No q-factor return file found. Expected `data/q5_factors_monthly_<year>.csv` "
            "from global-q.org — see docs/UPDATING.md."
        )
        return

    factors = factors.set_index("date")

    st.markdown(
        "A **factor model** says a portfolio's average return is payment for taking known risks. "
        "Regress the portfolio on the factors, and whatever average return is left over is the "
        "**alpha**. An alpha near zero means the model explains the anomaly. A large alpha with a "
        "**t-statistic above about 2** means it does not — that is the interesting case."
    )
    st.caption(
        "Models: CAPM (market only); the q-factor model of Hou, Xue and Zhang (2015) — market, "
        "size, investment, profitability; and q5, which adds the expected-growth factor of "
        "Hou, Mo, Xue and Zhang (2021). Factor returns are the ones published at global-q.org."
    )

    groups = _group_options(data_dict)
    if not groups:
        st.warning("No portfolio data loaded.")
        return

    control_1, control_2, control_3 = st.columns([2, 3, 2])

    with control_1:
        group = st.selectbox(
            "Category",
            options=groups,
            format_func=lambda g: metrics.CATEGORY_LABELS.get(
                DataLoader.group_to_category(g), DataLoader.group_to_category(g)
            ),
        )

    factor_keys = sorted(data_dict[group].keys())
    code_by_key = {key: DataLoader.strip_me_prefix(key) for key in factor_keys}

    with control_2:
        factor_key = st.selectbox(
            "Anomaly",
            options=factor_keys,
            format_func=lambda key: "{} — {}".format(
                code_by_key[key],
                metrics.display_name(code_by_key[key], fallback=code_by_key[key], base_path=base_path),
            ),
        )

    with control_3:
        size_choice = st.selectbox(
            "Size group",
            options=["All three (averaged)", 1, 2, 3],
            format_func=lambda v: v if isinstance(v, str)
            else {1: "1 — micro cap", 2: "2 — small cap", 3: "3 — big cap"}[v],
        )

    entry = metrics.get_metric(code_by_key[factor_key], base_path)
    if entry:
        end, reason = _split_direction(entry.get("direction", ""))
        st.info(
            "**{}** — {}\n\nExpected winning end: **{}**{}".format(
                entry.get("name", ""),
                entry.get("definition", ""),
                end,
                " ({})".format(reason) if reason else "",
            )
        )
        default_leg = 0 if end == "High" else 1
    else:
        default_leg = 0

    leg_col, model_col, lag_col = st.columns([2, 2, 2])
    with leg_col:
        leg = st.radio(
            "Spread direction",
            options=["High − Low (Q5 − Q1)", "Low − High (Q1 − Q5)"],
            index=default_leg,
            help="Defaults to the direction the literature expects to be profitable.",
        )
    with model_col:
        model_name = st.selectbox(
            "Model for the detail below",
            options=list(factor_models.MODELS.keys()),
            index=len(factor_models.MODELS) - 1,
        )
    with lag_col:
        nw_lags = st.number_input(
            "Newey-West lags",
            min_value=0, max_value=36, value=12, step=1,
            help="Lags for the standard errors. 0 gives plain OLS.",
        )

    df = data_dict[group][factor_key]
    rank_col = DataLoader.get_factor_rank_column(df)
    rank_ME = None if isinstance(size_choice, str) else size_choice

    spread_frame = factor_models.build_spread(df, rank_col, rank_ME=rank_ME)
    if spread_frame.empty:
        st.warning("Could not build a long-short spread for this anomaly.")
        return

    if leg.startswith("Low"):
        spread_frame = spread_frame.rename(columns={"low": "high", "high": "low"})
        spread_frame["spread"] = spread_frame["high"] - spread_frame["low"]
        low_label, high_label = "High quintile (short)", "Low quintile (long)"
    else:
        low_label, high_label = "Low quintile (short)", "High quintile (long)"

    min_date = spread_frame.index.min().date()
    max_date = spread_frame.index.max().date()
    date_from, date_to = st.select_slider(
        "Sample period",
        options=[d.date() for d in spread_frame.index],
        value=(min_date, max_date),
    )
    window = spread_frame.loc[
        (spread_frame.index >= pd.Timestamp(date_from))
        & (spread_frame.index <= pd.Timestamp(date_to))
    ]
    if len(window) < 24:
        st.warning("Fewer than 24 months in that window — pick a longer period.")
        return

    spread = window["spread"]
    base = factor_models.raw_stats(spread)

    st.markdown("### The long-short spread")
    metric_cols = st.columns(4)
    metric_cols[0].metric("Return", "{:.2f}% p.a.".format(base["mean_annual_pct"]))
    metric_cols[1].metric("t-statistic", "{:.2f}".format(base["t_stat"]))
    metric_cols[2].metric("Volatility", "{:.2f}% p.a.".format(base["vol_annual_pct"]))
    metric_cols[3].metric("Sharpe", "{:.2f}".format(base["sharpe"]))

    st.plotly_chart(
        spread_plot(
            window,
            "{} — {} to {}".format(
                metrics.display_name(code_by_key[factor_key], fallback=code_by_key[factor_key],
                                     base_path=base_path),
                date_from, date_to,
            ),
            low_label=low_label,
            high_label=high_label,
        ),
        use_container_width=True,
    )

    st.markdown("### Does a factor model explain it?")
    comparison = factor_models.model_comparison(spread, factors, nw_lags=int(nw_lags))
    st.dataframe(
        comparison.style.format(
            {"Alpha (% p.a.)": "{:.2f}", "t(alpha)": "{:.2f}", "R²": "{:.2f}", "Months": "{:.0f}"},
            na_rep="—",
        ),
        hide_index=True,
        use_container_width=True,
    )
    st.caption(
        "Read down the column: if the alpha shrinks towards zero as factors are added, the model "
        "is absorbing the anomaly. If it stays large with |t| above 2, the model is not."
    )

    st.markdown("#### Factor loadings — {}".format(model_name))
    loadings = factor_models.factor_loadings(
        spread, factors, factor_models.MODELS[model_name], nw_lags=int(nw_lags)
    )
    st.dataframe(
        loadings.style.format({"Beta": "{:.3f}", "t(Beta)": "{:.2f}"}),
        hide_index=True,
        use_container_width=True,
    )

    st.markdown("---")
    st.subheader("Screen the whole category")
    st.caption(
        "Same calculation across every anomaly in **{}**, so you can see which spreads the model "
        "fails to explain. High-minus-low throughout, so a negative number means the low quintile "
        "won.".format(
            metrics.CATEGORY_LABELS.get(
                DataLoader.group_to_category(group), DataLoader.group_to_category(group)
            )
        )
    )

    if st.button("Run the screen", type="primary"):
        with st.spinner("Running regressions…"):
            screen = factor_models.screen_alphas(
                data_dict, factors, group,
                model_name=model_name, rank_ME=rank_ME, nw_lags=int(nw_lags),
                start_date=date_from, end_date=date_to,
            )

        if screen.empty:
            st.warning("No results.")
            return

        screen["Metric"] = screen["code"].apply(
            lambda code: metrics.display_name(code, fallback=code, base_path=base_path)
        )
        screen = screen[
            ["code", "Metric", "Raw return (% p.a.)", "t(raw)",
             "Alpha (% p.a.)", "t(alpha)", "R²", "Months"]
        ].rename(columns={"code": "Code"})
        screen = screen.reindex(
            screen["t(alpha)"].abs().sort_values(ascending=False).index
        ).reset_index(drop=True)

        st.dataframe(
            screen.style.format(
                {
                    "Raw return (% p.a.)": "{:.2f}", "t(raw)": "{:.2f}",
                    "Alpha (% p.a.)": "{:.2f}", "t(alpha)": "{:.2f}",
                    "R²": "{:.2f}", "Months": "{:.0f}",
                },
                na_rep="—",
            ),
            hide_index=True,
            use_container_width=True,
            height=460,
        )

        st.download_button(
            "Download the screen as CSV",
            data=screen.to_csv(index=False).encode("utf-8"),
            file_name="alpha_screen_{}_{}.csv".format(
                DataLoader.group_to_category(group), model_name.split()[0]
            ),
            mime="text/csv",
        )

        unexplained = int((screen["t(alpha)"].abs() >= 2).sum())
        st.metric(
            "Spreads the {} model leaves unexplained (|t(alpha)| ≥ 2)".format(model_name),
            "{} of {}".format(unexplained, len(screen)),
        )

        st.plotly_chart(
            alpha_bar(screen, "t(alpha)", "Metric",
                      "t(alpha) vs {}".format(model_name), "t(alpha)"),
            use_container_width=True,
        )
