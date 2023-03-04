n, m = map(int, input().split())

adj = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b)
    adj[b-1].append(a)

for i in range(n):
    if len(adj[i]) != 0:
        adj[i].sort()
        print(*adj[i])
    else:
        print(-1)

