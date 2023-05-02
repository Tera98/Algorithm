m, n = map(int, input().split())
arr = [0] * m
for _ in range(0, n):
    u, v = map(int, input().split())
    for i in range(u - 1, v):
        arr[i] += 1
print(*arr)
