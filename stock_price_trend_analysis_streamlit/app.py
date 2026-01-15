
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Stock Price Trend Analysis", layout="wide")

st.title("📈 Stock Price Trend Analysis Dashboard")
st.markdown("Analyze stock price trends using interactive visualizations.")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "stock_prices.csv")

df = pd.read_csv(DATA_PATH)

st.sidebar.header("Filters")
company = st.sidebar.multiselect(
    "Select Company",
    df["company"].unique(),
    df["company"].unique()
)

df = df[df["company"].isin(company)]

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Closing Price Trend")
for c in df["company"].unique():
    temp = df[df["company"] == c]
    st.line_chart(temp.set_index("date")["close"])

st.subheader("Daily Summary")
idx = st.slider("Select Row Index", 0, len(df) - 1)
st.write(df.iloc[idx])
