import streamlit as st
import pandas as pd
from src.data_loader import DataLoader
from src.data_processor import DataProcessor
from src.visualizations import Visualizer
from src.analysis import Analysis
from datetime import datetime

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

#Configure Streamlit theme
st.set_page_config(
    page_title="Global Q Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to apply e styling
st.markdown("""
    <style>
        /* Main font and colors */
        html, body, [class*="css"] {
            font-family: Arial, sans-serif;
            background-color: #FFFFFF;
        }
        
        /* Headers */
        h1, h2, h3 {
            font-family: Arial, sans-serif;
            color: #0F2D46;
            font-weight: 600;
            padding-top: 1rem;
            padding-bottom: 0.5rem;
        }
        
        h4, h5, h6 {
            font-family: Arial, sans-serif;
            color: #5A7887;
            font-weight: 500;
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
        }
        
        /* Sidebar */
        .css-1d391kg, .css-12oz5g7 {
            background-color: #F7F7F7;
            border-right: 1px solid #EBEBEB;
        }
        
        /* Buttons */
        .stButton>button {
            background-color: #5A7887;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            transition: background-color 0.2s;
        }
        .stButton>button:hover {
            background-color: #0F2D46;
        }
        
        /* Selectbox */
        .stSelectbox [data-baseweb="select"] {
            border-color: #5A7887;
            border-radius: 4px;
        }
        
        /* Slider */
        .stSlider [data-baseweb="slider"] {
            background-color: #5A7887;
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            background-color: #F7F7F7;
            color: #0F2D46;
            border: 1px solid #EBEBEB;
            border-radius: 4px;
            padding: 0.5rem;
        }
        
        /* DataFrames */
        .dataframe {
            font-family: Arial, sans-serif;
            font-size: 12px;
            border-collapse: collapse;
            border: none;
        }
        .dataframe th {
            background-color: #F7F7F7;
            color: #0F2D46;
            font-weight: 600;
            padding: 8px;
            border: 1px solid #EBEBEB;
        }
        .dataframe td {
            padding: 8px;
            border: 1px solid #EBEBEB;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: #F7F7F7;
            padding: 0.5rem;
            border-radius: 4px;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #FFFFFF;
            color: #5A7887;
            border: 1px solid #EBEBEB;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            font-weight: 500;
        }
        .stTabs [data-baseweb="tab"]:focus {
            background-color: #5A7887;
            color: #FFFFFF;
        }
        
        /* Warning/Info messages */
        .stAlert {
            background-color: #F7F7F7;
            color: #0F2D46;
            border: 1px solid #EBEBEB;
            border-radius: 4px;
            padding: 1rem;
        }
        
        /* Metric styling */
        .css-1xarl3l {
            background-color: #F7F7F7;
            border: 1px solid #EBEBEB;
            border-radius: 4px;
            padding: 1rem;
        }
        
        /* Main content area */
        .main .block-container {
            padding: 2rem;
            background-color: #FFFFFF;
        }
        
        /* Multiselect */
        .stMultiSelect [data-baseweb="select"] {
            background-color: #FFFFFF;
            border-color: #5A7887;
            border-radius: 4px;
        }
        
        /* Number input */
        .stNumberInput [data-baseweb="input"] {
            border-color: #5A7887;
            border-radius: 4px;
        }
        
        /* Checkbox */
        .stCheckbox {
            color: #0F2D46;
        }
    </style>
""", unsafe_allow_html=True)

# Group name mappings
GROUP_NAMES = {
    "momentum": "Momentum",
    "value": "Value-versus-Growth",
    "investment": "Investment",
    "profitability": "Profitability",
    "intangibles": "Intangibles",
    "frictions": "Frictions"
}

# Factor name mappings
FACTOR_NAMES = {
    # Momentum
    "abr_1": "Abnormal Earnings Returns (1m)",
    "abr_6": "Abnormal Earnings Returns (6m)",
    "abr_12": "Abnormal Earnings Returns (12m)",
    "cim_1": "Customer Industries Momentum (1m)",
    "cim_6": "Customer Industries Momentum (6m)",
    "cim_12": "Customer Industries Momentum (12m)",
    "cm_1": "Customer Momentum (1m)",
    "cm_6": "Customer Momentum (6m)",
    "cm_12": "Customer Momentum (12m)",
    "def_1": "Changes in Analyst Forecasts (1m)",
    "def_6": "Changes in Analyst Forecasts (6m)",
    "def_12": "Changes in Analyst Forecasts (12m)",
    "ile_1": "Industry Lead-Lag Earnings (1m)",
    "ilr_1": "Industry Lead-Lag Returns (1m)",
    "ilr_6": "Industry Lead-Lag Returns (6m)",
    "ilr_12": "Industry Lead-Lag Returns (12m)",
    "im_1": "Industry Momentum (1m)",
    "im_6": "Industry Momentum (6m)",
    "im_12": "Industry Momentum (12m)",
    "nei_1": "Consecutive Earnings Increase (1m)",
    "p52w_6": "52-Week High (6m)",
    "p52w_12": "52-Week High (12m)",
    "r6_1": "6-Month Prior Returns (1m)",
    "r6_6": "6-Month Prior Returns (6m)",
    "r6_12": "6-Month Prior Returns (12m)",
    "r11_1": "11-Month Prior Returns (1m)",
    "r11_6": "11-Month Prior Returns (6m)",
    "r11_12": "11-Month Prior Returns (12m)",
    "re_1": "Analyst Earnings Forecast Revisions (1m)",
    "re_6": "Analyst Earnings Forecast Revisions (6m)",
    "resid6_6": "6-Month Residual Momentum (6m)",
    "resid6_12": "6-Month Residual Momentum (12m)",
    "resid11_1": "11-Month Residual Momentum (1m)",
    "resid11_6": "11-Month Residual Momentum (6m)",
    "resid11_12": "11-Month Residual Momentum (12m)",
    "rs_1": "Revenue Surprises (1m)",
    "sim_1": "Supplier Industries Momentum (1m)",
    "sim_12": "Supplier Industries Momentum (12m)",
    "sm_1": "Segment Momentum (1m)",
    "sm_12": "Segment Momentum (12m)",
    "sue_1": "Standard Unexpected Earnings (1m)",
    "sue_6": "Standard Unexpected Earnings (6m)",
    
    # Value-versus-growth
    "bm": "Book-to-Market Equity",
    "bmj": "Book-to-June-Market Equity",
    "bmq_12": "Quarterly Book-to-Market (12m)",
    "cp": "Cash Flow-to-Price",
    "cpq_1": "Quarterly Cash Flow-to-Price (1m)",
    "cpq_6": "Quarterly Cash Flow-to-Price (6m)",
    "cpq_12": "Quarterly Cash Flow-to-Price (12m)",
    "dp": "Dividend Yield",
    "dur": "Equity Duration",
    "ebp": "Enterprise Book-to-Price",
    "em": "Enterprise Multiple",
    "emq_1": "Quarterly Enterprise Multiple (1m)",
    "emq_6": "Quarterly Enterprise Multiple (6m)",
    "emq_12": "Quarterly Enterprise Multiple (12m)",
    "ep": "Earnings-to-Price",
    "epq_1": "Quarterly Earnings-to-Price (1m)",
    "epq_6": "Quarterly Earnings-to-Price (6m)",
    "epq_12": "Quarterly Earnings-to-Price (12m)",
    "ir": "Intangible Return",
    "nop": "Net Payout Yield",
    "ocp": "Operating Cash Flow-to-Price",
    "ocpq_1": "Quarterly Operating Cash Flow-to-Price (1m)",
    "op": "Payout Yield",
    "rev_1": "Long-term Reversal (1m)",
    "rev_6": "Long-term Reversal (6m)",
    "rev_12": "Long-term Reversal (12m)",
    "sp": "Sales-to-Price",
    "spq_1": "Quarterly Sales-to-Price (1m)",
    "spq_6": "Quarterly Sales-to-Price (6m)",
    "spq_12": "Quarterly Sales-to-Price (12m)",
    "vfp": "Analyst-based Intrinsic Value-to-Market",
    "vhp": "ROE-based Intrinsic Value-to-Market",
    
    # Investment
    "aci": "Abnormal Corporate Investment",
    "cei": "Composite Equity Issuance",
    "dac": "Discretionary Accruals",
    "dbe": "Changes in Book Equity",
    "dcoa": "Changes in Current Operating Assets",
    "dfin": "Changes in Net Financial Assets",
    "dfnl": "Changes in Financial Liabilities",
    "dii": "Changes in Investment vs Industry",
    "dlno": "Changes in Long-term Net Operating Assets",
    "dlti": "Changes in Long-term Investments",
    "dnca": "Changes in Non-current Operating Assets",
    "dnco": "Changes in Net Non-current Operating Assets",
    "dnoa": "Changes in Net Operating Assets",
    "dpia": "Changes in PPE and Inventory to Assets",
    "dwc": "Changes in Net Non-cash Working Capital",
    "ia": "Investment-to-Assets",
    "iaq_1": "Quarterly Investment-to-Assets (1m)",
    "iaq_6": "Quarterly Investment-to-Assets (6m)",
    "iaq_12": "Quarterly Investment-to-Assets (12m)",
    "ig": "Investment Growth",
    "ig2": "2-Year Investment Growth",
    "ivc": "Inventory Changes",
    "ivg": "Inventory Growth",
    "ndf": "Net External Debt Financing",
    "nxf": "Net External Equity Financing",
    "noa": "Net Operating Assets",
    "nsi": "Net Stock Issues",
    "oa": "Operating Accruals",
    "pda": "Percent Discretionary Accruals",
    "poa": "Percent Operating Accruals",
    "pta": "Percent Total Accruals",
    "ta": "Total Accruals",
        # Profitability
    "ato": "Asset Turnover",
    "atoq_1": "Quarterly Asset Turnover (1m)",
    "atoq_6": "Quarterly Asset Turnover (6m)",
    "atoq_12": "Quarterly Asset Turnover (12m)",
    "cla": "Cash Operating Profits-to-Assets",
    "claq_1": "Quarterly Cash Operating Profits (1m)",
    "claq_6": "Quarterly Cash Operating Profits (6m)",
    "claq_12": "Quarterly Cash Operating Profits (12m)",
    "cop": "Operating Cash Flow-to-Assets",
    "cto": "Capital Turnover",
    "ctoq_1": "Quarterly Capital Turnover (1m)",
    "ctoq_6": "Quarterly Capital Turnover (6m)",
    "ctoq_12": "Quarterly Capital Turnover (12m)",
    "droa_1": "Change in Return on Assets (1m)",
    "droa_6": "Change in Return on Assets (6m)",
    "droe_1": "Change in Return on Equity (1m)",
    "droe_6": "Change in Return on Equity (6m)",
    "droe_12": "Change in Return on Equity (12m)",
    "eg_1": "Expected Growth (1m)",
    "eg_6": "Expected Growth (6m)",
    "eg_12": "Expected Growth (12m)",
    "fp_6": "Failure Probability (6m)",
    "fq_1": "Quarterly Fundamental Score (1m)",
    "fq_6": "Quarterly Fundamental Score (6m)",
    "fq_12": "Quarterly Fundamental Score (12m)",
    "glaq_1": "Quarterly Gross Profits-to-Assets (1m)",
    "glaq_6": "Quarterly Gross Profits-to-Assets (6m)",
    "glaq_12": "Quarterly Gross Profits-to-Assets (12m)",
    "gpa": "Gross Profits-to-Assets",
    "olaq_1": "Quarterly Operating Profits-to-Assets (1m)",
    "olaq_6": "Quarterly Operating Profits-to-Assets (6m)",
    "olaq_12": "Quarterly Operating Profits-to-Assets (12m)",
    "oleq_1": "Quarterly Operating Profits-to-Equity (1m)",
    "oleq_6": "Quarterly Operating Profits-to-Equity (6m)",
    "opa": "Operating Profits-to-Assets",
    "ope": "Operating Profits-to-Equity",
    "oq_1": "Quarterly O-Score (1m)",
    "pmq_1": "Quarterly Profit Margin (1m)",
    "rnaq_1": "Quarterly Return on Net Operating Assets (1m)",
    "rnaq_6": "Quarterly Return on Net Operating Assets (6m)",
    "rnaq_12": "Quarterly Return on Net Operating Assets (12m)",
    "roa_1": "Return on Assets (1m)",
    "roa_6": "Return on Assets (6m)",
    "roe_1": "Return on Equity (1m)",
    "roe_6": "Return on Equity (6m)",
    "sgq_1": "Quarterly Sales Growth (1m)",
    "tbiq_6": "Quarterly Tax-to-Book Income (6m)",
    "tbiq_12": "Quarterly Tax-to-Book Income (12m)",

    # Intangibles
    "adm": "Advertising-to-Market",
    "almq_1": "Quarterly Asset Liquidity (1m)",
    "almq_6": "Quarterly Asset Liquidity (6m)",
    "almq_12": "Quarterly Asset Liquidity (12m)",
    "eprd": "Earnings Predictability",
    "dls_1": "Long-Short Earnings Growth Forecast Disparity (1m)",
    "etl": "Earnings Timeliness",
    "etr": "Effective Tax Rate",
    "hs": "Industry Sales Concentration",
    "ioca": "Industry-Adjusted Organizational Capital-to-Assets",
    "oca": "Organizational Capital-to-Assets",
    "ol": "Operating Leverage",
    "olq_1": "Quarterly Operating Leverage (1m)",
    "olq_6": "Quarterly Operating Leverage (6m)",
    "olq_12": "Quarterly Operating Leverage (12m)",
    "r1a": "Seasonality Month t-12",
    "r1n": "Seasonality Months t-11 to t-1",
    "r5a": "Seasonality Months t-24,36,48,60",
    "r5n": "Seasonality Months t-60 to t-13 (Excl. Special)",
    "r10a": "Seasonality Months t-72,84,96,108,120",
    "r10n": "Seasonality Months t-120 to t-61 (Excl. Special)",
    "r15a": "Seasonality Months t-132,144,156,168,180",
    "r20a": "Seasonality Months t-192,204,216,228,240",
    "rca": "R&D Capital-to-Assets",
    "rdm": "R&D Expense-to-Market",
    "rdmq_1": "Quarterly R&D Expense-to-Market (1m)",
    "rdmq_6": "Quarterly R&D Expense-to-Market (6m)",
    "rdmq_12": "Quarterly R&D Expense-to-Market (12m)",
    "rdsq_6": "Quarterly R&D Expense-to-Sales (6m)",
    "rdsq_12": "Quarterly R&D Expense-to-Sales (12m)",
    "rer": "Industry-Adjusted Real Estate Ratio",

    # Frictions
    "beta_1": "Market Beta (1m)",
    "dtv_12": "Dollar Trading Volume (12m)",
    "isff_1": "FF3 Idiosyncratic Skewness (1m)",
    "isq_1": "Q-Factor Idiosyncratic Skewness (1m)",
    "ivff_1": "FF3 Idiosyncratic Volatility (1m)",
    "ivq_1": "Q-Factor Idiosyncratic Volatility (1m)",
    "me": "Market Equity",
    "srev": "Short-term Reversal",
    "sv_1": "Systematic Volatility (1m)",
    "tv_1": "Total Volatility (1m)"

}

# Rank name mappings
RANK_NAMES = {
    "rank_ME": "Market Cap",
    "rank_beta": "Beta",
    "rank_mom": "Momentum",
    "rank_bm": "Book-to-Market",
    "rank_op": "Operating Profitability",
    "rank_inv": "Investment"
}

def get_display_name(factor_key):
    """Get display name for a factor, handling group prefixes"""
    if '/' in factor_key:
        group, factor = factor_key.split('/')
        group_display = GROUP_NAMES.get(group, group)
        if 'me_' in factor:
            factor_stripped = factor.replace('me_', '')
            base_name = FACTOR_NAMES.get(factor_stripped, factor_stripped)
        else:
            base_name = FACTOR_NAMES.get(factor, factor)
        return f"{group_display}: {base_name}"
    else:
        if 'me_' in factor_key:
            factor_stripped = factor_key.replace('me_', '')
            base_name = FACTOR_NAMES.get(factor_stripped, factor_stripped)
        else:
            base_name = FACTOR_NAMES.get(factor_key, factor_key)
        return base_name

def create_factor_display_dict(factors, group=None):
    """Create a dictionary mapping display names to factor codes"""
    display_dict = {}
    for factor in factors:
        if group:
            display_name = get_display_name(f"{group}/{factor}")
            display_name = get_display_name(factor)
            display_dict[display_name] = factor
        else:
            display_name = get_display_name(factor)
            display_dict[display_name] = factor
    return display_dict

def format_rank_name(rank_col):
    """Format rank column name for display"""
    return RANK_NAMES.get(rank_col, rank_col.replace('rank_', '').replace('_', ' ').title())

def create_multifactor_portfolio(factor_data, weights=None):
    """Create a multifactor portfolio from factor returns with given weights"""
    if weights is None:
        # Equal weights if none provided
        n_factors = len(factor_data)
        weights = {factor: 1/n_factors for factor in factor_data.keys()}
    
    # Find common date range across all factors
    all_dates = set.intersection(*[set(df['date']) for df in factor_data.values()])
    common_dates = sorted(list(all_dates))
    
    # Initialize result DataFrame with common dates
    result = pd.DataFrame({'date': common_dates})
    
    # Get return columns (should be consistent across all factors)
    first_factor = list(factor_data.keys())[0]
    return_cols = [col for col in factor_data[first_factor].columns if col.startswith('ret_')]
    
    # Initialize return columns with zeros
    for col in return_cols:
        result[col] = 0.0
    
    # Calculate weighted returns
    for factor, df in factor_data.items():
        # Align dates
        df_aligned = df[df['date'].isin(common_dates)].copy()
        df_aligned.set_index('date', inplace=True)
        
        weight = weights[factor]
        for col in return_cols:
            result.set_index('date', inplace=True)
            result[col] += df_aligned[col] * weight
            result.reset_index(inplace=True)
    
    # Calculate cumulative return
    result.set_index('date', inplace=True)
    result['cumulative_return'] = (1 + result[return_cols[0]]).cumprod()
    result.reset_index(inplace=True)
    
    return result

def main():
    #st.set_page_config(page_title="Global Q Explorer", layout="wide")
    st.title("Global Q Explorer")

    # Load Data
    data_loader = DataLoader()
    data_dict = data_loader.load_data_directory("data")
    
    # Sidebar Controls
    st.sidebar.header("Data Selection")
    
    # Get available groups excluding market portfolio
    available_groups = [g for g in data_loader.get_available_groups(data_dict) 
                       if g != 'market_portfolio']
    
    # Create expandable sections for each group
    selected_factors = {}
    
    for group in available_groups:
        group_display = GROUP_NAMES.get(group, group)
        with st.sidebar.expander(f"{group_display}"):
            group_factors = data_loader.get_available_factors(data_dict, group)
            factor_display_dict = create_factor_display_dict(group_factors, group)
            
            selected_displays = st.multiselect(
                "Select Factors",
                options=sorted(factor_display_dict.keys()),
                key=f"factor_select_{group}"
            )
            
            if selected_displays:
                selected_factors[group] = [factor_display_dict[display] for display in selected_displays]
    
    # Check if any factors are selected
    if not any(selected_factors.values()):
        st.warning("Please select at least one factor from any group.")
        st.stop()
    
    # Market Cap Selection
    all_market_caps = set()
    for group, factors in selected_factors.items():
        for factor in factors:
            market_caps = data_loader.get_available_market_caps(data_dict, group, factor)
            all_market_caps.update(market_caps)
    
    selected_market_cap = st.sidebar.selectbox(
        "Select Market Cap Rank",
        sorted(list(all_market_caps)),
        index=2,
        format_func=lambda x: f"Rank {x}"
    )
    
    # Factor Rank Selection
    factor_ranks = {}
    for group, factors in selected_factors.items():
        for factor in factors:
            available_ranks = data_loader.get_available_ranks(data_dict, group, factor)
            if available_ranks:
                display_name = get_display_name(f"{group}/{factor}")
                st.sidebar.subheader(f"Ranks for {display_name}")
                factor_ranks[(group, factor)] = {}
                for rank_col, rank_values in available_ranks.items():
                    rank_display = format_rank_name(rank_col)
                    default_index = 4  # middle rank
                    selected_rank = st.sidebar.selectbox(
                        f"Select {rank_display} Rank",
                        rank_values,
                        index=default_index,
                        key=f"{group}_{factor}_{rank_col}",
                        format_func=lambda x: f"Rank {x}"
                    )
                    factor_ranks[(group, factor)][rank_col] = selected_rank
    
    # Load selected factor data
    factor_data = {}
    for group, factors in selected_factors.items():
        group_data = data_loader.get_factor_data(
            data_dict, 
            group, 
            factors, 
            selected_market_cap,
            {f: factor_ranks[(group, f)] for f in factors if (group, f) in factor_ranks}
        )
        # Add group prefix to factor names to avoid duplicates
        factor_data.update({f"{group}/{f}": data for f, data in group_data.items()})
    
    # Load market portfolio data for the selected market cap
    market_data = data_loader.get_market_portfolio(data_dict, 10)#selected_market_cap)

    #st.write(factor_data)
    #st.write(market_data)
    
    # Return Type Selection
    return_columns = data_loader.get_return_columns()
    selected_return = st.sidebar.selectbox(
        "Select Return Type",
        return_columns,
        index=0,
        format_func=lambda x: "Value-weighted" if x == "ret_vw" else "Equal-weighted"
    )

    # Get common date range across all selected factors
    min_date = max(df['date'].min() for df in factor_data.values())
    max_date = min(df['date'].max() for df in factor_data.values())
    
    # Filter data by date range and add display names
    filtered_data = {}
    for factor, df in factor_data.items():
        display_name = get_display_name(factor)
        filtered_df = df[df['date'].between(min_date, max_date)].copy()
        filtered_df['cumulative_return'] = (1 + filtered_df[selected_return]).cumprod()
        filtered_data[display_name] = filtered_df
    
    if market_data is not None:
        market_data = market_data[market_data['date'].between(min_date, max_date)]

    # Before visualization
    for factor in filtered_data:
        if 'date' not in filtered_data[factor].columns and isinstance(filtered_data[factor].index, pd.DatetimeIndex):
            filtered_data[factor] = filtered_data[factor].reset_index()

    # Add multifactor portfolio section
    st.sidebar.markdown("---")
    st.sidebar.subheader("Multifactor Portfolio")
    show_weights = st.sidebar.checkbox("Modify Portfolio Weights", value=False)
    
    # Calculate default equal weights
    n_factors = len(filtered_data)
    default_weight = 1/n_factors
    
    # Create weight inputs if requested
    portfolio_weights = {}
    if show_weights:
        st.sidebar.markdown("Enter weights (they will be normalized to sum to 1)")
        total_weight = 0
        for factor in sorted(filtered_data.keys()):
            weight = st.sidebar.number_input(
                f"Weight for {factor}",
                min_value=0.0,
                max_value=1.0,
                value=default_weight,
                step=0.1,
                key=f"weight_{factor}"
            )
            portfolio_weights[factor] = weight
            total_weight += weight
        
        # Normalize weights
        if total_weight > 0:
            portfolio_weights = {k: v/total_weight for k, v in portfolio_weights.items()}
    else:
        portfolio_weights = {factor: default_weight for factor in filtered_data.keys()}
    
    # Create multifactor portfolio
    if filtered_data:
        multifactor_data = create_multifactor_portfolio(filtered_data, portfolio_weights)
        if not multifactor_data.empty:
            filtered_data["Multifactor Portfolio"] = multifactor_data
        else:
            st.warning("Could not create multifactor portfolio - no common dates found across factors")

    # Display current weights
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Current Portfolio Weights**")
    weights_df = pd.DataFrame(list(portfolio_weights.items()), columns=['Factor', 'Weight'])
    weights_df['Weight'] = weights_df['Weight'].map(lambda x: f"{x:.2%}")
    st.sidebar.dataframe(weights_df, hide_index=True)

    # Add tabs for different analyses
    #tab1, tab2, tab3 = st.tabs(["Basic Analysis", "Rolling Analysis", "Quantile Analysis"])
    tab1, tab2 = st.tabs(["Basic Analysis", "Rolling Analysis"])
    
    with tab1: 
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Total Return Performance")
            fig = Visualizer.create_multi_performance_plot(
                filtered_data, 
                market_data=market_data,
                return_col=selected_return,
                title=f"Portfolio Performance (Market Cap Rank {selected_market_cap})"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Excess Return Performance")
            if market_data is not None:
                # Set date as index for alignment if not already
                if not isinstance(market_data.index, pd.DatetimeIndex):
                    market_data = market_data.set_index('date')
                for factor in filtered_data:
                    if not isinstance(filtered_data[factor].index, pd.DatetimeIndex):
                        filtered_data[factor] = filtered_data[factor].set_index('date')
                
                fig = Visualizer.create_excess_return_plot(
                    filtered_data,
                    market_data,
                    return_col=selected_return,
                    title=f"Excess Returns vs Market (Market Cap Rank {selected_market_cap})"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Market data required for excess return analysis")
        
        # Correlation matrix below the plots
        st.subheader("Excess Return Correlations")
        if market_data is not None:
            corr_matrix = DataProcessor.calculate_multi_correlation_matrix(
                filtered_data, market_data, selected_return
            )
            fig = Visualizer.create_heatmap(corr_matrix)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Market data required for excess return correlations")
    
    with tab2:
        # Let user select which factor to analyze in detail
        selected_display_name = st.selectbox(
            "Select Factor for Detailed Analysis",
            options=sorted(filtered_data.keys())
        )
        
        # Add date range selection
        st.subheader("Analysis Period Selection")
        
        # Convert dates to datetime for the slider
        date_range = pd.date_range(min_date, max_date, freq='M')
        
        # Create two columns for the date range inputs
        date_col1, date_col2 = st.columns(2)
        
        with date_col1:
            start_date = st.date_input(
                "Start Date",
                value=min_date,
                min_value=min_date,
                max_value=max_date
            )
        
        with date_col2:
            end_date = st.date_input(
                "End Date",
                value=max_date,
                min_value=min_date,
                max_value=max_date
            )
        
        # Filter data for selected date range
        selected_factor_data = filtered_data[selected_display_name].copy()
        
        # Reset index if date is the index
        if isinstance(selected_factor_data.index, pd.DatetimeIndex):
            selected_factor_data = selected_factor_data.reset_index()
        
        # Filter by date range
        selected_factor_data = selected_factor_data[
            selected_factor_data['date'].between(pd.Timestamp(start_date), pd.Timestamp(end_date))
        ]
        
        if market_data is not None:
            # Reset index if date is the index
            if isinstance(market_data.index, pd.DatetimeIndex):
                selected_market_data = market_data.reset_index()
            else:
                selected_market_data = market_data.copy()
            
            selected_market_data = selected_market_data[
                selected_market_data['date'].between(pd.Timestamp(start_date), pd.Timestamp(end_date))
            ]
        
        # Rolling Analysis
        st.subheader("Rolling Statistics Analysis")
        
        window = st.slider(
            "Rolling Window (months)",
            min_value=3,
            max_value=36,
            value=12
        )
        
        # Set date as index for rolling calculations
        selected_factor_data.set_index('date', inplace=True)
        if market_data is not None:
            selected_market_data.set_index('date', inplace=True)
        
        rolling_stats = Analysis.calculate_rolling_stats(
            selected_factor_data, 
            return_col=selected_return, 
            window=window
        )
        
        fig = Visualizer.create_rolling_stats_plot(
            selected_factor_data, 
            rolling_stats, 
            return_col=selected_return,
            title=f"Rolling Statistics: {selected_display_name} ({start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')})"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Drawdown Analysis
        drawdown = Analysis.calculate_drawdown(
            selected_factor_data, 
            return_col=selected_return
        )
        fig = Visualizer.create_drawdown_plot(
            selected_factor_data, 
            drawdown, 
            return_col=selected_return,
            title=f"Drawdown Analysis: {selected_display_name} ({start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')})"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Market Comparison Section
        st.subheader("Market Relative Analysis")
        
        if market_data is not None:
            relative_stats = Analysis.calculate_relative_performance(
                selected_factor_data, 
                return_col=selected_return, 
                market_data=selected_market_data, 
                window=window
            )
            
            # Relative Performance Plot
            fig = Visualizer.create_relative_performance_plot(
                selected_factor_data, 
                relative_stats, 
                market_data=selected_market_data,
                return_col=selected_return,
                title=f"Relative Performance: {selected_display_name} vs Market ({start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')})"
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Tracking Error Plot
            fig = Visualizer.create_tracking_error_plot(
                selected_factor_data, 
                relative_stats,
                title=f"Tracking Error Analysis: {selected_display_name} ({start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')})"
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Market Relative Statistics
            st.subheader("Market Relative Statistics")
            market_stats = Analysis.calculate_market_relative_statistics(
                selected_factor_data, 
                return_col=selected_return,
                market_data=selected_market_data
            )
            
            # Create a DataFrame with both factor and market statistics
            combined_stats = pd.DataFrame({
                f"{selected_display_name}": market_stats,
                "Market Portfolio": DataProcessor.calculate_statistics(
                    selected_market_data,
                    return_col=selected_return
                )
            })
            
            # Format the statistics based on the type of metric
            formatted_stats = combined_stats.copy()
            
            # Define formatting rules for different types of metrics
            percentage_metrics = [
                'Annual Alpha (%)', 'Mean Return (% p.a.)', 
                'Excess Return (% p.a.)', 'Tracking Error (% p.a.)', 
                'Volatility (% p.a.)'
            ]
            
            ratio_metrics = [
                'Beta', 'Information Ratio', 'Sharpe Ratio'
            ]
            
            correlation_metrics = [
                'Correlation', 'R-Squared'
            ]
            
            count_metrics = [
                'Average N Stocks'
            ]
            
            distribution_metrics = [
                'Skewness', 'Kurtosis'
            ]
            
            for col in formatted_stats.columns:
                for idx in formatted_stats.index:
                    value = formatted_stats.loc[idx, col]
                    if pd.isna(value) or value is None:
                        formatted_stats.loc[idx, col] = "N/A"
                    else:
                        if idx in percentage_metrics:
                            # Format percentages with 2 decimal places
                            formatted_stats.loc[idx, col] = f"{float(value) * 100:,.2f}%"
                        elif idx in ratio_metrics:
                            # Format ratios with 2 decimal places
                            formatted_stats.loc[idx, col] = f"{float(value):,.2f}"
                        elif idx in correlation_metrics:
                            # Format correlations with 3 decimal places
                            formatted_stats.loc[idx, col] = f"{float(value):,.3f}"
                        elif idx in count_metrics:
                            # Format counts as integers
                            formatted_stats.loc[idx, col] = f"{int(value):,}"
                        elif idx in distribution_metrics:
                            # Format distribution metrics with 3 decimal places
                            formatted_stats.loc[idx, col] = f"{float(value):,.3f}"
                        else:
                            # Default format with 4 decimal places
                            formatted_stats.loc[idx, col] = f"{float(value):,.4f}"
            
            st.dataframe(
                formatted_stats,
                use_container_width=True
            )
        else:
            st.warning("Market portfolio data not available for comparison.")
    
    # with tab3:
    #     # Quantile Analysis
    #     st.subheader("Factor Quantile Analysis")
        
    #     selected_display_name_quantile = st.selectbox(
    #         "Select Factor for Quantile Analysis",
    #         options=sorted(filtered_data.keys()),
    #         key="quantile_factor"
    #     )
        
    #     n_quantiles = st.select_slider(
    #         "Number of Quantiles",
    #         options=[3, 5, 10],
    #         value=5
    #     )
        
    #     quantile_stats = Analysis.factor_quantile_analysis(
    #         filtered_data[selected_display_name_quantile], 
    #         return_col=selected_return, 
    #         n_quantiles=n_quantiles
    #     )
    #     st.dataframe(quantile_stats)

    # Statistics Table
    st.subheader("Portfolio Statistics")
    
    # Calculate statistics for all selected portfolios
    stats_dict = {}
    for factor_name, df in filtered_data.items():
        stats = DataProcessor.calculate_statistics(
            df, 
            return_col=selected_return,
            market_data=market_data if market_data is not None else None
        )
        stats_dict[factor_name] = stats
    
    # Create and format the statistics DataFrame
    stats_df = pd.DataFrame(stats_dict)
    
    # Format the statistics table
    formatted_stats = stats_df.copy()
    for col in formatted_stats.columns:
        formatted_stats[col] = formatted_stats[col].apply(
            lambda x: f"{x:.2f}" if pd.notnull(x) and isinstance(x, (int, float)) else x
        )
    
    # Display statistics with better formatting
    st.dataframe(
        formatted_stats,
        use_container_width=True,
        height=400
    )

if __name__ == "__main__":
    main() 