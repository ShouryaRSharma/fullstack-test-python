from typing_extensions import TypedDict


class Transaction(TypedDict):
    id: str
    created_at: str
    updated_at: str
    description: str
    amount: str
    currency_code: str
    category: str
    date: str


class CategoryInfo(TypedDict):
    amount: float
    count: int
