import pytest
from calculatrice.app import addition, soustraction, multiplication, division

def test_addition():
    assert addition(1, 2) == 3
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_soustraction():
    assert soustraction(5, 3) == 2
    assert soustraction(3, 5) == -2
    assert soustraction(0, 0) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 3) == -3
    assert multiplication(0, 5) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(5, 2) == 2.5
    assert division(1, 0) == "Erreur : Division par zéro"
    assert division(0, 1) == 0

if __name__ == "__main__":
    pytest.main()