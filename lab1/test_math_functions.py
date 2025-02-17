# test_math_functions.py
from math_functions import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(5, 5) == 10
    assert add("a", 1) == "Error: Non-numeric input"

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(10, 5) == 5
    assert subtract("a", 1) == "Error: Non-numeric input"

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply("a", 1) == "Error: Non-numeric input"

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-10, 2) == -5
    assert divide(5, 0) == "Error: You cannot divide by 0"
    assert divide("a", 1) == "Error: Non-numeric input"