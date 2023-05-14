import random


class RandomProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0
        self.count = 0

    def hash(self, key):
        return int(key * 0.61803 % 1 * self.M)

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        random.seed(1000)
        while True:
            if self.a[i] is None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            self.count += 1
            j = random.randint(1, 99)
            i = (initial_position + j) % self.M
            if self.N > self.M:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        random.seed(1000)
        while self.a[i] is not None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + random.randint(1, 99)) % self.M
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
        print()
        print('충돌 횟수 : ', self.count)
