"""Smoke tests: every view must render without raising.

    pip install pytest
    pytest tests/

Streamlit Cloud installs the newest versions of everything in
requirements.txt, so the app gets silently upgraded underneath it. Twice now a
pandas release has broken a code path that only runs after a factor is
selected, which is exactly the path a casual check never reaches. These tests
select factors and walk the widgets, so that class of breakage shows up here
instead of in production.

To check against the versions the cloud would install:

    python -m venv .venv-latest
    .venv-latest/Scripts/pip install -U -r requirements.txt pytest
    .venv-latest/Scripts/python -m pytest tests/
"""

import os
import sys

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(REPO, "app.py")

if REPO not in sys.path:
    sys.path.insert(0, REPO)


def run_app():
    """Load the app at the repo root so its relative data/ paths resolve."""
    cwd = os.getcwd()
    os.chdir(REPO)
    try:
        at = AppTest.from_file(APP, default_timeout=900)
        at.run()
        return at
    finally:
        os.chdir(cwd)


def assert_clean(at, label):
    if at.exception:
        detail = "\n".join(
            "{}: {}".format(e.type, e.message) for e in at.exception
        )
        pytest.fail("{} raised:\n{}".format(label, detail))


@pytest.fixture(scope="module")
def app():
    return run_app()


def test_loads(app):
    assert_clean(app, "initial load")
    assert app.sidebar.radio[0].options == [
        "Portfolio Analysis",
        "Metric Reference",
        "Factor Model Alphas",
    ]


def test_metric_reference_lists_every_anomaly():
    at = run_app()
    at.sidebar.radio[0].set_value("Metric Reference").run()
    assert_clean(at, "metric reference")

    counts = {m.label: int(m.value) for m in at.metric}
    assert sum(counts.values()) == 201, counts

    # the big table holds one row per anomaly
    biggest = max(len(frame.value) for frame in at.dataframe)
    assert biggest == 201


def test_metric_reference_search():
    at = run_app()
    at.sidebar.radio[0].set_value("Metric Reference").run()
    at.text_input[0].set_value("accrual").run()
    assert_clean(at, "search")
    assert any("of 201 anomalies" in c.value for c in at.caption)


def test_factor_model_alphas_roe():
    """The q-factor model must absorb a profitability sort.

    Pinning the economics, not just "it did not crash": the ROE high-minus-low
    spread should be strongly positive, load about 1 on the profitability
    factor, and see its alpha collapse once that factor is in the model.
    """
    at = run_app()
    at.sidebar.radio[0].set_value("Factor Model Alphas").run()
    assert_clean(at, "factor model alphas")

    category = [o for o in at.selectbox[0].options if "Profitability" in str(o)]
    at.selectbox[0].set_value(category[0]).run()
    roe = [o for o in at.selectbox[1].options if str(o).startswith("roe_1 ")]
    at.selectbox[1].set_value(roe[0]).run()
    assert_clean(at, "select roe_1")

    tables = {}
    for frame in at.dataframe:
        columns = list(getattr(frame.value, "columns", []))
        if "t(alpha)" in columns:
            tables["models"] = frame.value
        if "t(Beta)" in columns:
            tables["loadings"] = frame.value

    models = tables["models"].set_index("Model")
    raw = models.loc["Raw (no model)"]
    assert raw["Alpha (% p.a.)"] > 5, raw
    assert raw["t(alpha)"] > 4, raw

    q = models.loc["q-factor (HXZ 2015)"]
    assert q["Alpha (% p.a.)"] < raw["Alpha (% p.a.)"] / 3, models
    assert q["R²"] > 0.5, models

    loadings = tables["loadings"].set_index("Factor")
    assert 0.8 < loadings.loc["Profitability", "Beta"] < 1.5, loadings
    assert loadings.loc["Profitability", "t(Beta)"] > 10, loadings


def test_portfolio_analysis_with_a_factor_selected():
    """The path that a load-the-page check never reaches."""
    at = run_app()

    index, option = None, None
    for i, widget in enumerate(at.sidebar.multiselect):
        hits = [o for o in widget.options if "Return on Equity" in str(o)]
        if hits:
            index, option = i, hits[0]
            break
    assert index is not None, "no Return on Equity option in any group"

    at.sidebar.multiselect[index].set_value([option]).run()
    assert_clean(at, "one factor selected")
    assert not at.warning, [w.value for w in at.warning]

    headings = [s.value for s in at.subheader]
    for expected in ["Total Return Performance", "Rolling Statistics Analysis",
                     "Market Relative Statistics", "Portfolio Statistics"]:
        assert expected in headings, headings

    # move the analysis window - this is where pd.date_range(freq='M') used to blow up
    at.date_input[0].set_value(pd.Timestamp("1990-01-01").date()).run()
    assert_clean(at, "start date changed")
    at.slider[0].set_value(36).run()
    assert_clean(at, "rolling window changed")


def test_multifactor_portfolio_weights():
    at = run_app()
    picked = 0
    for i, widget in enumerate(at.sidebar.multiselect):
        if picked >= 2 or not widget.options:
            continue
        at.sidebar.multiselect[i].set_value([widget.options[0]])
        picked += 1
    at.run()
    assert_clean(at, "two groups selected")

    at.sidebar.checkbox[0].set_value(True).run()
    assert_clean(at, "weights enabled")
    assert at.sidebar.number_input, "no weight inputs appeared"

    at.sidebar.number_input[0].set_value(0.75).run()
    assert_clean(at, "weight changed")
