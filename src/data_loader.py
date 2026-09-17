import os
import re
import glob

import pandas as pd
import streamlit as st

# Directory name -> short category key used by the metric catalog.
GROUP_TO_CATEGORY = {
    "me_mom": "momentum",
    "me_vvg": "value-growth",
    "me_inv": "investment",
    "me_prof": "profitability",
    "me_intan": "intangibles",
    "me_fric": "frictions",
}


class DataLoader:
    @staticmethod
    def create_date_column(df):
        """Create date column from year and month"""
        if 'year' in df.columns and 'month' in df.columns:
            df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
        return df

    @staticmethod
    def detect_vintage(base_path="data"):
        """Find the data vintage (e.g. '2025') from the market portfolio filename.

        The global-q.org library stamps the last sample year into every filename,
        so the vintage is read off the data rather than hard-coded. Updating to a
        new release is then a matter of dropping in the new files.
        """
        candidates = glob.glob(os.path.join(base_path, "portf_me_monthly_*.csv"))
        years = []
        for path in candidates:
            match = re.search(r"portf_me_monthly_(\d{4})\.csv$", os.path.basename(path))
            if match:
                years.append(match.group(1))
        return max(years) if years else None

    @staticmethod
    def market_portfolio_filename(base_path="data"):
        """Filename of the size-decile market portfolio file for the current vintage."""
        vintage = DataLoader.detect_vintage(base_path)
        return f"portf_me_monthly_{vintage}.csv" if vintage else None

    @staticmethod
    def parse_factor_name(filename):
        """'portf_me_roe_1_monthly_2025.csv' -> 'me_roe_1'"""
        stem = os.path.splitext(os.path.basename(filename))[0]
        stem = stem.split('portf_')[-1]
        return re.sub(r"_monthly_\d{4}$", "", stem)

    @staticmethod
    def group_to_category(group_name):
        """'me_prof_monthly_2025' -> 'profitability'"""
        prefix = re.sub(r"_monthly_\d{4}$", "", group_name)
        return GROUP_TO_CATEGORY.get(prefix, prefix)

    @staticmethod
    def strip_me_prefix(factor_key):
        """'me_roe_1' -> 'roe_1'. Only the leading 'me_' is removed."""
        return factor_key[3:] if factor_key.startswith('me_') else factor_key

    @staticmethod
    @st.cache_data
    def load_data_directory(base_path="data"):
        """Load and organize all available datasets"""
        data_dict = {}

        market_name = DataLoader.market_portfolio_filename(base_path)

        # First load market portfolio data
        if market_name:
            market_file = os.path.join(base_path, market_name)
            if os.path.exists(market_file):
                market_data = pd.read_csv(market_file)
                market_data = DataLoader.create_date_column(market_data)
                market_data['ret_vw'] = market_data['ret_vw'] / 100
                data_dict['market_portfolio'] = market_data

        # Walk through all subdirectories in the data folder
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if not file.endswith('.csv') or file == market_name:
                    continue
                if file.startswith('q5_factors'):
                    continue

                rel_path = os.path.relpath(root, base_path)
                if rel_path == os.curdir:
                    continue
                group_name = rel_path.split(os.sep)[0]

                if group_name not in data_dict:
                    data_dict[group_name] = {}

                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path)
                df = DataLoader.create_date_column(df)
                df['ret_vw'] = df['ret_vw'] / 100

                factor_name = DataLoader.parse_factor_name(file)
                data_dict[group_name][factor_name] = df

        return data_dict

    @staticmethod
    @st.cache_data
    def load_q5_factors(base_path="data"):
        """Load the q5 factor returns (R_F, R_MKT, R_ME, R_IA, R_ROE, R_EG).

        Source: global-q.org, Hou, Mo, Xue and Zhang (2021). Returns are stored
        in percent in the source file and are converted to decimals here so they
        sit on the same scale as the testing-portfolio returns.
        """
        candidates = sorted(glob.glob(os.path.join(base_path, "q5_factors_monthly_*.csv")))
        if not candidates:
            return None

        df = pd.read_csv(candidates[-1])
        df = DataLoader.create_date_column(df)
        for col in df.columns:
            if col.startswith('R_'):
                df[col] = df[col] / 100
        return df

    @staticmethod
    def get_sample_range(data_dict):
        """(first date, last date) of the market portfolio, for display."""
        market = data_dict.get('market_portfolio')
        if market is None or 'date' not in market.columns:
            return None, None
        return market['date'].min(), market['date'].max()

    @staticmethod
    def get_portfolio_columns():
        """Get standard portfolio columns and their descriptions"""
        return {
            'ret_vw': 'Value-weighted Returns (%)',
            #'ret_ew': 'Equal-weighted Returns (%)',
            'nstocks': 'Number of Stocks',
            'rank_ME': 'Market Cap Ranking'
        }

    @staticmethod
    def get_return_columns():
        """Get available return measure columns"""
        return ['ret_vw']

    @staticmethod
    def get_available_groups(data_dict):
        """Get list of available data groups"""
        return list(data_dict.keys())

    @staticmethod
    def get_available_factors(data_dict, group):
        """Get list of available factors in a group"""
        return list(data_dict[group].keys())

    @staticmethod
    def get_available_ranks(data_dict, group, factor):
        """Get available ranks for a factor"""
        df = data_dict[group][factor]
        rank_columns = [col for col in df.columns if col.startswith('rank_') and col != 'rank_ME']
        ranks = {}
        for rank_col in rank_columns:
            ranks[rank_col] = sorted(df[rank_col].unique())
        return ranks

    @staticmethod
    def get_factor_rank_column(df):
        """The anomaly rank column of a two-way sorted file (not rank_ME)."""
        for col in df.columns:
            if col.startswith('rank_') and col != 'rank_ME':
                return col
        return None

    @staticmethod
    def get_factor_data(data_dict, group, factors, rank_ME=None, factor_ranks=None):
        """
        Get data for specific factors and ranks

        Parameters:
        - data_dict: The data dictionary
        - group: The group name
        - factors: List of factor names
        - rank_ME: Optional market cap rank to filter
        - factor_ranks: Dict of {factor_name: {rank_column: rank_value}}
        """
        factor_data = {}
        for factor in factors:
            df = data_dict[group][factor].copy()

            # Apply market cap filter if specified
            if rank_ME is not None:
                df = df[df['rank_ME'] == rank_ME]

            # Apply factor-specific rank filter if specified
            if factor_ranks and factor in factor_ranks:
                for rank_col, rank_val in factor_ranks[factor].items():
                    df = df[df[rank_col] == rank_val]

            factor_data[factor] = df
        return factor_data

    @staticmethod
    def get_common_columns(df):
        """Get list of available columns excluding standard ones"""
        exclude_cols = ['year', 'month', 'date', 'nstocks']
        return [col for col in df.columns if col not in exclude_cols]

    @staticmethod
    def get_market_portfolio(data_dict, rank_ME=1):
        """Get market portfolio data for specific rank"""
        if 'market_portfolio' in data_dict:
            market_data = data_dict['market_portfolio']
            return market_data[market_data['rank_ME'] == rank_ME].copy()
        return None

    @staticmethod
    def get_available_market_caps(data_dict, group, factor):
        """Get available market cap ranks for a factor"""
        if group in data_dict and factor in data_dict[group]:
            return sorted(data_dict[group][factor]['rank_ME'].unique())
