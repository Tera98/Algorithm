# 11650 : 좌표 정렬하기
import sys

n = int(input())
data = []
for i in range(n):
    data.append(sys.stdin.readline().rstrip().split())

data.sort(key=lambda x: [int(x[0]), int(x[1])])

for i in data:
    print(*i)
