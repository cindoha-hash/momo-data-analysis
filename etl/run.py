"""
Main ETL pipeline: parse -> clean -> categorize -> load -> export JSON
"""
from etl.parse_xml import parse_xml
from etl.clean_normalize import clean_transactions
from etl.categorize import categorize_all
from etl.load_db import create_tables, load_transactions


def run():
    print("Step 1: Parsing XML...")
    raw_data = parse_xml()

    print("Step 2: Cleaning data...")
    cleaned_data = clean_transactions(raw_data)

    print("Step 3: Categorizing transactions...")
    categorized_data = categorize_all(cleaned_data)

    print("Step 4: Loading into database...")
    create_tables()
    load_transactions(categorized_data)

    print("ETL pipeline complete.")


if __name__ == "__main__":
    run()
