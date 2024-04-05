from typing import List, Dict, Union
from models import Transaction, CategoryInfo

def normalise_transactions(
    transactions: List[Transaction]
) -> Dict[str, Union[float, int, Dict[str, CategoryInfo]]]:
    """Analyse transaction data to get total income, spending, and group by categories.

    Args:
        transactions (List[Transaction]): List of transaction dictionaries

    Returns:
        Dictionary object holding total income, total spending, num transactions and category info on spending and salary.
    """
    total_income = 0.0
    total_spending = 0.0
    num_income_transactions = 0
    num_spending_transactions = 0
    spending_by_category: Dict[str, CategoryInfo] = {}
    income_by_payer_for_salary: Dict[str, CategoryInfo] = {}

    for transaction in transactions:
        amount = round(float(transaction['amount']), 2)
        category = transaction["category"]

        if amount > 0:
            total_income += amount
            num_income_transactions += 1
            if category == "Salary":
                income_by_payer_for_salary = get_income_by_payer_for_salary(
                    transaction, income_by_payer_for_salary)
        elif amount < 0:
            total_spending += amount
            num_spending_transactions += 1
            spending_by_category = get_spending_by_category(transaction, spending_by_category)

    return {
        'total_income': total_income,
        'total_spending': total_spending,
        'num_income_transactions': num_income_transactions,
        'num_spending_transactions': num_spending_transactions,
        'spending_by_category': spending_by_category,
        'income_by_payer_for_salary': income_by_payer_for_salary
    }

def get_spending_by_category(
    transaction: Transaction, category_dict: Dict[str, CategoryInfo]
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
        category_dict[category] = {'amount': 0.00, 'count': 0}
    category_dict[category]['amount'] += amount
    category_dict[category]['count'] += 1
    
    # Round the amount to two decimal places
    category_dict[category]['amount'] = round(category_dict[category]['amount'], 2)
    
    return category_dict

def get_income_by_payer_for_salary(
    transaction: Transaction, salary_dict: Dict[str, CategoryInfo]
) -> Dict[str, CategoryInfo]:
    """Get salary info per payer and update salary dictionary with count.

    Args:
        transaction (Transaction): Transaction from which we get salary info
        salary_dict (Dict[str, CategoryInfo]): Dictionary to hold salary by payer

    Returns:
        Updated salary dict with new amount and count number
    """
    amount = float(f"{float(transaction['amount']):.2f}")
    description = transaction['description']

    if description not in salary_dict:
        salary_dict[description] = {'amount': 0.00, 'count': 0}

    salary_dict[description]['amount'] += amount
    salary_dict[description]['count'] += 1
    salary_dict[description]['amount'] = round(salary_dict[description]['amount'], 2)

    return salary_dict