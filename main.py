from typing import List, Dict, Union
from models import Transaction, CategoryInfo


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


def get_spending_by_category(
    transaction: Transaction, 
    category_dict: Dict[str, CategoryInfo]
) -> Dict[str, CategoryInfo]:
    """Get spending info for transaction and update category dictionary with count.
    
    Args:
        transaction (Transaction): Transaction from which we get spending info
        category_dict (Dict[str, CategoryInfo]): Dictionary to hold spending by category info

    Returns:
        Updated category dict with new amount and count number
    """
    amount = float(transaction['amount'])
    category = transaction['category']

    if category not in category_dict:
        category_dict[category] = {'amount': 0.0, 'count': 0}
    category_dict[category]['amount'] += amount
    category_dict[category]['count'] += 1

    return category_dict


def get_income_by_payer_for_salary(
    transaction: Transaction,
    salary_dict: Dict[str, CategoryInfo]
) -> Dict[str, CategoryInfo]:
    """Get salary info per payer and update salary dictionary with count.
    
    Args:
        transaction (Transaction): Transaction from which we get salary info
        salary_dict (Dict[str, CategoryInfo]): Dictionary to hold salary by payer

    Returns:
        Updated salary dict with new amount and count number
    """
    amount = float(transaction['amount'])
    description = transaction['description']

    if description not in salary_dict:
        salary_dict[description] = {'amount': 0.0, 'count': 0}
    salary_dict[description]['amount'] += amount
    salary_dict[description]['count'] += 1
    
    return salary_dict