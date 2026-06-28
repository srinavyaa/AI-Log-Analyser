from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

class Settings:
    APP_NAME = "AI Log Analyser"
    APP_VERSION = "2.0"

    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "ai_log_analyser")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")

settings = Settings()