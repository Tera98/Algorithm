class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n == None:
            return 0
        return n.height

    def put(self, key, value):  # key 값은 찾아야 하는 값
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value, 1)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
            return n
        n.height = max(self.height(n.left), self.height(n.right))+1
        return self.balance(n)

    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)

        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n

    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right))+1
        x.height = max(self.height(x.left), self.height(x.right))+1
        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right))+1
        x.height = max(self.height(x.left), self.height(x.right))+1
        return x

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def delete_min(self):
        if self.root == None:
            print('트리가 비어 있음')
        self.root = self.del_min(self.root) # 루트 노드와 삭제 후의 subtree 노드를 연결하는 코드

    def del_min(self, n):
        if n.left == None: # 노드 n의 왼쪽 자식 노드 값이 None 이면
            return n.right # 그 다음으로 가능성이 있는, 노드 n의 오른쪽 자식 노드 값을 반납한다.
        n.left = self.del_min(n.left) # 노드 n의 왼쪽 자식 노드 값이 있으면, 한번 더 탐색을 수행
        return n # 메소드 이름은 delete이지만, 실제로 노드 값을 지우는게 아니고 연결 관계를 잇거나 끊어지는 역할을 통해 delete를 수행한다.


    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, n, key):
        if n == None:
            return None
        if n.key > key:
            n.left = self.del_node(n.left, key)
        elif n.key < key:
            n.right = self.del_node(n.right, key)
        else:  # 삭제하고자 하는 노드를 찾았으면, 노드 사이의 연결을 재정립.
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n  # target은 삭제할 노드
            n = self.minimum(target.right)  # right subtree에서 최솟값 뽑아내기
            n.right = self.del_min(target.right)
            n.left = target.left

        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def preorder(self, n):
        if n != None:
            print(str(n.key), ' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), ' ', end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.key), ' ', end='')
