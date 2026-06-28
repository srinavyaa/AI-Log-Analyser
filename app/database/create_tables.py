from app.database.connection import get_connection


def create_logs_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            log_level VARCHAR(20) NOT NULL,
            source VARCHAR(100) NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Logs table created successfully!")


if __name__ == "__main__":
    create_logs_table()