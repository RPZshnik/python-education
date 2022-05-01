from datastructures.linked_list import LinkedList


class MyQueue:
    def __init__(self):
        self.__queue = LinkedList()

    def enqueue(self, data):
        self.__queue.append(data)

    def dequeue(self):
        return self.__queue.pop(0)

    def peek(self):
        return self.__queue[0]

    def clear(self):
        self.__queue.clear()

    def __str__(self):
        return str(self.__queue)

    def __repr__(self):
        return f"Queue({len(self)})"

    def __len__(self):
        return len(self.__queue)

    def __iter__(self):
        return iter(self.__queue)

    def __bool__(self):
        return len(self.__queue) != 0
