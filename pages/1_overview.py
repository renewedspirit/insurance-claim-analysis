import streamlit as st
import pandas as pd

st.title("📊 Data Overview")

df = pd.read_csv("data/insurance_data_clean.csv")

st.markdown("""
This page provides an overview of the insurance dataset, including key statistics
and a summary of the data used in the analysis.
""")

# KPI metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", f"{len(df):,}")
col2.metric("Average Claim (£)", f"{df['claim'].mean():,.2f}")
col3.metric("Median Claim (£)", f"{df['claim'].median():,.2f}")

smoker_pct = (df["smoker"].astype(str).str.lower() == "yes").mean() * 100
col4.metric("Smokers (%)", f"{smoker_pct:.1f}%")

st.divider()

st.subheader("Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("Missing Values Check")
st.write(df.isnull().sum())
