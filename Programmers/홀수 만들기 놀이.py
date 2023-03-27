import heapq
import sys

n = int(input())
a = list(map(int, sys.stdin.readline().rstrip().split()))
heapq.heapify(a)

while len(a) > 1:
    tmp1 = heapq.heappop(a)
    tmp2 = heapq.heappop(a)
    if (tmp1 + tmp2) % 2 != 0:
        heapq.heappush(a, tmp1 + tmp2)

if len(a) != 0:
    print(*a)
else:
    print(-1)