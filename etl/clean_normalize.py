"""
Cleans and normalizes raw transaction data:
amounts, dates, phone numbers.
Implementation to be completed in Phase 2.
"""
from dateutil import parser as date_parser


def normalize_amount(raw_amount: str) -> float:
    # TODO: strip currency symbols/commas, convert to float
    return float(raw_amount.replace(",", "").strip())


def normalize_date(raw_date: str):
    # TODO: handle multiple date formats from SMS text
    return date_parser.parse(raw_date)


def normalize_phone(raw_phone: str) -> str:
    # TODO: standardize phone number format
    return raw_phone.strip()


def clean_transactions(transactions: list) -> list:
    cleaned = []
    for txn in transactions:
        # TODO: apply normalization functions to each field
        cleaned.append(txn)
    return cleaned
