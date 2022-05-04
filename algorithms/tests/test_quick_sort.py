from algorithms.quick_sort import quick_sort
from random import randint
import pytest


@pytest.mark.parametrize("numbers", [[randint(-1000, 1000) for _ in range(100)] for n in range(100)])
def test_binary_search(numbers):
    assert sorted(numbers) == quick_sort(numbers)


@pytest.mark.parametrize("numbers", [[randint(-1000, 1000) for _ in range(100)] for n in range(10)])
def test_type_error(numbers):
    numbers.append("abx")
    with pytest.raises(TypeError):
        assert quick_sort(numbers) == sorted(numbers)
