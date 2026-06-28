from app.database.insert_log import insert_log
from app.validation.validator import validate_log
from app.preprocessing.preprocessor import preprocess_log
from app.features.feature_engineering import engineer_features


def ingest_log(log):
    """
    Receives a log, validates it, and stores it in the database.
    """

    # Step 1: Validate
    if not validate_log(log):
        print("❌ Invalid log rejected!")
        return

# Step 2: Preprocess
    log = preprocess_log(log)

# Step 3: Feature Engineering
    features = engineer_features(log)
    print("Extracted Features:", features)

# Step 4: Store in Database
    insert_log(
        log["timestamp"],
        log["log_level"],
        log["source"],
        log["message"]
    )

print("✅ Log ingested successfully!")