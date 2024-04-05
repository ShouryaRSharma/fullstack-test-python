from csv import DictReader
import pytest

from main import normalise_transactions, get_spending_by_category, get_income_by_payer_for_salary


@pytest.fixture
def transactions():
    with open("transactions.csv") as f:
        yield list(DictReader(f))


def test_get_spending_by_category():
    transaction = {'amount': '-50.0', 'category': 'Shopping'}
    result = get_spending_by_category(transaction, {})
    assert result['Shopping'] == {'amount': -50.0, 'count': 1}


def test_get_income_by_payer_for_salary():
    transaction = {'amount': '1500.00', 'category': 'Salary', 'description': 'WEB GENIUS'}
    result = get_income_by_payer_for_salary(transaction, {})
    assert result['WEB GENIUS'] == {'amount': 1500.0, 'count': 1}


def test_normalise_transactions(transactions):
    result = normalise_transactions(transactions)
    assert result['total_income'] == 5023.95
    assert result['total_spending'] == -325.31
    assert result['num_income_transactions'] == 5
    assert result['num_spending_transactions'] == 11
    assert result['spending_by_category']['Shopping'] == {'amount': -136.30, 'count': 5}
    assert result['spending_by_category']['Food & Dining'] == {'amount': -17.40, 'count': 1}
    assert result['spending_by_category']['Bills and Utilities'] == {'amount': -69.86, 'count': 2}
    assert result['income_by_payer_for_salary']['WEB GENIUS'] == {'amount': 4700.00, 'count': 3}