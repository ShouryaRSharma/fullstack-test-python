from csv import DictReader
import pytest

from main import normalise_transactions, get_total_amount, get_spending_by_category


@pytest.fixture
def transactions():
    with open("transactions.csv") as f:
        yield list(DictReader(f))


def test_normalise_transactions(transactions):
    # TODO: Write unit test
    pass


def test_get_total_amount():
    transactions = [
        {'amount': '1500.0', 'category': 'Salary', 'description': 'ABC Company Salary'},
        {'amount': '-100.0', 'category': 'Shopping', 'description': 'Grocery Shopping'},
        {'amount': '200.0', 'category': 'Other Income', 'description': 'Freelance Work'},
        {'amount': '-50.0', 'category': 'Bills', 'description': 'Electricity Bill'},
    ]
    result = get_total_amount(transactions)
    assert result['total_income'] == 1700.0
    assert result['total_spending'] == -150.0
    assert result['num_income_transactions'] == 2
    assert result['num_spending_transactions'] == 2


def test_get_spending_by_category():
    transaction = {'amount': '-50.0', 'category': 'Shopping'}
    result = get_spending_by_category(transaction, {})
    assert result['Shopping'] == {'amount': -50.0, 'count': 1}