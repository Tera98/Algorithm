import heapq
import sys

n = int(input())
hq = []
for _ in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    if tmp != 0:
        heapq.heappush(hq, tmp)
    else:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
