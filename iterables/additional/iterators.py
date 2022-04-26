from collections.abc import Iterable


class Zip:
    def __init__(self, *args, **kwargs):
        self.__iterables_objects = []
        if all(isinstance(arg, Iterable) for arg in args):
            self.__iterables_objects = sorted(args, key=len)
        else:
            raise ValueError("All objects must be iterables")

    def __len__(self):
        return len(self.__iterables_objects)

    def __iter__(self):
        return ZipIterator(self.__iterables_objects, len(self))


class ZipIterator:
    """Class, that implements zip iterator"""
    def __init__(self, iterables_objects, length):
        self._iterables_objects = iterables_objects
        self._length = length
        self._index = 0

    def __next__(self):
        if self._length == 0 or self._index >= len(self._iterables_objects[0]):
            raise StopIteration
        else:
            group = list()
            for iterable_object in self._iterables_objects:
                group.append(iterable_object[self._index])
            self._index += 1
            return tuple(group)

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
        self.lengths = [len(iterable) for iterable in self.pools]
        self.counters = [0] * len(self.pools)
        self.counters[-1] = -1

    def __next__(self):
        product = []
        for i in range(len(self.counters) - 1, -1, -1):
            if self.counters[i] + 1 != self.lengths[i]:
                self.counters[i] += 1
                break
            elif i != 0:
                self.counters[i] = 0
            else:
                raise StopIteration
        for index, i in enumerate(self.counters):
            product.append(self.pools[index][i])
        return tuple(product)

    def __iter__(self):
        return self


class Open:
    """Context manager for files"""

    def __init__(self, filename, mode):
        self.file = open(filename, mode, encoding="utf-8")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read(self):
        """Return all text"""
        return self.file.read()

    def readline(self):
        """Return generator"""
        for line in self.file.readlines():
            yield line

    def write(self, text):
        """Write text in the end of file"""
        self.file.write(text)
