import sys
from collections import deque


def bfs(y, x):
    global deq, visited
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for idx in range(4):
        if 0 <= (x + dx[idx]) < m and 0 <= (y + dy[idx]) < n:
            if graph[y + dy[idx]][x + dx[idx]] > graph[y][x] or graph[y + dy[idx]][x + dx[idx]] == 1:
                if not visited[y + dy[idx]][x + dx[idx]]:
                    graph[y + dy[idx]][x + dx[idx]] = graph[y][x] + 1
                    deq.append([y + dy[idx], x + dx[idx]])
                    visited[y + dy[idx]][x + dx[idx]] = True


n, m = map(int, input().split())
graph = []
visited = [[False] * m for i in range(n)]
deq = deque()
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            deq.append([i, j])
            graph[i][j] = 0
            break

while len(deq):
    a, b = deq.popleft()
    bfs(a, b)

for i in range(n):
    for j in range(m):
        if visited[i][j] is False and graph[i][j] == 1:
            graph[i][j] = -1

for i in graph:
    print(*i)
