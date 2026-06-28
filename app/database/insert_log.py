from app.database.connection import get_connection
from datetime import datetime


def insert_log(timestamp, log_level, source, message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO logs (timestamp, log_level, source, message)
        VALUES (%s, %s, %s, %s)
        """,
        (timestamp, log_level, source, message)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Log inserted successfully!")


if __name__ == "__main__":
    insert_log(
        datetime.now(),
        "INFO",
        "Server-01",
        "Application started successfully."
    )