import pytest

from toycalc.core import add, fib


def test_add():
    assert add(2, 3) == 5


@pytest.mark.parametrize("n, val", [(0, 0), (1, 1), (5, 5), (10, 55)])
def test_fib(n, val):
    assert fib(n) == val


def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-1)
