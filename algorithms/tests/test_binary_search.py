from algorithms.binary_search import binary_search
from random import randint
import pytest


@pytest.mark.parametrize("numbers", [[randint(-1000, 1000) for _ in range(100)] for n in range(100)])
def test_binary_search(numbers):
    numbers.sort()
    num = numbers[len(numbers) // 2]
    assert numbers.index(num) == binary_search(numbers, num)


@pytest.mark.parametrize("numbers", [[randint(-1000, 1000) for _ in range(100)] for n in range(10)])
def test_item_not_include(numbers):
    assert binary_search(numbers, 2000) == -1
