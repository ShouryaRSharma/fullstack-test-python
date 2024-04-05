from csv import DictReader
from typing import List

import pytest

from main import normalise_transactions, get_total_income, get_total_spending
from models import Transaction


@pytest.fixture
def transactions():
    with open("transactions.csv") as f:
        yield list(DictReader(f))


def test_normalise_transactions(transactions):
    # TODO: Write unit test
    pass


def test_get_total_income():
    transactions: List[Transaction] = [
        {'amount': '700.00', 'category': 'Salary'},
        {'amount': '100.00', 'category': 'Capital Gains'},
        {'amount': '-100.0', 'category': 'Shopping'},
    ]
    result = get_total_income(transactions)
    assert result['total_income'] == 800.00
    assert result['num_transactions'] == 2


def test_get_total_spending():
    transactions = [
        {'amount': '-10.00', 'category': 'Shopping'},
        {'amount': '700.00', 'category': 'Salary'},
        {'amount': '-25.00', 'category': 'Bills and Utilities'},
    ]
    result = get_total_spending(transactions)
    assert result['total_spending'] == -35.00
    assert result['num_transactions'] == 2