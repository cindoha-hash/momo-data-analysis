import os

# Paths used by the import pipeline.
XML_INPUT_PATH = os.getenv("XML_INPUT_PATH", "data/raw/momo.xml")
DATABASE_PATH = os.getenv("DATABASE_URL", "data/db.sqlite3")
DASHBOARD_JSON_PATH = os.getenv("DASHBOARD_JSON_PATH", "data/processed/dashboard.json")
LOG_PATH = "data/logs/etl.log"
DEAD_LETTER_PATH = "data/logs/dead_letter/"

# Labels used when classifying transaction messages.
CATEGORIES = [
    "deposit",
    "withdrawal",
    "transfer",
    "payment",
    "airtime",
    "other",
]
