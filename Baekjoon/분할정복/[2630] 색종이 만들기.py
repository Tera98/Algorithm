import sys


def divide_conquer(size, idx_x, idx_y):
    global data, answer_blue, answer_white
    cnt = 0
    for i in range(size):
        for j in range(size):
            cnt += data[idx_x + i][idx_y + j]
    if 0 < cnt < size * size:
        divide_conquer(size // 2, idx_x, idx_y)
        divide_conquer(size // 2, idx_x + size // 2, idx_y)
        divide_conquer(size // 2, idx_x, idx_y + size // 2)
        divide_conquer(size // 2, idx_x + size // 2, idx_y + size // 2)
    elif cnt == size * size:
        answer_blue += 1
    else:
        answer_white += 1


n = int(input())
data = []
answer_blue, answer_white = 0, 0
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))
divide_conquer(n, 0, 0)
print(answer_white)
print(answer_blue)
