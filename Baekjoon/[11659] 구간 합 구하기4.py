import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(n - 1):
    a[i + 1] = a[i] + a[i + 1]

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x == 1:
        print(a[y-1])
    else:
        print(a[y-1]-a[x-2])
