# 3/10 [상] [그래프]
import sys
from collections import deque


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        a, b = queue.popleft()
        visit[a][b] = 1
        graph[a][b] = '@'
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '#':
                continue
            if graph[nx][ny] == '.' and visit[nx][ny] == 0:
                queue.append((nx, ny))


n, m = map(int, input().split())
x, y = map(int, input().split())

graph = []
visit = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

bfs(x - 1, y - 1)

for i in range(n):
    for j in range(m):
        print(graph[i][j], end="")
    print()
