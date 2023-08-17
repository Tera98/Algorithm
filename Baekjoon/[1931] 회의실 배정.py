import sys

n = int(input())
time, cnt = 0, 0
data = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    data.append([a, b, b - a])

data.sort(key=lambda x: (x[1], x[0], x[2]))  # 정렬이 포인트

for i in range(n):
    if data[i][0] >= time:
        cnt += 1
        time = data[i][1]
print(cnt)
