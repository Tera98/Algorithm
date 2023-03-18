class EmptyError(Exception):
    pass


class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):
        p.next = self.Node(item, p.next)  # 원래 p와 연결되어 있던 노드를 새로운 노드의 다음 노드로 할당한 후, 새로운 노드를 p와 연결되어
        self.size += 1  # 있는 노드의 다음 노드로 설정 하는 것.

    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError('UnderFlow')
        else:
            t = p.next
            p.next = t.next
            self.size -= 1

    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            p = p.next
