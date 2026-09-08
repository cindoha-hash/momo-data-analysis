"""Assign a transaction category from the message text."""


def categorize_transaction(txn: dict) -> str:
    """Return the first category matched in a transaction message."""
    message = txn.get("message", "").lower()

    if "deposit" in message:
        return "deposit"
    elif "withdraw" in message:
        return "withdrawal"
    elif "transfer" in message:
        return "transfer"
    elif "payment" in message:
        return "payment"
    elif "airtime" in message:
        return "airtime"
    return "other"


def categorize_all(transactions: list) -> list:
    for txn in transactions:
        txn["category"] = categorize_transaction(txn)
    return transactions
