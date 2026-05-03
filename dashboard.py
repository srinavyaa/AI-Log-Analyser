import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Log Analyzer", layout="wide")

st.title("AI Log Analyzer Dashboard")

# Read logs
with open("app.log", "r") as file:
    logs = file.readlines()

# Read anomalies
with open("anomalies.log", "r") as file:
    anomalies = file.readlines()

# Count log types
info_count = sum(1 for log in logs if "INFO" in log)
warning_count = sum(1 for log in logs if "WARNING" in log)
error_count = sum(1 for log in logs if "ERROR" in log)

# Sidebar
st.sidebar.title("Project Info")
st.sidebar.write("Real-Time AI Log Monitoring")
st.sidebar.write("Machine Learning: Isolation Forest")

# Metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Logs", len(logs))

with col2:
    st.metric("Total Anomalies", len(anomalies))

# Pie chart
st.subheader("Log Distribution")

labels = ["INFO", "WARNING", "ERROR"]
sizes = [info_count, warning_count, error_count]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%")
ax.axis("equal")

st.pyplot(fig)

# Recent logs
st.subheader("Recent Logs")
for log in logs[-10:]:
    if "ERROR" in log:
        st.error(log.strip())
    elif "WARNING" in log:
        st.warning(log.strip())
    else:
        st.success(log.strip())

# Recent anomalies
st.subheader("Recent Anomalies")
for anomaly in anomalies[-10:]:
    st.error(anomaly.strip())