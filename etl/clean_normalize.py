"""Normalize amounts, dates, and phone numbers in transaction records."""
from dateutil import parser as date_parser


def normalize_amount(raw_amount: str) -> float:
    return float(raw_amount.replace(",", "").strip())


def normalize_date(raw_date: str):
    return date_parser.parse(raw_date)


def normalize_phone(raw_phone: str) -> str:
    return raw_phone.strip()


def clean_transactions(transactions: list) -> list:
    cleaned = []
    for txn in transactions:
        cleaned.append(txn)
    return cleaned
