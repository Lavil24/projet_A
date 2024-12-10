# tests/test_main.py
import pytest
from src.projet_z.projet_Z_main import addition, soustraction, multiplication, division, division_euclidienne

def test_addition():
    assert addition(3, 2) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_soustraction():
    assert soustraction(3, 2) == 1
    assert soustraction(2, 3) == -1
    assert soustraction(0, 0) == 0

def test_multiplication():
    assert multiplication(3, 2) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0

def test_division():
    assert division(6, 2) == 3
    assert division(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

def test_division_euclidienne():
    assert division_euclidienne(6, 2) == 3
    assert division_euclidienne(5, 2) == 2
    with pytest.raises(ZeroDivisionError):
        division_euclidienne(1, 0)
