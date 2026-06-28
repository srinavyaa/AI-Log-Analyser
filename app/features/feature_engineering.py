def engineer_features(log):
    """
    Convert raw log data into ML-friendly features.
    """

    features = {
        "hour_of_day": log["timestamp"].hour,
        "is_error": 1 if log["log_level"] == "ERROR" else 0,
        "message_length": len(log["message"]),
        "source_length": len(log["source"])
    }

    return features