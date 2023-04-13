# 4/4
import math


def getz(x, y, n, value):
    length = int(math.pow(2, n - 1))
    if n >= 1:
        if x < length and y < length:
            getz(x, y, n - 1, value)
        elif x >= length > y:
            getz(x - length, y, n - 1, value + length * length)
        elif y >= length > x:
            getz(x, y - length, n - 1, value + 2 * length * length)
        else:
            getz(x - length, y - length, n - 1, value + 3 * length * length)
    else:
        print(value)


n, col, row = map(int, input().split())
getz(row, col, n, 0)
