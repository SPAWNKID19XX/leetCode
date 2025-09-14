import pytest


def test_sum(calc, simple_numbers):
    assert calc.sum(simple_numbers['a'], simple_numbers['b']) == 6


def test_mult(calc, simple_numbers):
    assert calc.mult(simple_numbers['a'], simple_numbers['b']) == 8


def test_div(calc, simple_numbers):
    assert calc.div(simple_numbers['a'], simple_numbers['b']) == 2


@pytest.mark.parametrize("a", [1, 2, 3, 4, -1, 4.0, 0])
def test_div_zero(calc, a):
    with pytest.raises(ValueError, match='Div by zero error'):
        calc.div(a, 0)


@pytest.mark.parametrize(
    "a, b, expected", [
        [3, 2, 1],
        [-2, -3, 1],
        [2, -2, 4],
        [3, 3, 0]
    ]
)
def test_minus(calc, a,b,expected):
    assert calc.minus(a, b) == expected
