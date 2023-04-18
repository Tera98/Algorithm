# 4/4
from collections import deque

n, k = map(int, input().split())
dp = [0] * (10 ** 5 + 1)
deq = deque()

if n != k:
    deq.append(n)

while len(deq) > 0:
    tmp = deq.popleft()

    if -1 < tmp - 1 < len(dp):
        if dp[tmp - 1] == 0:
            dp[tmp - 1] = dp[tmp] + 1
            deq.append(tmp - 1)
        else:
            dp[tmp - 1] = min(dp[tmp] + 1, dp[tmp - 1])

    if tmp + 1 < len(dp):
        if dp[tmp + 1] == 0:
            dp[tmp + 1] = dp[tmp] + 1
            deq.append(tmp + 1)
        else:
            dp[tmp + 1] = min(dp[tmp] + 1, dp[tmp + 1])

    if tmp * 2 < len(dp):
        if dp[tmp * 2] == 0:
            dp[tmp * 2] = dp[tmp] + 1
            deq.append(tmp * 2)
        else:
            dp[tmp * 2] = min(dp[tmp] + 1, dp[tmp * 2])

print(dp[k])
