class Node:
    def __init__(self, key):
        self.key = key
        self.left_child: Node = None
        self.right_child: Node = None
        self.height = 0

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        else:
            return node.height

    @staticmethod
    def get_balance(node):
        if not node:
            return 0
        left_height = 0
        right_height = 0
        if node.left_child is not None:
            left_height = Node.get_height(node.left_child) + 1
        if right_height is not None:
            right_height = Node.get_height(node.right_child) + 1
        return left_height - right_height

    def __str__(self):
        return str(None if not self else self.key)

    def __repr__(self):
        return str(self)


class BalancedBinarySearchTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def insert(self, item):
        if self.__root is None:
            self.__root = Node(item)
        else:
            self.__root = self._insert(item, self.__root)

    def lookup(self, item):
        cur_node = self.__root
        while cur_node and cur_node.key != item:
            if cur_node.key > item:
                cur_node = cur_node.left_child
            else:
                cur_node = cur_node.right_child
        return cur_node

    def delete(self, key):
        self.__root = self.__delete(self.__root, key)

    def preorder_traversal(self, node):
        keys = list()
        if node is None:
            return keys
        keys.append(node.key)
        keys += self.preorder_traversal(node.left_child)
        keys += self.preorder_traversal(node.right_child)
        return keys

    def inorder_traversal(self):
        return self._inorder_traversal(self.__root)

    def _insert(self, item, cur_node):
        if item < cur_node.key:
            if cur_node.left_child is None:
                cur_node.left_child = Node(item)
            else:
                cur_node.left_child = self._insert(item, cur_node.left_child)
        elif item > cur_node.key:
            if cur_node.right_child is None:
                cur_node.right_child = Node(item)
            else:
                cur_node.right_child = self._insert(item, cur_node.right_child)
        else:
            print("Value already in tree")
            return cur_node

        cur_node.height = 1 + max(Node.get_height(cur_node.left_child),
                                  Node.get_height(cur_node.right_child))
        balance = Node.get_balance(cur_node)

        if balance > 1 and item < cur_node.left_child.key:
            return self.__right_rotate(cur_node)

        if balance < -1 and item > cur_node.right_child.key:
            return self.__left_rotate(cur_node)

        if balance > 1 and item > cur_node.left_child.key:
            cur_node.left_child = self.__left_rotate(cur_node.left_child)
            return self.__right_rotate(cur_node)

        if balance < -1 and item < cur_node.right_child.key:
            cur_node.right_child = self.__right_rotate(cur_node.right_child)
            return self.__left_rotate(cur_node)

        return cur_node

    @staticmethod
    def __left_rotate(cur_node):

        right_node = cur_node.right_child
        left_subtree = right_node.left_child

        right_node.left_child = cur_node
        cur_node.right_child = left_subtree

        if cur_node.left_child is None and cur_node.right_child is None:
            cur_node.height = 0
        else:
            subtree_height = max(Node.get_height(cur_node.left_child),
                                 Node.get_height(cur_node.right_child))
            cur_node.height = 1 + subtree_height
        if right_node.left_child is None and right_node.right_child is None:
            right_node.height = 0
        else:
            subtree_height = max(Node.get_height(right_node.left_child),
                                 Node.get_height(right_node.right_child))
            right_node.height = 1 + subtree_height

        return right_node

    @staticmethod
    def __right_rotate(cur_node):
        left_node = cur_node.left_child
        right_subtree = left_node.right_child

        left_node.right_child = cur_node
        cur_node.left_child = right_subtree

        if cur_node.left_child is None and cur_node.right_child is None:
            cur_node.height = 0
        else:
            cur_node.height = 1 + max(Node.get_height(cur_node.left_child),
                                      Node.get_height(cur_node.right_child))
        if left_node.left_child is None and left_node.right_child is None:
            left_node.height = 0
        else:
            left_node.height = 1 + max(Node.get_height(left_node.left_child),
                                       Node.get_height(left_node.right_child))

        return left_node

    def _inorder_traversal(self, root):
        keys = list()
        if root is not None:
            keys = self._inorder_traversal(root.left_child)
            keys.append(root.key)
            keys = keys + self._inorder_traversal(root.right_child)
        return keys

    def __delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left_child = self.__delete(root.left_child, key)
        elif key > root.key:
            root.right_child = self.__delete(root.right_child, key)
        else:
            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                temp = root.left_child
                root = None
                return temp
            temp = self.__get_min_node(root.right_child)
            root.key = temp.key
            root.right_child = self.__delete(root.right_child, temp.key)

        if root is None:
            return root

        root.height = 1 + max(Node.get_height(root.left_child),
                              Node.get_height(root.right_child))
        balance = Node.get_balance(root)
        if balance > 1 and root.left_child.get_balance() >= 0:
            return self.__right_rotate(root)
        if balance < -1 and root.right_child.get_balance() <= 0:
            return self.__left_rotate(root)
        if balance > 1 and root.left_child.get_balance() < 0:
            root.left_child = self.__left_rotate(root.left_child)
            return self.__right_rotate(root)
        if balance < -1 and root.right_child.get_balance() > 0:
            root.right_child = self.__right_rotate(root.right_child)
            return self.__left_rotate(root)
        return root

    def __get_min_node(self, root):
        if root is None or root.left_child is None:
            return root
        return self.__get_min_node(root.left_child)
