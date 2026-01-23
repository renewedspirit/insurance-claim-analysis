import streamlit as st
import pandas as pd

st.set_page_config(page_title="Insurance Claims Dashboard", layout="wide")

st.title("🏥 Insurance Claims Dashboard")

st.markdown("""
This app explores insurance claim data using **data analysis, visualisation, and a simple machine learning model**.

Use the **sidebar** to navigate:
- 📊 Overview
- 🧪 Hypotheses
- 🤖 ML Predictor
""")

df = pd.read_csv("data/insurance_data_clean.csv")

st.subheader("Quick Preview")
st.dataframe(df.head(10), use_container_width=True)
