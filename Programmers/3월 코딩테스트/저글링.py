# 3/27 코딩 테스트

from collections import deque

a = deque([1, 2, 3])
n = int(input())
a.rotate((n - 1) * -1)
print(*a)
