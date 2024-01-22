import pytest

from source import myfun as fn

def test_add():
    result = fn.add(number1=5, number2=5)
    assert result == 10

def test_divide():
    result = fn.divide(number1=10, number2=5)
    assert result == 2

# division by zero
def test_divide_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        fn.divide(number1=10, number2=0)

def test_divide2_value_err():
    # instead of ZeroDivisionError we'll use ValueError
    with pytest.raises(ValueError):
        fn.divide2(number1=10, number2=0)

def test_add_for_strings():
    result = fn.add(number1='I like ', number2='burgers')
    assert result == 'I like burgers'
