import pytest
from calculator import Calculator

calc = Calculator()
def test_add():
    assert calc.sum(5,3) == 8

def test_mult():
    assert calc.mult(5,3) == 15

def test_div():
    assert calc.div(10,4)==2.5

def test_div_by_zero():
    with pytest.raises(ValueError):  # ожидаем ошибку
        calc.div(10, 0)

def test_minus():
    assert calc.minus(3,2) == 1