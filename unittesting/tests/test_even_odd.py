from unittesting.to_test import even_odd
import pytest


@pytest.mark.parametrize("x", [-4, -2, 0, 2, 4])
def test_to_even(x):
    """Test number for even"""
    assert even_odd(x) == "even"


@pytest.mark.parametrize("x", [-5, -3, -1, 1, 3, 5])
def test_to_odd(x):
    """Test number for odd"""
    assert even_odd(x) == "odd"


@pytest.mark.parametrize("x", ["2", "number", [1, 2], {1, 2}])
def test_to_type_error(x):
    """Test to incorrect type of value"""
    with pytest.raises(TypeError):
        return even_odd(x)
