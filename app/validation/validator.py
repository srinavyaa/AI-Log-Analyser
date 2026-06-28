VALID_LOG_LEVELS = {"INFO", "WARNING", "ERROR"}


def validate_log(log):
    """
    Validate a log before inserting into the database.
    Returns True if valid, otherwise False.
    """

    required_fields = ["timestamp", "log_level", "source", "message"]

    # Check if all required fields exist
    for field in required_fields:
        if field not in log:
            print(f"Validation Error: Missing field '{field}'")
            return False

    # Check for empty values
    for field in required_fields:
        if log[field] is None or log[field] == "":
            print(f"Validation Error: '{field}' cannot be empty")
            return False

    # Check log level
    if log["log_level"] not in VALID_LOG_LEVELS:
        print(f"Validation Error: Invalid log level '{log['log_level']}'")
        return False

    return True