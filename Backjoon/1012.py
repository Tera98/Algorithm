# 1012 : 유기농 배추
import sys

sys.setrecursionlimit(10 ** 7)


def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if visit[x][y] == 0 and graph[x][y] == 1:
        visit[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


test_num = int(input())
for _ in range(test_num):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visit = [[0] * n for _ in range(m)]
    cnt = 0
    for i in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and visit[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
