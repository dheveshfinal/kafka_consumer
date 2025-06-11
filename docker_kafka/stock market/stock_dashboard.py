import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")
st.title("📈 Real-Time Stock Dashboard")

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv('latest_stock_data.csv')
        latest = df.groupby('ticker').last().reset_index()

        with placeholder.container():
            st.subheader("Latest Stock Prices")
            st.dataframe(latest.sort_values("price", ascending=False))

        time.sleep(2)
    except FileNotFoundError:
        st.warning("Waiting for stock data...")
        time.sleep(1)
