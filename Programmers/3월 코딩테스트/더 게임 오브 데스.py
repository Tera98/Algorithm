# 3/27 코딩 테스트

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
visit = [0] * n
i = k - 1
out = "NO"
while visit[i] == 0:
    if i == m - 1:
        out = "YES"
        break
    else:
        visit[i] = 1
        i = a[i] - 1

print(out)
