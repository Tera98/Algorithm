import heapq
import sys

n = int(input())
que = []

for i in range(n):
    a = sys.stdin.readline().rstrip().split()

    if a[0] == "push":
        heapq.heappush(que, a[1])

    elif a[0] == "pop":
        if len(que) != 0:
            print(int(heapq.heappop(que)))
        else:
            print(-1)
