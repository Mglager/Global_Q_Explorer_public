import pandas as pd
import numpy as np
from scipy import stats

class Analysis:
    @staticmethod
    def calculate_rolling_stats(df, return_col='ret_vw', window=12):
        """Calculate rolling statistics for returns"""
        rolling_stats = pd.DataFrame()
        
        # Calculate rolling statistics
        rolling_stats['rolling_mean'] = df[return_col].rolling(window).mean() * 12  # Annualize
        rolling_stats['rolling_std'] = df[return_col].rolling(window).std() * np.sqrt(12)
        rolling_stats['rolling_sharpe'] = (
            rolling_stats['rolling_mean'] / 
            rolling_stats['rolling_std']
        )
        return rolling_stats
    
    @staticmethod
    def calculate_drawdown(df, return_col='ret_vw'):
        """Calculate drawdown series for returns"""
        values = (1 + df[return_col]).cumprod()
        rolling_max = values.cummax()
        drawdown = (values - rolling_max) / rolling_max
        return drawdown
    
    @staticmethod
    def factor_quantile_analysis(df, return_col='ret_vw', n_quantiles=5):
        """Analyze return performance by quantiles"""
        df['quantile'] = pd.qcut(df[return_col], n_quantiles, labels=False) + 1
        quantile_stats = df.groupby('quantile')[return_col].agg([
            'mean', 'std', 'count',
            lambda x: stats.skew(x, nan_policy='omit'),
            lambda x: stats.kurtosis(x, nan_policy='omit')
        ]).round(4)
        quantile_stats.columns = ['Mean', 'Std Dev', 'Count', 'Skewness', 'Kurtosis']
        return quantile_stats

    @staticmethod
    def calculate_relative_performance(df, return_col='ret_vw', market_data=None, window=12):
        """Calculate relative performance against market portfolio"""
        relative_stats = pd.DataFrame()
        
        # Store portfolio values
        relative_stats['portfolio_value'] = (1 + df[return_col]).cumprod()
        
        if market_data is not None and return_col in market_data.columns:
            # Calculate market values and relative statistics
            relative_stats['market_value'] = (1 + market_data[return_col]).cumprod()
            
            # Calculate rolling statistics
            relative_stats['rolling_alpha'] = (
                df[return_col].rolling(window).mean() - 
                market_data[return_col].rolling(window).mean()
            ) * 12  # Annualize
            
            relative_stats['rolling_beta'] = (
                df[return_col]
                .rolling(window)
                .cov(market_data[return_col]) /
                market_data[return_col]
                .rolling(window)
                .var()
            )
            
            # Calculate tracking error
            relative_stats['tracking_error'] = (
                (df[return_col] - market_data[return_col])
                .rolling(window)
                .std() * np.sqrt(12)
            )
            
            # Calculate information ratio
            relative_stats['information_ratio'] = (
                relative_stats['rolling_alpha'] / 
                relative_stats['tracking_error']
            )
        else:
            # If no market data, just store portfolio statistics
            relative_stats['market_value'] = None
            relative_stats['rolling_alpha'] = None
            relative_stats['rolling_beta'] = None
            relative_stats['tracking_error'] = None
            relative_stats['information_ratio'] = None
        
        return relative_stats

    @staticmethod
    def calculate_market_relative_statistics(df, return_col='ret_vw', market_data=None):
        """Calculate market-relative statistics for a portfolio"""
        stats = {}
        
        # Ensure data is properly aligned
        if market_data is not None:
            # Get common dates
            common_dates = df.index.intersection(market_data.index)
            df = df.loc[common_dates]
            market_data = market_data.loc[common_dates]
            
            # Calculate basic statistics
            portfolio_returns = df[return_col]
            market_returns = market_data[return_col]
            
            # Beta calculation
            cov_matrix = pd.concat([portfolio_returns, market_returns], axis=1).cov()
            beta = cov_matrix.iloc[0, 1] / cov_matrix.iloc[1, 1]
            stats['Beta'] = beta
            
            # Correlation
            correlation = portfolio_returns.corr(market_returns)
            stats['Correlation'] = correlation
            
            # Average number of stocks
            if 'n_stocks' in df.columns:
                stats['Average N Stocks'] = df['n_stocks'].mean()
            else:
                stats['Average N Stocks'] = None
            
            # Annual statistics (assuming monthly data)
            annual_factor = 12
            
            # Mean returns
            portfolio_mean = portfolio_returns.mean() * annual_factor
            market_mean = market_returns.mean() * annual_factor
            
            # Volatilities
            portfolio_vol = portfolio_returns.std() * np.sqrt(annual_factor)
            market_vol = market_returns.std() * np.sqrt(annual_factor)
            
            # Alpha calculation (CAPM)
            alpha = portfolio_mean - (beta * market_mean)
            stats['Annual Alpha (%)'] = alpha
            
            # Excess return
            excess_return = portfolio_mean - market_mean
            stats['Excess Return (% p.a.)'] = excess_return
            
            # Information Ratio
            tracking_error = (portfolio_returns - market_returns).std() * np.sqrt(annual_factor)
            stats['Tracking Error (% p.a.)'] = tracking_error
            
            if tracking_error > 0:
                stats['Information Ratio'] = excess_return / tracking_error
            else:
                stats['Information Ratio'] = None
            
            # R-squared
            stats['R-Squared'] = correlation ** 2
            
            # Sharpe Ratio (assuming 0 risk-free rate for simplicity)
            if portfolio_vol > 0:
                stats['Sharpe Ratio'] = portfolio_mean / portfolio_vol
            else:
                stats['Sharpe Ratio'] = None
            
            # Higher moments
            stats['Skewness'] = portfolio_returns.skew()
            stats['Kurtosis'] = portfolio_returns.kurtosis()
            
            # Mean return and volatility
            stats['Mean Return (% p.a.)'] = portfolio_mean
            stats['Volatility (% p.a.)'] = portfolio_vol
            
        return stats 