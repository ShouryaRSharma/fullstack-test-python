from csv import DictReader

import pytest

from main import normalise_transactions


@pytest.fixture
def transactions():
    with open("transactions.csv") as f:
        yield list(DictReader(f))


def test_normalise_transactions(transactions):
    normalise_transactions(transactions)
    assert False
