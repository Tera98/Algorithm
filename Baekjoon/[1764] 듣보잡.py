# 4/20
import sys

n, m = map(int, input().split())
a, b = set(), set()
for _ in range(n):
    a.add(sys.stdin.readline().rstrip())
for _ in range(m):
    b.add(sys.stdin.readline().rstrip())
output = sorted(a.intersection(b))
print(len(output))
for _ in output:
    print(_)
