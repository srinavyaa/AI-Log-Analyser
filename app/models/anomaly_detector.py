import pandas as pd
from sklearn.ensemble import IsolationForest
from app.database.connection import get_connection


def detect_anomalies():
    conn = get_connection()

    query = """
    SELECT timestamp, log_level, source, message
    FROM logs
    """

    df = pd.read_sql(query, conn)
    conn.close()

    # Feature engineering for the model
    df["message_length"] = df["message"].str.len()
    df["is_error"] = (df["log_level"] == "ERROR").astype(int)

    X = df[["message_length", "is_error"]]

    # Train Isolation Forest
    model = IsolationForest(contamination=0.20, random_state=42)
    df["anomaly"] = model.fit_predict(X)
    print(df["anomaly"].value_counts())
    # Return only anomalies
    anomalies = df[df["anomaly"] == -1]

    return anomalies