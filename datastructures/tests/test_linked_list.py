from datastructures.linked_list import LinkedList
import pytest


@pytest.fixture
def list_example() -> LinkedList:
    """List fixture"""
    list_example = LinkedList()
    for i in range(4):
        list_example.append(i)
    return list_example


@pytest.fixture
def list_empty_example() -> LinkedList:
    """Empty list fixture"""
    list_example = LinkedList()
    return list_example


def test_list_init(list_empty_example):
    """Test list init method"""
    assert list_empty_example.head is None and \
           list_empty_example.tail is None and \
           len(list_empty_example) == 0


@pytest.mark.parametrize("items", [[1, 2, 3, 4], ["a", "b", "c", "d"], [1, 2, "c", "d"]])
def test_append(list_empty_example, items):
    """Test append method"""
    for item in items:
        list_empty_example.append(item)
    assert list(list_empty_example) == items
    assert len(list_empty_example) == len(items)


@pytest.mark.parametrize("items", [[1, 2, 3, 4], ["a", "b", "c", "d"], [1, 2, "c", "d"]])
def test_prepend(list_empty_example, items):
    """Test prepend method"""
    for item in items:
        list_empty_example.prepend(item)
    assert list(list_empty_example) == list(reversed(items))
    assert len(list_empty_example) == len(items)


def test_pop(list_example):
    """Test pop method"""
    item = list_example.pop(2)
    assert item == 2
    assert list(list_example) == [0, 1, 3]
    assert len(list_example) == 3


def test_pop_index_error(list_example):
    """Test pop method (index error)"""
    with pytest.raises(IndexError):
        list_example.pop(10)


@pytest.mark.parametrize("item, index", [(0, 0), (1, 1), (3, 3)])
def test_lookup(list_example, item, index):
    """Test lookup method"""
    assert list_example.lookup(item) == index


def test_clear(list_example):
    """Test clear method"""
    list_example.clear()
    assert len(list_example) == 0 and\
           list_example.head is None and\
           list_example.tail is None


def test_delete(list_example):
    """Test delete method"""
    list_example.delete(2)
    assert len(list_example) == 3 and list(list_example) == [0, 1, 3]


def test_remove(list_example):
    """Test remove method"""
    list_example.remove(2)
    assert len(list_example) == 3 and list(list_example) == [0, 1, 3]


def test_remove_value_error(list_example):
    """Test remove method (value error)"""
    with pytest.raises(ValueError):
        list_example.remove(10)
