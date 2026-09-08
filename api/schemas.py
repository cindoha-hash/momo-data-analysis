from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    amount: float
    date: str
    phone: str
    category: str
    raw_message: str
