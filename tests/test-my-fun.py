import pytest

from source import myfun as fn

def test_add():
    result = fn.add(number1=5, number2=5)
    assert result == 10

def test_divide():
    result = fn.divide(number1=10, number2=5)
    assert result == 2