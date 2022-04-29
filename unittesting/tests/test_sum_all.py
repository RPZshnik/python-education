import random

from unittesting.to_test import sum_all
import pytest


@pytest.fixture
def random_list():
    return [random.random() * 10 - 5 for _ in range(10)]


@pytest.mark.parametrize("x", [-2, 0, 2])
def test_to_single_argument(x):
    """Test with single argument"""
    assert sum_all(x) == x


@pytest.mark.parametrize("x", [[-1, 2, -3, 4], {-1, 2, -3, 4}])
def test_to_iter_object(x):
    """Test with iter objects"""
    assert sum_all(*x) == 2


def test_different_types(random_list):
    """Test different types"""
    assert sum_all(*random_list) == sum(random_list)
