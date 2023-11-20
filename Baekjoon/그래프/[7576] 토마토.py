import sys
from collections import deque


def tomato(x, y):
    global deq, visited
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for idx in range(4):
        if 0 <= (x + dx[idx]) < m and 0 <= (y + dy[idx]) < n:
            if data[x + dx[idx]][y + dy[idx]] > data[x][y] or data[x + dx[idx]][y + dy[idx]] == 0:
                data[x + dx[idx]][y + dy[idx]] = data[x][y] + 1
                if not visited[x + dx[idx]][y + dy[idx]]:
                    deq.append([x + dx[idx], y + dy[idx]])
                    visited[x + dx[idx]][y + dy[idx]] = True


n, m = map(int, sys.stdin.readline().rstrip().split())
data = []
visited = [[False] * n for i in range(m)]
for i in range(m):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))
maxi, output = 0, 0
deq = deque()

for i in range(m):
    for j in range(n):
        if data[i][j] == 1:
            deq.append([i, j])

while len(deq):
    a, b = deq.popleft()
    tomato(a, b)

for i in range(m):
    if 0 in data[i]:
        output = 1
    if maxi < max(data[i]):
        maxi = max(data[i])

if output == 0:
    print(maxi - 1)
else:
    print(-1)
