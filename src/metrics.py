"""Access to the metric catalog.

The catalog is a machine-readable rendering of the variable definitions in

    Hou, K., C. Xue and L. Zhang (July 2026), "Technical Document: Testing
    Portfolios", global-q.org,

which documents the testing portfolios of Hou, Xue and Zhang (2020),
"Replicating Anomalies", Review of Financial Studies 33(5), 2019-2133.

Each entry describes one anomaly: what it measures, how it is built, the
inputs it needs, how the portfolios are sorted, which end of the sort is
expected to win, and the paper the technical document credits.
"""

import json
import os

import pandas as pd
import streamlit as st

CATALOG_FILENAME = "metrics_catalog.json"

CATEGORY_LABELS = {
    "momentum": "Momentum",
    "value-growth": "Value-versus-Growth",
    "investment": "Investment",
    "profitability": "Profitability",
    "intangibles": "Intangibles",
    "frictions": "Trading Frictions",
}

# Columns shown in the reference table, in order.
TABLE_COLUMNS = [
    "code",
    "name",
    "category_label",
    "definition",
    "formula",
    "inputs_text",
    "direction",
    "rebalance",
    "holding_period",
    "sort",
    "start",
    "source_paper",
    "doc_section",
]

COLUMN_LABELS = {
    "code": "Code",
    "name": "Metric",
    "category_label": "Category",
    "definition": "What it measures",
    "formula": "Construction",
    "inputs_text": "Inputs",
    "direction": "Which end wins",
    "rebalance": "Rebalance",
    "holding_period": "Holding period",
    "sort": "Portfolio sort",
    "start": "Series starts",
    "source_paper": "Credited paper",
    "doc_section": "Doc section",
}


@st.cache_data
def load_catalog(base_path="data"):
    """Load the catalog. Returns (metrics_list, conventions_dict)."""
    path = os.path.join(base_path, CATALOG_FILENAME)
    if not os.path.exists(path):
        return [], {}
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload.get("metrics", []), payload.get("conventions", {})


@st.cache_data
def catalog_frame(base_path="data"):
    """The catalog as a DataFrame, with display-ready helper columns."""
    metrics, _ = load_catalog(base_path)
    if not metrics:
        return pd.DataFrame(columns=TABLE_COLUMNS)

    df = pd.DataFrame(metrics)
    df["category_label"] = df["category"].map(CATEGORY_LABELS).fillna(df["category"])
    df["inputs_text"] = df["inputs"].apply(
        lambda value: "; ".join(value) if isinstance(value, list) else str(value)
    )
    for column in TABLE_COLUMNS:
        if column not in df.columns:
            df[column] = ""
    return df


def build_index(base_path="data"):
    """{code: entry} lookup."""
    metrics, _ = load_catalog(base_path)
    return {entry["code"]: entry for entry in metrics}


def get_metric(code, base_path="data"):
    """Catalog entry for an anomaly code, or None.

    Accepts either the bare code ('roe_1') or the two-way-sorted factor key
    ('me_roe_1') used by the data files.
    """
    index = build_index(base_path)
    if code in index:
        return index[code]
    if code.startswith("me_") and code[3:] in index:
        return index[code[3:]]
    return None


def display_name(code, fallback=None, base_path="data"):
    """Human-readable name for a code, falling back to the code itself."""
    entry = get_metric(code, base_path)
    if entry:
        return entry.get("name", code)
    return fallback if fallback is not None else code


def summary_line(code, base_path="data"):
    """One-line description used in tooltips and captions."""
    entry = get_metric(code, base_path)
    if not entry:
        return ""
    return entry.get("definition", "")


def search(query="", categories=None, base_path="data"):
    """Filter the catalog by free text and category.

    The text match runs over code, name, definition, construction and the
    credited paper, so 'accrual', 'Sloan' and 'oa' all find operating accruals.
    """
    df = catalog_frame(base_path)
    if df.empty:
        return df

    if categories:
        df = df[df["category"].isin(categories)]

    query = (query or "").strip().lower()
    if query:
        haystack = (
            df["code"].astype(str)
            + " " + df["name"].astype(str)
            + " " + df["definition"].astype(str)
            + " " + df["formula"].astype(str)
            + " " + df["source_paper"].astype(str)
            + " " + df["inputs_text"].astype(str)
        ).str.lower()
        df = df[haystack.str.contains(query, regex=False)]

    return df.sort_values(["category_label", "name"]).reset_index(drop=True)


def category_counts(base_path="data"):
    """Anomaly count per category, for the overview strip."""
    df = catalog_frame(base_path)
    if df.empty:
        return pd.DataFrame(columns=["Category", "Anomalies"])
    counts = (
        df.groupby("category_label")["code"]
        .count()
        .reset_index()
        .rename(columns={"category_label": "Category", "code": "Anomalies"})
    )
    return counts.sort_values("Anomalies", ascending=False).reset_index(drop=True)
