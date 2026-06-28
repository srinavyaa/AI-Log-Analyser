import pandas as pd
from app.database.connection import get_connection
import matplotlib.pyplot as plt


def load_logs():

    conn = get_connection()

    query = "SELECT * FROM logs"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


if __name__ == "__main__":

    df = load_logs()

    print(df.head())
    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

    print("\nSummary:")
    print(df.describe(include="all"))
    # Plot log level distribution
    df["log_level"].value_counts().plot(kind="bar")

    plt.title("Log Level Distribution")
    plt.xlabel("Log Level")
    plt.ylabel("Count")

    plt.show()