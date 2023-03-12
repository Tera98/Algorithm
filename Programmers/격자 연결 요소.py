# 3/8 [중] [그래프]

import sys

sys.setrecursionlimit(10 ** 5)


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if visit[x][y] == 0 and graph[x][y] == '#':
        visit[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
graph = []
visit = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#' and visit[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)
