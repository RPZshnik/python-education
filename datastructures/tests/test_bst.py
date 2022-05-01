from datastructures.binary_search_tree import BalancedBinarySearchTree, Node
import pytest


@pytest.fixture
def bst_example() -> BalancedBinarySearchTree:
    """BST fixture"""
    bst_example = BalancedBinarySearchTree()
    for i in range(4):
        bst_example.insert(i)
    return bst_example


@pytest.fixture
def bst_empty_example():
    """Empty BST fixture"""
    bst_example = BalancedBinarySearchTree()
    return bst_example


def test_bst_init(bst_empty_example):
    """Test BST init method"""
    assert bst_empty_example.root is None


@pytest.mark.parametrize("items", [[1, 2], ["a", "b", "c"]])
def test_insert(bst_empty_example, items):
    """Test insert method"""
    for item in items:
        bst_empty_example.insert(item)
    assert bst_empty_example.inorder_traversal() == items


@pytest.mark.parametrize("items", [[1, 2, "a", "b", "c"]])
def test_insert_type_error(bst_empty_example, items):
    """Test insert method"""
    with pytest.raises(TypeError):
        for item in items:
            bst_empty_example.insert(item)


@pytest.mark.parametrize("item", [4, 5, 6])
def test_lookup(bst_example, item):
    """Test lookup method"""
    bst_example.insert(item)
    assert bst_example.lookup(item).key == item


@pytest.mark.parametrize("item", [4, 5, 6])
def test_lookup_value_error(bst_example, item):
    """Test lookup method value error"""
    assert bst_example.lookup(item) is None


def test_delete(bst_example):
    """Test delete method"""
    bst_example.delete(2)
    assert bst_example.lookup(2) is None


