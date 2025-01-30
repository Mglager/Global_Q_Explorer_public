import pandas as pd
import numpy as np

class DataProcessor:
    @staticmethod
    def calculate_statistics(df, return_col='ret_vw', market_data=None):
        """Calculate comprehensive statistics for a portfolio"""
        returns = df[return_col]
        
        # Calculate excess returns if market data is available
        if market_data is not None:
            excess_returns = returns - market_data[return_col]
            mean_excess = excess_returns.mean() * 12  # Annualize
            vol_excess = excess_returns.std() * np.sqrt(12)
            ir = mean_excess / vol_excess if vol_excess != 0 else 0
        else:
            mean_excess = None
            vol_excess = None
            ir = None

        # Calculate basic statistics
        mean_return = returns.mean() * 12  # Annualize
        volatility = returns.std() * np.sqrt(12)
        sharpe = mean_return / volatility if volatility != 0 else 0
        
        stats = {
            'Mean Return (% p.a.)': mean_return * 100,
            'Volatility (% p.a.)': volatility * 100,
            'Sharpe Ratio': sharpe,
            'Skewness': returns.skew(),
            'Kurtosis': returns.kurtosis(),
            'Excess Return (% p.a.)': mean_excess * 100 if mean_excess is not None else None,
            'Tracking Error (% p.a.)': vol_excess * 100 if vol_excess is not None else None,
            'Information Ratio': ir if ir is not None else None,
            'Average N Stocks': df['nstocks'].mean() if 'nstocks' in df.columns else None
        }
        
        return pd.Series(stats)

    @staticmethod
    def calculate_correlation_matrix(df, factors):
        """Calculate correlation matrix between factors"""
        return df[factors].corr()

    @staticmethod
    def calculate_multi_correlation_matrix(factor_data, market_data, return_col='ret_vw'):
        """Calculate correlation matrix of excess returns"""
        # Create DataFrame for excess returns
        excess_returns = pd.DataFrame()
        
        for factor, df in factor_data.items():
            # Align dates between factor and market data
            common_dates = df.index.intersection(market_data.index)
            factor_returns = df.loc[common_dates, return_col]
            market_returns = market_data.loc[common_dates, return_col]
            
            # Calculate excess returns
            excess_returns[factor] = factor_returns - market_returns
        
        # Calculate correlation matrix
        corr_matrix = excess_returns.corr()
        
        return corr_matrix 