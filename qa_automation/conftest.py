import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.fixture
def simple_numbers():
    return {
        'a': 4,
        'b': 2
    }
