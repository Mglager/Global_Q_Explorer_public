import pandas as pd
import streamlit as st
import os
from pathlib import Path

class DataLoader:
    @staticmethod
    def create_date_column(df):
        """Create date column from year and month"""
        if 'year' in df.columns and 'month' in df.columns:
            df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
        return df

    @staticmethod
    @st.cache_data
    def load_data_directory(base_path="data"):
        """Load and organize all available datasets"""
        data_dict = {}
        
        # First load market portfolio data
        market_file = os.path.join(base_path, "portf_me_monthly_2023.csv")
        if os.path.exists(market_file):
            market_data = pd.read_csv(market_file)
            market_data = DataLoader.create_date_column(market_data)
            market_data['ret_vw'] = market_data['ret_vw'] / 100
            data_dict['market_portfolio'] = market_data
        
        # Walk through all subdirectories in the data folder
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith('.csv') and file != "portf_me_monthly_2023.csv":
                    # Get relative path components
                    rel_path = os.path.relpath(root, base_path)
                    group_name = rel_path.split(os.sep)[0]  # First subdirectory is the group name
                    
                    # Create group if it doesn't exist
                    if group_name not in data_dict:
                        data_dict[group_name] = {}
                    
                    # Load the CSV file
                    file_path = os.path.join(root, file)
                    df = pd.read_csv(file_path)
                    df = DataLoader.create_date_column(df)
                    df['ret_vw'] = df['ret_vw'] / 100
                    
                    # Extract factor name from filename
                    factor_name = os.path.splitext(file)[0].split('portf_')[-1].split('_monthly')[0]
                    data_dict[group_name][factor_name] = df
        
        return data_dict

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