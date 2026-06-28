import time
import random
from datetime import datetime

from app.ingestion.ingest import ingest_log

levels = ["ERROR", "ERROR", "WARNING", "INFO"]

messages = {
    "INFO": ["User logged in", "Page loaded", "Request success"],
    "ERROR": ["Database failed", "Timeout occurred", "Service unavailable"],
    "WARNING": ["High memory usage", "Slow response"]
}

sources = [
    "Authentication Service",
    "API Gateway",
    "Database",
    "Web Server"
]

while True:
    log = {
    "timestamp": datetime.now(),
    "log_level": "ERROR",
    "source": "Web Server",
    "message": None
}
    log["message"] = random.choice(messages[log["log_level"]])

    ingest_log(log)

    print("Generated:", log)

    time.sleep(2)