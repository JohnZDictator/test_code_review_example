import pytest


def f(x, y):
     if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numeric")


def test_mytest():
    with pytest.raises(TypeError):
        f("2", 3)
    with pytest.raises(TypeError):
        f(2, "3")