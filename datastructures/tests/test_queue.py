from datastructures.my_queue import MyQueue
import pytest


@pytest.fixture
def queue_example() -> MyQueue:
    """Empty queue fixture"""
    queue_example = MyQueue()
    for i in range(4):
        queue_example.enqueue(i)
    return queue_example


@pytest.fixture
def queue_empty_example() -> MyQueue:
    """Queue fixture"""
    queue_example = MyQueue()
    return queue_example


def test_queue_init(queue_empty_example):
    """Test queue init method"""
    assert len(queue_empty_example) == 0


@pytest.mark.parametrize("items", [[1, 2, 3, 4], ["a", "b", "c", "d"], [1, 2, "c", "d"]])
def test_enqueue(queue_empty_example, items):
    """Test enqueue method"""
    for item in items:
        queue_empty_example.enqueue(item)
    assert list(queue_empty_example) == items
    assert len(queue_empty_example) == len(items)


def test_dequeue(queue_example):
    """Test dequeue method"""
    item = queue_example.dequeue()
    assert item == 0
    assert list(queue_example) == [1, 2, 3]
    assert len(queue_example) == 3


def test_peek(queue_example):
    """Test peek method"""
    item = queue_example.peek()
    assert item == 0
    assert list(queue_example) == [0, 1, 2, 3]
    assert len(queue_example) == 4


def test_clear(queue_example):
    """Test clear method"""
    queue_example.clear()
    assert len(queue_example) == 0
