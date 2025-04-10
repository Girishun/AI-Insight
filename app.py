import streamlit as st
from etl import run_etl  # Make sure `etl.py` has a `run_etl()` function

st.title("ETL Dashboard")

if st.button("Run ETL Now"):
    st.write("Running ETL...")
    result = run_etl()
    st.success("ETL Complete!")
