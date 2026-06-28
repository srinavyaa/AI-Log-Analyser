import psycopg
from app.config.settings import settings


def get_connection():
    """
    Creates and returns a PostgreSQL database connection.
    """

    connection = psycopg.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD
    )

    return connection