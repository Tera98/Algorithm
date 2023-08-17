import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
data = []
visit = [[False] * n for i in range(m)]
for i in range(m):
    data.append(list(map(int, input().split())))
a, b, maxi = 0, 0, 0
out = True


def tomato(a, b):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        try:
            if data[a + dx[i]][b + dy[i]] == 0 or data[a + dx[i]][b + dy[i]] > (data[a][b]):
                data[a + dx[i]][b + dy[i]] = data[a][b] + 1
        except IndexError:
            pass


while out:
    for i in range(m):
        for j in range(n):
            if data[i][j] != 0 and data[i][j] != -1 and visit[i][j] is False:
                tomato(i, j)
                out = False
                visit[i][j] = True
                if maxi < data[i][j]:
                    maxi = data[i][j]
    if out:
        break
    else:
        out = True

output = 0
for i in range(m):
    if 0 in data[i]:
        output = 1
if output == 0:
    print(maxi-1)
else:
    print(-1)