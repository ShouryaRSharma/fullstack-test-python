from typing import Any, Dict, Union


def normalise_transactions(transactions):
    pass


def get_total_income(transactions: Dict[str, Any]) -> Dict[str, Union[float, int]]:
    """Get total of and number of positive transaction amounts.
    
    Args:
        transactions (Dict[str, Any]): Dictionary object holding transaction data

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