"""Factor-model regressions against the q-factor models.

Three models are supported, all using the factor returns published at
global-q.org:

    CAPM        R_MKT
    q-factor    R_MKT, R_ME, R_IA, R_ROE
                Hou, Xue and Zhang (2015), "Digesting Anomalies: An Investment
                Approach", Review of Financial Studies 28(3), 650-705.
    q5          R_MKT, R_ME, R_IA, R_ROE, R_EG
                Hou, Mo, Xue and Zhang (2021), "An Augmented q-Factor Model with
                Expected Growth", Review of Finance 25(1), 1-41.

The question a factor model answers here is: once the portfolio's exposure to
the market, size, investment, profitability and expected-growth factors is
priced in, is there any average return left over? That leftover is the alpha.
An anomaly that the model explains has an alpha near zero.
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm

MODELS = {
    "CAPM": ["R_MKT"],
    "q-factor (HXZ 2015)": ["R_MKT", "R_ME", "R_IA", "R_ROE"],
    "q5 (HMXZ 2021)": ["R_MKT", "R_ME", "R_IA", "R_ROE", "R_EG"],
}

FACTOR_LABELS = {
    "R_MKT": "Market",
    "R_ME": "Size",
    "R_IA": "Investment",
    "R_ROE": "Profitability",
    "R_EG": "Expected growth",
}

MONTHS_PER_YEAR = 12


def build_spread(df, rank_col, low_rank=None, high_rank=None,
                 rank_ME=None, return_col="ret_vw"):
    """Monthly high-minus-low return of a two-way sorted testing portfolio.

    The files hold 3 size groups x 5 anomaly groups. With rank_ME set, the
    spread is taken inside that one size group. With rank_ME left as None, the
    leg returns are averaged across the three size groups first, which is the
    usual way to read a size-interacted sort without letting one size bucket
    dominate.

    Returns a DataFrame indexed by date with columns low, high and spread.
    """
    if rank_col is None or rank_col not in df.columns:
        return pd.DataFrame(columns=["low", "high", "spread"])

    frame = df.copy()
    if rank_ME is not None:
        frame = frame[frame["rank_ME"] == rank_ME]

    ranks = sorted(frame[rank_col].dropna().unique())
    if len(ranks) < 2:
        return pd.DataFrame(columns=["low", "high", "spread"])

    low_rank = ranks[0] if low_rank is None else low_rank
    high_rank = ranks[-1] if high_rank is None else high_rank

    legs = (
        frame[frame[rank_col].isin([low_rank, high_rank])]
        .groupby(["date", rank_col])[return_col]
        .mean()
        .unstack(rank_col)
    )
    if low_rank not in legs.columns or high_rank not in legs.columns:
        return pd.DataFrame(columns=["low", "high", "spread"])

    out = pd.DataFrame(
        {
            "low": legs[low_rank],
            "high": legs[high_rank],
        }
    ).dropna()
    out["spread"] = out["high"] - out["low"]
    return out


def regress(returns, factors, factor_cols, nw_lags=12):
    """Regress a monthly return series on factor returns.

    `returns` must already be the quantity to be explained: a long-short spread
    (which needs no risk-free adjustment because it is self-financing), or an
    excess return over the risk-free rate for a long-only portfolio.

    t-statistics use Newey-West standard errors with `nw_lags` lags, which is
    the convention in this literature; pass nw_lags=0 for plain OLS.
    """
    aligned = pd.concat([returns.rename("y"), factors[factor_cols]], axis=1).dropna()
    if len(aligned) <= len(factor_cols) + 1:
        return None

    y = aligned["y"]
    X = sm.add_constant(aligned[factor_cols])

    if nw_lags and nw_lags > 0:
        fit = sm.OLS(y, X).fit(cov_type="HAC", cov_kwds={"maxlags": nw_lags})
    else:
        fit = sm.OLS(y, X).fit()

    result = {
        "n_months": int(len(aligned)),
        "start": aligned.index.min(),
        "end": aligned.index.max(),
        "alpha_monthly": fit.params["const"],
        "alpha_annual_pct": fit.params["const"] * MONTHS_PER_YEAR * 100,
        "alpha_t": fit.tvalues["const"],
        "alpha_p": fit.pvalues["const"],
        "r_squared": fit.rsquared,
        "adj_r_squared": fit.rsquared_adj,
        "betas": {col: fit.params[col] for col in factor_cols},
        "beta_t": {col: fit.tvalues[col] for col in factor_cols},
    }
    return result


def raw_stats(returns):
    """Mean, t-stat and volatility of a return series, before any model."""
    series = returns.dropna()
    if series.empty:
        return None
    mean = series.mean()
    t_stat = mean / (series.std(ddof=1) / np.sqrt(len(series))) if series.std(ddof=1) > 0 else np.nan
    return {
        "n_months": int(len(series)),
        "mean_annual_pct": mean * MONTHS_PER_YEAR * 100,
        "t_stat": t_stat,
        "vol_annual_pct": series.std(ddof=1) * np.sqrt(MONTHS_PER_YEAR) * 100,
        "sharpe": (mean * MONTHS_PER_YEAR) / (series.std(ddof=1) * np.sqrt(MONTHS_PER_YEAR))
        if series.std(ddof=1) > 0 else np.nan,
    }


def model_comparison(returns, factors, models=None, nw_lags=12):
    """Run several models on one return series and return a tidy DataFrame."""
    models = models or MODELS
    rows = []

    base = raw_stats(returns)
    if base:
        rows.append(
            {
                "Model": "Raw (no model)",
                "Alpha (% p.a.)": base["mean_annual_pct"],
                "t(alpha)": base["t_stat"],
                "R²": np.nan,
                "Months": base["n_months"],
            }
        )

    for name, cols in models.items():
        available = [col for col in cols if col in factors.columns]
        if len(available) < len(cols):
            continue
        fit = regress(returns, factors, available, nw_lags=nw_lags)
        if not fit:
            continue
        rows.append(
            {
                "Model": name,
                "Alpha (% p.a.)": fit["alpha_annual_pct"],
                "t(alpha)": fit["alpha_t"],
                "R²": fit["r_squared"],
                "Months": fit["n_months"],
            }
        )

    return pd.DataFrame(rows)


def factor_loadings(returns, factors, factor_cols, nw_lags=12):
    """Factor betas and their t-stats as a tidy DataFrame."""
    fit = regress(returns, factors, factor_cols, nw_lags=nw_lags)
    if not fit:
        return pd.DataFrame(columns=["Factor", "Beta", "t(Beta)"])

    rows = []
    for col in factor_cols:
        rows.append(
            {
                "Factor": FACTOR_LABELS.get(col, col),
                "Beta": fit["betas"][col],
                "t(Beta)": fit["beta_t"][col],
            }
        )
    return pd.DataFrame(rows)


def screen_alphas(data_dict, factors, group, model_name="q5 (HMXZ 2021)",
                  rank_ME=None, nw_lags=12, return_col="ret_vw",
                  start_date=None, end_date=None):
    """Alpha of the high-minus-low spread for every anomaly in one group.

    This is the engine behind the screener view: it answers "which anomalies in
    this category does the model fail to explain?" in a single pass.
    """
    from src.data_loader import DataLoader

    factor_cols = MODELS.get(model_name, MODELS["q5 (HMXZ 2021)"])
    available = [col for col in factor_cols if col in factors.columns]

    rows = []
    for factor_key, df in data_dict.get(group, {}).items():
        rank_col = DataLoader.get_factor_rank_column(df)
        spread_frame = build_spread(
            df, rank_col, rank_ME=rank_ME, return_col=return_col
        )
        if spread_frame.empty:
            continue

        spread = spread_frame["spread"]
        if start_date is not None:
            spread = spread[spread.index >= pd.Timestamp(start_date)]
        if end_date is not None:
            spread = spread[spread.index <= pd.Timestamp(end_date)]

        base = raw_stats(spread)
        if not base:
            continue

        fit = regress(spread, factors, available, nw_lags=nw_lags)
        rows.append(
            {
                "code": DataLoader.strip_me_prefix(factor_key),
                "Raw return (% p.a.)": base["mean_annual_pct"],
                "t(raw)": base["t_stat"],
                "Alpha (% p.a.)": fit["alpha_annual_pct"] if fit else np.nan,
                "t(alpha)": fit["alpha_t"] if fit else np.nan,
                "R²": fit["r_squared"] if fit else np.nan,
                "Months": base["n_months"],
            }
        )

    return pd.DataFrame(rows)
