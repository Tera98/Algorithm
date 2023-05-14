class DoubleProbing:
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
        d = 7 - (key % 7)
        j = 0
        while True:
            if self.a[i] is None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            self.count += 1
            i = (initial_position + j * d) % self.M
            if self.N > self.M:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        d = 7 - (key % 7)
        j = 1
        while self.a[i] is not None:
            if self.a[i] == key:
                return self.d[i]
            j += 1
            i = (initial_position + j * d) % self.M
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
        print()
        print('충돌 횟수 : ', self.count)

