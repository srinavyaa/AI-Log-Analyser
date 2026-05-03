import time
import random

levels = ["ERROR", "ERROR", "WARNING", "INFO"]

messages = {
    "INFO": ["User logged in", "Page loaded", "Request success"],
    "ERROR": ["Database failed", "Timeout occurred", "Service unavailable"],
    "WARNING": ["High memory usage", "Slow response"]
}

while True:
    level = random.choice(levels)
    message = random.choice(messages[level])

    log_line = f"{level}: {message}\n"

    with open("app.log", "a") as f:
        f.write(log_line)

    print("Generated:", log_line.strip())

    time.sleep(2)