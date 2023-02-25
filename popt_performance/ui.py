import os
from pathlib import Path
import streamlit as st
from popt_performance.data import get_data
import pandas as pd
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Stocks prices dashboard", layout="wide")

DATA_DIR = Path('.') / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_candlestick_chart(x: pd.DataFrame, ma_type: str, ma_length: int, plot_days: int):
    _tmp = x.copy()
    if ma_type == 'Simple':
        _tmp['ma'] = _tmp['adjclose'].rolling(int(ma_length)).mean()
    else:
        _tmp['ma'] = _tmp['adjclose'].ewm(int(ma_length)).mean()

    _tmp = _tmp[-int(plot_days):]

    fig = go.Figure()

    # fig.add_trace(
    #     go.Candlestick(
    #         x=price_data['date'],
    #         open=price_data['open'],
    #         high=price_data['high'],
    #         low=price_data['low'],
    #         close=price_data['close'],
    #         showlegend=False,
    #     )
    # )

    fig.add_trace(
        go.Scatter(
            x=_tmp['date'],
            y=_tmp['adjclose'],
            mode='lines+markers',
            name='Prices'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=_tmp['date'],
            y=_tmp['ma'],
            mode='lines',
            name=f'{int(ma_length)} Period {ma_type} Moving Average'
        )
    )

    fig.update_xaxes(
        rangebreaks=[{'bounds': ['sat', 'mon']}],
        rangeslider_visible=False,
    )

    fig.update_layout(
        legend={'x': 0, 'y': -0.05, 'orientation': 'h'},
        margin={'l': 50, 'r': 50, 'b': 50, 't': 25},
        width=1200,
        height=600,
    )

    return fig


# Sidebar controls -----------------------------------------------------------
ticker = st.sidebar.text_input(
    label='Stock ticker',
    value='LDA.MC',
)

ma_type = st.sidebar.selectbox(
    label='Moving average type',
    options=['Simple', 'Exponential'],
)

ma_length = st.sidebar.number_input(
    label='Moving average length',
    value=10,
    min_value=2,
    step=1,
)

plot_days = st.sidebar.number_input(
    label='Chart viewing length',
    value=120,
    min_value=1,
    step=1,
)

st.sidebar.button(
    label='Update data',
    on_click=get_data,
    kwargs={'ticker': ticker},
)

# The dashboard plots --------------------------------------------------------



st.header(f'{ticker} Dashboard 💵')

# Check if we have the stock data, if not, download it
if os.path.isfile(DATA_DIR / f'{ticker}_prices.csv'):
    price_data = pd.read_csv(DATA_DIR / f'{ticker}_prices.csv', index_col=0, parse_dates=['date'])
else:
    price_data = get_data(ticker)

# with st.expander('Open to see the stock information'):
#     st.write(yf.Ticker('TSLA').info['longBusinessSummary'])


st.subheader('Price Chart 📈')
st.plotly_chart(
    get_candlestick_chart(price_data, ma_type, ma_length, plot_days)
)

st.subheader('Price Table 📊')
st.write(price_data)
