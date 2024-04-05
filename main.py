from typing import List, Dict, Union
from models import Transaction


def normalise_transactions(transactions):
    pass


def get_total_amount(transactions: List[Transaction]) -> Dict[str, Union[float, int]]:
    """Get sum of and number of positive and negative transaction amounts.

    Args:
        transactions (List[Transaction]): List of transaction dictionaries

    Returns:
        Dictionary object holding total income, total spending, and number of transactions
    """
    total_income = 0.0
    total_spending = 0.0
    num_income_transactions = 0
    num_spending_transactions = 0

    for transaction in transactions:
        amount = float(transaction['amount'])
        if amount > 0:
            total_income += amount
            num_income_transactions += 1
        elif amount < 0:
            total_spending += amount
            num_spending_transactions += 1

    return {
        'total_income': total_income,
        'total_spending': total_spending,
        'num_income_transactions': num_income_transactions,
        'num_spending_transactions': num_spending_transactions
    }