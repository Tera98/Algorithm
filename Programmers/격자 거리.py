# 3/9 [중] [그래프]

import sys
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '#':
                continue
            if graph[nx][ny] == '.' and visit[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())
graph = []
visit = [[0] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

dist[0][0] = 0
bfs(0, 0)

for i in range(n):
    print(*dist[i])
