def preprocess_log(log):
    """
    Clean and standardize log data before storing it.
    """

    # Standardize log level
    log["log_level"] = log["log_level"].upper().strip()

    # Standardize source
    log["source"] = log["source"].upper().strip()

    # Clean message
    log["message"] = log["message"].strip()

    return log