from unittesting.to_test import Product
import pytest


@pytest.fixture
def product_example():
    """Fixture of product"""
    return Product("Potato", 25, 30)


def test_init_product(product_example):
    """Test init of Product"""
    assert product_example.title == "Potato" and\
           product_example.quantity == 30 and\
           product_example.price == 25


def test_subtract_quantity(product_example):
    """Test subtract quantity method"""
    product_example.subtract_quantity(15)
    assert product_example.quantity == 15


def test_add_quantity(product_example):
    """Test add quantity method"""
    product_example.add_quantity(15)
    assert product_example.quantity == 45


@pytest.mark.parametrize("price", [-10, 0, 3, 34, 100])
def test_change_price(product_example, price):
    """Test change price method"""
    product_example.change_price(price)
    assert product_example.price == price
