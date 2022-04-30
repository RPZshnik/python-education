from datastructures.linked_list import LinkedList


class Stack:
    def __init__(self):
        self.__stack = LinkedList()

    @property
    def top(self):
        if len(self) > 0:
            return self.__stack[-1]

    def push(self, data):
        self.__stack.append(data)

    def pop(self):
        return self.__stack.pop(len(self.__stack) - 1)

    def peek(self):
        return self.__stack[(len(self.__stack) - 1)]

    def is_empty(self):
        return not len(self.__stack)

    def clear(self):
        self.__stack.clear()

    def __str__(self):
        return str(self.__stack)

    def __repr__(self):
        return f"Stack({len(self.__stack)})"

    def __len__(self):
        return len(self.__stack)

    def __iter__(self):
        return iter(self.__stack)

    def __bool__(self):
        return len(self) != 0
