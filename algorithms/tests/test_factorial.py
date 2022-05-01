from algorithms.factorial import factorial as custom_factorial
from math import factorial
import pytest


@pytest.mark.parametrize("numbers", [num for num in range(100)])
def test_factorial(numbers):
    assert custom_factorial(numbers) == factorial(numbers)


def test_value_error():
    with pytest.raises(ValueError):
        assert factorial(-1)
