from pathlib import Path
import yahoo_fin.stock_info as si
import streamlit as st


def get_data(ticker: str):

    new_path = Path('.') / 'data'
    new_path.mkdir(parents=True, exist_ok=True)

    price_data = None
    try:
        price_data = si.get_data(ticker=ticker, index_as_date=False)
        price_data.to_csv(new_path / f'{ticker}_prices.csv')
    except Exception as e:
        st.write(e)

    return price_data




# df_ibex = si.get_data(ticker='^IBEX', start_date='1999-12-31', end_date='2022-04-22', index_as_date=False)
# df_market_price = pd.pivot(data=df_ibex, index=['date'], columns=['ticker'], values=['adjclose'])
# df_market_price = pd.DataFrame(df_market_price.values, index=df_market_price.index,
#                                columns=df_market_price.columns.get_level_values(1).to_list())
