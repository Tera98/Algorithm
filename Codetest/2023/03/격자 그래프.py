import sys


def check(data, row, col, rowsize, colsize):
    cnt = 0
    if row > 0 and data[row - 1][col] == '.':
        cnt += 1
    if row < rowsize - 1 and data[row + 1][col] == '.':
        cnt += 1
    if col > 0 and data[row][col - 1] == '.':
        cnt += 1
    if col < colsize - 1 and data[row][col + 1] == '.':
        cnt += 1
    return cnt


row, col = map(int, sys.stdin.readline().rstrip().split())
data = [[] for i in range(row)]
for i in range(row):
    data[i] = list(map(str, sys.stdin.readline().rstrip()))
arr = [[] for i in range(row)]
cnt = 0
for i in range(row):
    for j in range(col):
        if data[i][j] == '.':
            cnt += check(data, i, j, row, col)

print(str(row * col) + " " + str(int(cnt / 2)))
