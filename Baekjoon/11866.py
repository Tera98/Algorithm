# 11866 : 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
a = deque()
for i in range(n):
    a.append(i + 1)

print("<", end="")
for i in range(n):
    a.rotate((k - 1) * -1)
    print(a.popleft(), end="")
    if i != n - 1:
        print(", ", end="")
print(">")
