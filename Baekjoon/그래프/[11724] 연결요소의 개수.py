import sys
from collections import deque


def cnt_connect():
    global graph, deq, visited
    cnt = 0
    deq.append(1)

    for j in range(n + 1):
        if not visited[j]:
            deq.append(j)
            while deq:
                tmp = deq.popleft()
                if not visited[tmp]:
                    for k in graph[tmp]:
                        if not visited[k]:
                            deq.append(k)
                    visited[tmp] = True
            cnt += 1

    return cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
deq = deque()

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

print(cnt_connect())
