from typing import List, Dict, Union
from models import Transaction


def normalise_transactions(transactions):
    pass


def get_total_income(transactions: List[Transaction]) -> Dict[str, Union[float, int]]:
    """Get sum of and number of positive transaction amounts.

    Args:
        transactions (List[Transaction]): List of transaction dictionaries

    Returns:
        Dictionary object holding total income and number of transactions
    """
    total_income = 0.0
    num_transactions = 0

    for transaction in transactions:
        amount = float(transaction['amount'])
        if amount > 0:
            total_income += amount
            num_transactions += 1

    return {
        'total_income': total_income,
        'num_transactions': num_transactions
    }


def get_total_spending(transactions: List[Transaction]) -> Dict[str, Union[float, int]]:
    """Get sum of and number of negative transaction amounts.

    Args:
        transactions (List[Transaction]): List of transaction dictionaries

    Returns:
        Dictionary object holding total spending and number of transactions
    """
    pass