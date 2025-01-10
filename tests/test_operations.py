from src.math_operations import add , subtract

def test_add():
    assert add(2,3) == 5
    assert add(3,4) == 7

def test_sub():
    assert subtract(3,2) == 1
    assert subtract(4,1) == 3