import sys

n, m = map(int, input().split())
arr = dict()

for i in range(n):
    arr[i] = sys.stdin.readline().rstrip()

arr2 = {v: k for k, v in arr.items()}

for _ in range(m):
    data = sys.stdin.readline().rstrip()
    if ord(data[0]) < 60:
        print(arr.get(int(data) - 1))
    else:
        print(arr2.get(data) + 1)
