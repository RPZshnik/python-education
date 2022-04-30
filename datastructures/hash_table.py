import ctypes


class Node:
    def __init__(self, key, key_hash, data):
        self.key = key
        self.key_hash = key_hash
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def insert(self, node: Node, node2: Node):
        """Method that insert node before node2"""
        node.previous = node2.previous
        node.next = node2
        if node2.previous is None:
            self.__head = node
        node2.previous = node
        self.__length += 1

    def append(self, node):
        """Method that append node in the end of LinkedList"""
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.previous = self.__tail
            self.__tail.next = node
            self.__tail = node
        self.__length += 1

    def remove(self, node: Node):
        """Method that remove node"""
        self.__length -= 1
        # remove node in head
        if node.previous is None:
            self.__head = node.next
            if node.key_hash == node.next.key_hash:
                return id(node.next)
            else:
                return ""
        # remove node in tail
        if node.next is None:
            self.__tail = node.previous
            self.__tail.next = None
            if node.key_hash == node.previous.key_hash:
                return None
            else:
                return ""
        # remove node in middle
        node.previous.next = node.next
        node.next.previous = node.previous
        if node.previous.key_hash == node.key_hash:
            return None
        elif node.next.key_hash == node.key_hash:
            return id(node.next)
        else:
            return ""

    def __len__(self):
        """Method return length of LinkedList"""
        return self.__length

    def __iter__(self):
        current_node = self.__head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


class HashTable:
    def __init__(self):
        self._str_hash_table = "_" * (16 * 30)
        self.list = LinkedList()

    def insert(self, key, value):
        """Method that push item"""
        key_hash = self.__get_hash(key)
        node = Node(key, key_hash, value)
        item_id = id(node)
        if self.__is_empty(key_hash):
            self.list.append(node)
        else:
            node2 = self.__get_object_by_id(int(self.__get_id_by_hash(key_hash)))
            self.list.insert(node, node2)
        self._str_hash_table = self.__new_str_hash_table(key_hash, item_id)

    def lookup(self, key):
        """Method that return value by key"""
        return self.__lookup(key).data

    def delete(self, key):
        """Method that remove item value by key"""
        key_hash = self.__get_hash(key)
        node = self.__lookup(key)
        new_id = self.list.remove(node)
        if new_id == "":
            self._str_hash_table = self.__new_str_hash_table(key_hash, "_" * 16)
        elif new_id is not None:
            self._str_hash_table = self.__new_str_hash_table(key_hash, self.__get_str_id(new_id))

    def __lookup(self, key):
        """Method that return node by key"""
        key_hash = self.__get_hash(key)
        if self.__is_empty(key_hash):
            raise KeyError("Key error")
        item_id = self.__get_id_by_hash(key_hash)
        node = self.__get_object_by_id(item_id)
        while node is not None and node.key_hash == key_hash:
            if node.key == key:
                return node
            node = node.next
        raise KeyError("Key error")

    def __is_empty(self, key_hash):
        """Method return True if id by key_hash not empty"""
        if not self.__get_id_by_hash(key_hash):
            return True
        return False

    def __new_str_hash_table(self, key_hash, item_id):
        """Method create new str_hash_table"""
        str_id = self.__get_str_id(item_id)
        str_hash_table = self._str_hash_table[:16 * key_hash] + str_id + \
                         self._str_hash_table[16 * (key_hash + 1):]
        return str_hash_table

    def __get_id_by_hash(self, key_hash):
        """Method that return id by hash"""
        return self._str_hash_table[16 * key_hash:16 * (key_hash + 1)].replace("_", "")

    @staticmethod
    def __get_hash(key):
        """Hash function"""
        return hash(key) % 30

    @staticmethod
    def __get_str_id(value_id) -> str:
        """Method that return id in string format"""
        id_length = len(str(value_id))
        return str(value_id) + "_" * (16 - id_length)

    @staticmethod
    def __get_object_by_id(item_id):
        """Method that return object by id"""
        return ctypes.cast(int(item_id), ctypes.py_object).value

    def __repr__(self):
        return repr(self.list)
