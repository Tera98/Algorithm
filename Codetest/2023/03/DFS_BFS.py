from collections import deque


def dfs(here):
    adj[here].sort()
    visit[here] = True
    output.append(here)
    for there in adj[here]:
        if not visit[there]:
            dfs(there)


def bfs(here):
    queue.append(1)
    visit[1] = True

    while len(queue) != 0:
        here = queue.popleft()
        adj[here].sort()
        output.append(here)
        for there in adj[here]:
            if not visit[there]:
                dist[there - 1] = dist[here - 1] + 1
                queue.append(there)
                visit[there] = True


n, m = map(int, input().split())
adj = [[] for i in range(n + 1)]
visit = [False] * (n + 1)
dist = [0] * n
output = []
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# cnt = 0
# for here in range(1, n + 1):
#     if not visit[here]:
#         dfs(here)
#         cnt += 1

bfs(1)
print(*dist)
