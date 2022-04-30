from datastructures.linked_list import LinkedList


class Vertex:
    def __init__(self, data):
        self.data = data
        self.vertexes: LinkedList = LinkedList()

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"Vertex({self.data})"

    def __hash__(self):
        return self.data

    def __eq__(self, other):
        return self.data == other.data


class Graph:
    def __init__(self):
        self.vertexes: LinkedList = LinkedList()

    def insert(self, vertex, vertexes):
        for node in vertexes:
            node.vertexes.append(vertex)
            vertex.vertexes.append(node)
        self.vertexes.append(vertex)

    def lookup(self, item):
        for vertex in self.vertexes:
            if vertex.data == item:
                return vertex
        raise ValueError("Item not in graph")

    def delete(self, item):
        self.vertexes.remove(Vertex(item))
        for vertex in self.vertexes:
            vertex.vertexes.remove(Vertex(item))

    def __len__(self):
        return len(self.vertexes)

    def __iter__(self):
        return GraphIterator(self.vertexes)


class GraphIterator:
    def __init__(self, vertexes):
        self.__vertexes = vertexes
        self.__index = 0

    def __get_vertex(self):
        if self.__index >= len(self.__vertexes):
            raise StopIteration
        vertex = list(self.__vertexes)[self.__index]
        self.__index += 1
        return vertex.data

    def __next__(self):
        return self.__get_vertex()

    def __iter__(self):
        return self
