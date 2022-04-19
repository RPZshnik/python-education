import cProfile
from collections.abc import Iterable
from memory_profiler import profile
import timeit

class Product:
    def __init__(self, *args, **kwargs):
        self.__iterables_objects = []
        if all(isinstance(arg, Iterable) for arg in args):
            self.__iterables_objects = sorted(args, key=len)
        else:
            raise ValueError("All objects must be iterables")
        self.__repeat = kwargs.get("repeat", 1)
        self._index = 0

    def __len__(self):
        return len(self.__iterables_objects)

    def __iter__(self):
        return ProductIterator(self.__iterables_objects, self.__repeat)


class ProductIterator:
    """Class, that implements product iterator"""
    def __init__(self, iterables_objects, repeat):
        self.pools = list(map(tuple, iterables_objects)) * repeat
        self.__results = [[]]
        for pool in self.pools:
            self.__results = [x + [y] for x in self.__results for y in pool]
        self._index = -1

    def __next__(self):
        if len(self.__results) - 1 <= self._index:
            raise StopIteration
        self._index += 1
        return tuple(self.__results[self._index])

    def __iter__(self):
        return self

class Chain:
    def __init__(self, *args, **kwargs):
        self.__iterables_objects = []
        if all(isinstance(arg, Iterable) for arg in args):
            self.__iterables_objects = sorted(args, key=len)
        else:
            raise ValueError("All objects must be iterables")

    def __len__(self):
        return len(self.__iterables_objects)

    def __iter__(self):
        return ChainIterator(self.__iterables_objects)


class ChainIterator:
    """Class, that implements chain iterator"""
    def __init__(self, iterables_objects):
        self._items = [i for item in iterables_objects for i in item]
        self._length = len(self._items)
        self._index = -1

    def __next__(self):
        if self._length == 0 or self._index >= self._length - 1:
            raise StopIteration
        else:
            self._index += 1
            return self._items[self._index]

    def __iter__(self):
        return self


@profile
def main():
    p = Chain(list(range(100000)), ("a"))
    for i in p:
        print(i)
    print()


if __name__ == '__main__':
    main()
