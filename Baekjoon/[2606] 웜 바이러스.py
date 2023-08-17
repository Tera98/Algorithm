import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
grap = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    grap[a].append(b)
    grap[b].append(a)
deq = deque()
deq.append(1)
visited[1] = True
cnt = -1
while len(deq) != 0:
    tmp = deq.popleft()
    for i in grap[tmp]:
        if not visited[i]:
            deq.append(i)
            visited[i] = True
    cnt += 1
print(cnt)
