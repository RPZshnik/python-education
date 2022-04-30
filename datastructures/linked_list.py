class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    @property
    def tail(self):
        return self.__tail

    @property
    def head(self):
        return self.__head

    def append(self, data):
        node = Node(data=data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__length += 1

    def prepend(self, data):
        node = Node(data=data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head = node
        self.__length += 1

    def __insert(self, node, previous_node, current_node):
        if previous_node is not None:
            node.next = current_node
            previous_node.next = node
            self.__length += 1
            return
        previous_node.next = node
        self.__head = node
        self.__length += 1
        return

    def insert(self, index, data):
        node = Node(data=data)
        previous_node = None
        current_node = self.__head
        while index >= 0 and current_node is not None:
            if index == 0:
                self.__insert(node, previous_node, current_node)
            index -= 1
            previous_node = current_node
            current_node = current_node.next

    def is_empty(self):
        return not self.__length

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def __remove(self, previous_node: Node, current_node: Node):
        self.__length -= 1
        if previous_node is not None:
            previous_node.next = current_node.next
            return
        self.__head = current_node.next
        return

    def remove(self, item):
        previous_node = None
        current_node = self.__head
        while current_node is not None:
            if current_node.data == item:
                self.__remove(previous_node, current_node)
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError("SortedLinkedList.remove(item): "
                         "item not in SortedLinkedList")

    def delete(self, index):
        previous_node = None
        current_node = self.__head
        while index >= 0 and current_node is not None:
            if index == 0:
                self.__remove(previous_node, current_node)
            index -= 1
            previous_node = current_node
            current_node = current_node.next

    def lookup(self, item):
        current_node = self.__head
        counter = 0
        while current_node is not None:
            if current_node.data == item:
                return counter
            counter += 1
            current_node = current_node.next
        raise ValueError("SortedLinkedList.index(item): "
                         "item not in SortedLinkedList")

    def pop(self, index):
        if index - 1 > self.__length:
            raise IndexError("pop index out of range")
        self.__length -= 1
        if index == 0:
            node = self.__head
            self.__head = self.__head.next
            return node.data
        else:
            previous_node = self.__head
            node = self.__head.next
            for _ in range(index - 1):
                node = node.next
                previous_node = previous_node.next
            previous_node.next = node.next
            return node.data

    def __getitem__(self, index):
        if index - 1 > self.__length:
            raise IndexError("pop index out of range")
        previous_node = self.__head
        if index == 0:
            return previous_node.data
        node = self.__head.next
        for _ in range(index - 1):
            node = node.next
            previous_node = previous_node.next
        return node.data

    def __str__(self):
        str_representation = ""
        current_node = self.__head
        while current_node is not None:
            str_representation += str(current_node.data)
            current_node = current_node.next
            if current_node is None:
                break
            str_representation += ", "
        str_representation = f'[{str_representation}]'
        return str_representation

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.__length

    def __iter__(self):
        current_node = self.__head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    def __bool__(self):
        return self.__head is not None
