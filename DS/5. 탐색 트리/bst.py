class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, n, key):
        if n is None:
            return None
        if n.key > key:
            return self.get_item(n.left, key)
        elif n.key < key:
            return self.get_item(n.right, key)
        else:
            return n.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n

    def min(self):
        if self.root is None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left is None:
            return n
        return self.minimum(n.left)

    def delete_min(self):
        if self.root is None:
            print("트리가 비어 있음")
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left is None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, n, key):
        if n is None:
            return None
        if n.key > key:
            n.left = self.del_node(n.left, key)
        elif n.key < key:
            n.right = self.del_node(n.right, key)
        else:
            if n.right is None:
                return n.left
            if n.left is None:
                return n.right
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
        return n

    def preorder(self, n):
        if n is not None:
            print(str(n.key) + '(' + n.value + ')', ' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n is not None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key) + '(' + n.value + ')', ' ', end='')
            if n.right:
                self.inorder(n.right)



