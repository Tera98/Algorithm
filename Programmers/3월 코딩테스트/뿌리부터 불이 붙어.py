# 3/27 코딩 테스트

from collections import deque


def bfs(here):
    queue.append(here)
    visit[here] = True
    while len(queue) != 0:
        here = queue.popleft()
        adj[here].sort()
        for there in adj[here]:
            if not visit[there]:
                dist[there - 1] = dist[here - 1] + 1
                queue.append(there)
                visit[there] = True
    return max(dist)


n = int(input())
adj = [[] for i in range(n + 1)]
output = 10000

for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n):
    visit = [False] * (n + 1)
    dist = [0] * n
    queue = deque()
    output = min(bfs(i), output)

if n == 1:
    print(0)
else:
    print(output)
