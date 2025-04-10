import streamlit as st
from etl import run_etl

st.title("🧠 Market News ETL")

symbol = st.text_input("Enter stock symbol (e.g., AAPL):", "AAPL")

if st.button("Run ETL"):
    with st.spinner("Running ETL pipeline..."):
        output = run_etl(symbol)
        st.success("ETL complete!")
        st.markdown(f"### Insight for **{symbol}**:\n\n{output}")
