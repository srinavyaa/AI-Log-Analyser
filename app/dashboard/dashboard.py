import sys
from pathlib import Path
from app.models.anomaly_detector import detect_anomalies

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))


import streamlit as st
import pandas as pd

from app.database.connection import get_connection

st.set_page_config(page_title="AI Log Analyzer", layout="wide")

st.title("📊 AI Log Analyzer Dashboard")

conn = get_connection()

query = """
SELECT *
FROM logs
ORDER BY timestamp DESC
"""

df = pd.read_sql(query, conn)
anomalies = detect_anomalies()

# Metrics
st.metric("Total Logs", len(df))
st.metric("Errors", len(df[df["log_level"] == "ERROR"]))
st.metric("Anomalies", len(anomalies))

st.divider()

st.subheader("Recent Logs")
st.sidebar.header("Filters")

selected_level = st.sidebar.selectbox(
    "Select Log Level",
    ["ALL"] + sorted(df["log_level"].unique().tolist())
)

if selected_level != "ALL":
    filtered_df = df[df["log_level"] == selected_level]
else:
    filtered_df = df
st.dataframe(filtered_df.head(20), width="stretch")

st.subheader("Log Level Distribution")
st.bar_chart(filtered_df["log_level"].value_counts())
st.subheader("Detected Anomalies")

st.dataframe(
    anomalies,
    width="stretch"
)