from unittesting.to_test import Product, Shop
import pytest


@pytest.fixture
def product_example() -> Product:
    """Product fixture"""
    product = Product("Potato", 25, 30)
    return product


@pytest.fixture
def product_second_example() -> Product:
    """Second product fixture"""
    product = Product("Apple", 17, 50)
    return product


@pytest.fixture
def shop_example(product_example) -> Shop:
    """Shop fixture"""
    shop = Shop(product_example)
    return shop


def test_init_with_product_example(shop_example, product_example):
    """Test of shop init"""
    assert shop_example.products == [product_example] and shop_example.money == .0


def test_add_product(shop_example, product_example, product_second_example):
    """Test of adding product to the shop"""
    shop_example.add_product(product_second_example)
    assert shop_example.products == [product_example, product_second_example]


def test_get_nonexistent_product_index(shop_example):
    """Test method _get_product_index with nonexistent product"""
    assert shop_example._get_product_index("Carrot") is None


def test_get_product_index(shop_example, product_example):
    """Test method _get_product_index"""
    assert shop_example._get_product_index("Potato") == 0


@pytest.mark.parametrize("title, quantity", [("Potato", 10)])
def test_sell_product(shop_example, title, quantity):
    """Test sell product method"""
    shop_example.sell_product(title, quantity)
    assert shop_example.products[shop_example._get_product_index(title)].quantity == 20


@pytest.mark.parametrize("title, quantity", [("Carrot", 10)])
def test_sell_nonexistent_product(shop_example, title, quantity):
    """Test method sell_product with nonexistent product"""
    assert shop_example.sell_product(title, quantity) is None


def test_sell_product_not_enough(product_example, shop_example):
    """Test method sell_product in case when amount of available
     products of that type is less then given."""
    with pytest.raises(ValueError):
        shop_example.sell_product(product_example.title, product_example.quantity + 10)
