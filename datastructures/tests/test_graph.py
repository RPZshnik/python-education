from datastructures.graph import Graph, Vertex
import pytest


@pytest.fixture
def graph_example() -> Graph:
    """Graph fixture"""
    graph_example = Graph()
    for i in range(4):
        graph_example.insert(Vertex(i), graph_example.vertexes)
    return graph_example


@pytest.fixture
def graph_empty_example():
    """Empty graph fixture"""
    graph_example = Graph()
    return graph_example


def test_graph_init(graph_empty_example):
    """Test graph init method"""
    assert len(graph_empty_example.vertexes) == 0


@pytest.mark.parametrize("items", [[1, 2], ["a", "b", "c"], [1, 2, "c", "d"]])
def test_insert(graph_empty_example, items):
    """Test insert method"""
    for item in items:
        graph_empty_example.insert(Vertex(item), graph_empty_example.vertexes)
    assert list(graph_empty_example) == items
    assert len(graph_empty_example) == len(items)


@pytest.mark.parametrize("item", [4, 5, 6])
def test_lookup(graph_example, item):
    """Test lookup method"""
    v = Vertex(item)
    graph_example.insert(v, graph_example.vertexes)
    assert graph_example.lookup(item) == v


@pytest.mark.parametrize("item", [4, 5, 6])
def test_lookup_value_error(graph_example, item):
    """Test lookup method"""
    v = Vertex(item)
    with pytest.raises(ValueError):
        graph_example.lookup(item)


def test_delete(graph_example):
    """Test delete method"""
    graph_example.delete(2)
    assert len(graph_example) == 3 and list(graph_example) == [0, 1, 3]


