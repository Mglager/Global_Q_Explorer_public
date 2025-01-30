import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import numpy as np
import pandas as pd

# e Brand Colors
e_COLORS = {
    'ocean_blue': '#0F2D46',  # Primary dark blue
    'aqua_blue': '#45EBD8',   # Bright aqua
    'nordic_blue': '#5A7887',  # Nordic blue
    'nordic_green': '#64827D', # Nordic green
    'nordic_red': '#8C5E60',   # Nordic red
    'nordic_beige': '#B4AB91', # Nordic beige
    'nordic_brown': '#777265', # Nordic brown
    'white': '#FFFFFF',        # White
    'light_grey': '#EBEBEB',   # Light grey
    'grey': '#9B9B9B',        # Grey
    'dark_grey': '#3C3C3C',   # Dark grey
    'black': '#000000'        # Black
}

# Default plot styling
PLOT_TEMPLATE = {
    'layout': go.Layout(
        font=dict(family="Arial, sans-serif", size=12, color="#0F2D46"),
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='#FFFFFF',
        title_font=dict(family="Arial, sans-serif", size=16, color=e_COLORS['ocean_blue']),
        xaxis=dict(
            gridcolor=e_COLORS['light_grey'],
            linecolor=e_COLORS['grey'],
            tickfont=dict(family="Arial, sans-serif", size=10, color="#5A7887"),
            showgrid=True,
            zeroline=False
        ),
        yaxis=dict(
            gridcolor=e_COLORS['light_grey'],
            linecolor=e_COLORS['grey'],
            tickfont=dict(family="Arial, sans-serif", size=10, color="#5A7887"),
            showgrid=True,
            zeroline=False
        ),
        margin=dict(t=50, l=50, r=50, b=50)
    )
}

# Custom color sequence for multiple traces - lighter, more distinct colors
e_COLOR_SEQUENCE = [
    '#5A7887',  # nordic blue
    '#64827D',  # nordic green
    '#8C5E60',  # nordic red
    '#45EBD8',  # aqua blue
    '#B4AB91',  # nordic beige
    '#0F2D46',  # ocean blue
    '#777265',  # nordic brown
]

class Visualizer:
    @staticmethod
    def create_time_series(df, factors, title="Factor Performance Over Time"):
        """Create interactive time series plot"""
        fig = go.Figure()
        
        for i, factor in enumerate(factors):
            fig.add_trace(
                go.Scatter(
                    x=df['date'], 
                    y=df[factor], 
                    name=factor,
                    line=dict(color=e_COLOR_SEQUENCE[i % len(e_COLOR_SEQUENCE)]),
                    hovertemplate="%{y:.2f}"
                )
            )
        
        fig.update_layout(
            PLOT_TEMPLATE['layout'],
            title=title,
            xaxis_title="Date",
            yaxis_title="Value",
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor='rgba(255, 255, 255, 0.8)',
                font=dict(family="Arial, sans-serif", size=10)
            )
        )
        return fig

    @staticmethod
    def create_heatmap(correlation_matrix, title="Factor Excess Return Correlations"):
        """Create enhanced correlation heatmap"""
        fig = go.Figure(data=go.Heatmap(
            z=correlation_matrix,
            x=correlation_matrix.columns,
            y=correlation_matrix.columns,
            zmin=-1, zmax=1,
            colorscale=[[0, '#8C5E60'],  # nordic red for negative
                       [0.5, '#FFFFFF'], # white for zero
                       [1, '#5A7887']],  # nordic blue for positive
            text=np.round(correlation_matrix, 2),
            texttemplate='%{text:.2f}',
            textfont=dict(family="Arial, sans-serif", size=10, color="#0F2D46"),
            hoverongaps=False,
        ))
        
        fig.update_layout(
            PLOT_TEMPLATE['layout'],
            title=title,
            height=600,
            width=800,
            xaxis_title="",
            yaxis_title="",
            xaxis={'side': 'bottom', 'tickangle': 45},
            yaxis={'side': 'left', 'autorange': 'reversed'},
            margin=dict(t=50, l=200, r=200, b=200)
        )
        return fig

    @staticmethod
    def create_rolling_stats_plot(df, rolling_stats, return_col='ret_vw', title="Rolling Statistics"):
        """Create rolling statistics plot"""
        fig = go.Figure()
        
        # Get date values whether it's index or column
        dates = df.index if isinstance(df.index, pd.DatetimeIndex) else df['date']
        
        # Returns
        fig.add_trace(go.Scatter(
            x=dates, 
            y=df[return_col],
            name="Monthly Returns",
            line=dict(color='blue', width=1),
            hovertemplate="%{y:.2%}"
        ))
        
        # Rolling mean
        fig.add_trace(go.Scatter(
            x=dates,
            y=rolling_stats['rolling_mean'],
            name='Rolling Mean',
            line=dict(color='red', width=1.5),
            hovertemplate="%{y:.2%}"
        ))
        
        # Rolling bands (mean ± std)
        upper = rolling_stats['rolling_mean'] + rolling_stats['rolling_std']
        lower = rolling_stats['rolling_mean'] - rolling_stats['rolling_std']
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=upper,
            fill=None,
            mode='lines',
            line=dict(color='rgba(0,0,0,0)'),
            showlegend=False,
            hovertemplate="%{y:.2%}"
        ))
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=lower,
            fill='tonexty',
            mode='lines',
            line=dict(color='rgba(0,0,0,0)'),
            name='±1 Std Dev',
            hovertemplate="%{y:.2%}"
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Date",
            yaxis_title="Return",
            yaxis_tickformat='.1%',
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor='rgba(255, 255, 255, 0.8)'
            )
        )
        return fig

    @staticmethod
    def create_drawdown_plot(df, drawdown, return_col='ret_vw', title="Drawdown Analysis"):
        """Create drawdown plot"""
        fig = go.Figure()
        
        dates = df.index if isinstance(df.index, pd.DatetimeIndex) else df['date']
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=drawdown,
            fill='tozeroy',
            name='Drawdown',
            line=dict(color='red'),
            hovertemplate="%{y:.1%}"
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Date",
            yaxis_title="Drawdown",
            yaxis_tickformat='.1%',
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor='rgba(255, 255, 255, 0.8)'
            )
        )
        return fig

    @staticmethod
    def create_relative_performance_plot(df, relative_stats, market_data=None, return_col='ret_vw', title="Relative Performance"):
        """Create relative performance plot with log scale"""
        fig = go.Figure()
        
        # Get dates whether from index or column
        dates = df.index if isinstance(df.index, pd.DatetimeIndex) else df['date']
        
        # Portfolio values
        fig.add_trace(go.Scatter(
            x=dates,
            y=relative_stats['portfolio_value'],
            name='Portfolio',
            line=dict(color='blue'),
            hovertemplate="%{y:.2f}x"
        ))
        
        # Market values
        if market_data is not None:
            market_dates = market_data.index if isinstance(market_data.index, pd.DatetimeIndex) else market_data['date']
            market_cumret = (1 + market_data[return_col]).cumprod()
            fig.add_trace(go.Scatter(
                x=market_dates,
                y=market_cumret,
                name='Market',
                line=dict(color='black', dash='dash'),
                hovertemplate="%{y:.2f}x"
            ))
        
        # Rolling alpha on secondary y-axis
        fig.add_trace(go.Scatter(
            x=dates,
            y=relative_stats['rolling_alpha'] * 100,  # Convert to percentage
            name='Rolling Alpha (% p.a.)',
            line=dict(color='green', dash='dash'),
            yaxis='y2',
            hovertemplate="%{y:.1f}%"
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Date",
            yaxis_title="Cumulative Value (log scale)",
            yaxis_type="log",
            yaxis2=dict(
                title="Rolling Alpha (% p.a.)",
                overlaying="y",
                side="right",
                tickformat='.1f'
            ),
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor='rgba(255, 255, 255, 0.8)'
            )
        )
        return fig

    @staticmethod
    def create_tracking_error_plot(df, relative_stats, title="Tracking Error Analysis"):
        """Create tracking error and information ratio plot"""
        fig = go.Figure()
        
        # Get dates whether from index or column
        dates = df.index if isinstance(df.index, pd.DatetimeIndex) else df['date']
        
        # Tracking Error
        fig.add_trace(go.Scatter(
            x=dates,
            y=relative_stats['tracking_error'],
            name='Tracking Error',
            line=dict(color='orange'),
            hovertemplate="%{y:.2%}"
        ))
        
        # Information Ratio
        fig.add_trace(go.Scatter(
            x=dates,
            y=relative_stats['information_ratio'],
            name='Information Ratio',
            line=dict(color='purple', dash='dash'),
            yaxis='y2',
            hovertemplate="%{y:.2f}"
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Date",
            yaxis_title="Tracking Error",
            yaxis_tickformat='.1%',
            yaxis2=dict(
                title="Information Ratio",
                overlaying="y",
                side="right",
                tickformat='.2f'
            ),
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor='rgba(255, 255, 255, 0.8)'
            )
        )
        return fig

    @staticmethod
    def create_performance_plot(df, return_col='ret_vw', title="Portfolio Performance"):
        """Create performance plot showing cumulative returns"""
        fig = go.Figure()
        
        # Cumulative return index
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['cumulative_return'],
            name="Cumulative Return",
            hovertemplate="%{y:.2f}x"
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Date",
            yaxis_title="Cumulative Return",
            hovermode='x unified'
        )
        return fig

    @staticmethod
    def create_multi_performance_plot(factor_data, market_data=None, return_col='ret_vw', title="Portfolio Performance"):
        """Create performance plot for multiple factors with market returns and log scale"""
        fig = go.Figure()
        
        # Add market returns first if available
        if market_data is not None:
            market_cumret = (1 + market_data[return_col]).cumprod()
            fig.add_trace(go.Scatter(
                x=market_data['date'],
                y=market_cumret,
                name="Market Portfolio",
                line=dict(color='#9B9B9B', dash='dash', width=1),
                hovertemplate="%{y:.2f}x"
            ))
        
        # Add individual factors
        for i, (factor, df) in enumerate(factor_data.items()):
            if factor != "Multifactor Portfolio":
                fig.add_trace(go.Scatter(
                    x=df['date'],
                    y=df['cumulative_return'],
                    name=factor,
                    line=dict(
                        color=e_COLOR_SEQUENCE[i % len(e_COLOR_SEQUENCE)],
                        width=1.5
                    ),
                    hovertemplate="%{y:.2f}x"
                ))
        
        # Add multifactor portfolio last with bold line
        if "Multifactor Portfolio" in factor_data:
            df = factor_data["Multifactor Portfolio"]
            fig.add_trace(go.Scatter(
                x=df['date'],
                y=df['cumulative_return'],
                name="Multifactor Portfolio",
                line=dict(color='#0F2D46', width=2.5),
                hovertemplate="%{y:.2f}x"
            ))
        
        fig.update_layout(
            PLOT_TEMPLATE['layout'],
            title=title,
            xaxis_title="Date",
            yaxis_title="Cumulative Return (log scale)",
            yaxis_type="log",
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor='rgba(255, 255, 255, 0.9)',
                bordercolor='#EBEBEB',
                borderwidth=1,
                font=dict(family="Arial, sans-serif", size=10, color="#0F2D46")
            )
        )
        return fig

    @staticmethod
    def create_excess_return_plot(factor_data, market_data, return_col='ret_vw', title="Excess Return Performance"):
        """Create performance plot showing cumulative excess returns vs market"""
        fig = go.Figure()
        
        # Add individual factors
        for i, (factor, df) in enumerate(factor_data.items()):
            if factor != "Multifactor Portfolio":
                # Align dates
                common_dates = df.index.intersection(market_data.index) if isinstance(df.index, pd.DatetimeIndex) else df['date']
                factor_returns = df[return_col]
                market_returns = market_data[return_col]
                
                # Calculate excess returns
                excess_returns = factor_returns - market_returns
                cum_excess = (1 + excess_returns).cumprod()
                
                # Add trace
                fig.add_trace(go.Scatter(
                    x=common_dates,
                    y=cum_excess,
                    name=factor,
                    line=dict(
                        color=e_COLOR_SEQUENCE[i % len(e_COLOR_SEQUENCE)],
                        width=1.5
                    ),
                    hovertemplate="%{y:.2f}x"
                ))
        
        # Add multifactor portfolio last with bold line
        if "Multifactor Portfolio" in factor_data:
            df = factor_data["Multifactor Portfolio"]
            common_dates = df.index.intersection(market_data.index) if isinstance(df.index, pd.DatetimeIndex) else df['date']
            factor_returns = df[return_col]
            market_returns = market_data[return_col]
            
            excess_returns = factor_returns - market_returns
            cum_excess = (1 + excess_returns).cumprod()
            
            fig.add_trace(go.Scatter(
                x=common_dates,
                y=cum_excess,
                name="Multifactor Portfolio",
                line=dict(color='#0F2D46', width=2.5),  # Ocean blue, bold line
                hovertemplate="%{y:.2f}x"
            ))
        
        # Add horizontal line at y=1 for reference
        fig.add_hline(
            y=1, 
            line=dict(
                dash="dash",
                color=e_COLORS['grey'],
                width=1
            ),
            opacity=0.5
        )
        
        fig.update_layout(
            PLOT_TEMPLATE['layout'],
            title=title,
            xaxis_title="Date",
            yaxis_title="Cumulative Excess Return (log scale)",
            yaxis_type="log",
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor='rgba(255, 255, 255, 0.9)',
                bordercolor=e_COLORS['light_grey'],
                borderwidth=1,
                font=dict(
                    family="Arial, sans-serif",
                    size=10,
                    color=e_COLORS['ocean_blue']
                )
            )
        )
        return fig 