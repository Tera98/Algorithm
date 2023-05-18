class TwoWay:
    class Node:
        def __init__(self, key, data, link):
            self.key = key
            self.data = data
            self.next = link

    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.n = [0] * size

    def hash(self, key):
        return key % self.M

    def hash2(self, key):
        return key * 7 % self.M

    def put(self, key, data):
        i = self.hash(key)
        j = self.hash2(key)

        p = self.a[i]
        while p is not None:
            if key == p.key:
                p.data = data
                return
            p = p.next

        p = self.a[j]
        while p is not None:
            if key == p.key:
                p.data = data
                return
            p = p.next

        if self.n[i] <= self.n[j]:
            self.n[i] += 1
            self.a[i] = self.Node(key, data, self.a[i])

        else:
            self.n[j] += 1
            self.a[j] = self.Node(key, data, self.a[j])

    def get(self, key):
        i = self.hash(key)
        j = self.hash2(key)
        h = self.a[i]
        d = self.a[j]
        while h is not None:
            if key == h.key:
                return h.data
            h = h.next
        while d is not None:
            if key == d.key:
                return d.data
            d = d.next
        return None

    def print_table(self):
        for i in range(self.M):
            print('%2d' % i, end='')
            p = self.a[i]
            while p is not None:
                print('-->[', p.key, ',', p.data, ']', end='')
                p = p.next
            print()
