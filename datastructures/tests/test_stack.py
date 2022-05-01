from datastructures.stack import Stack
import pytest


@pytest.fixture
def stack_example() -> Stack:
    """Empty stack fixture"""
    stack = Stack()
    for i in range(4):
        stack.push(i)
    return stack


@pytest.fixture
def stack_empty_example() -> Stack:
    """Stack fixture"""
    stack = Stack()
    return stack


def test_stack_init(stack_empty_example):
    """Test stack init method"""
    assert stack_empty_example.top is None and len(stack_empty_example) == 0


@pytest.mark.parametrize("items", [[1, 2, 3, 4], ["a", "b", "c", "d"], [1, 2, "c", "d"]])
def test_push(stack_empty_example, items):
    """Test push method"""
    for item in items:
        stack_empty_example.push(item)
    assert list(stack_empty_example) == items
    assert len(stack_empty_example) == len(items)


def test_pop(stack_example):
    """Test pop method"""
    item = stack_example.pop()
    assert item == 3
    assert list(stack_example) == [0, 1, 2]
    assert len(stack_example) == 3


def test_peek(stack_example):
    """Test peek method"""
    item = stack_example.peek()
    assert item == 3
    assert list(stack_example) == [0, 1, 2, 3]
    assert len(stack_example) == 4


def test_clear(stack_example):
    """Test clear method"""
    stack_example.clear()
    assert len(stack_example) == 0 and stack_example.top is None
