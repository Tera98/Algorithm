# 4/4
from collections import deque

n, k = map(int, input().split())
dp = [0] * 100001
deq = deque()
deq.append(n)

while dp[k] == 0:
    tmp = deq.popleft()

    if tmp * 2 < 100000:
        if dp[tmp * 2] == 0:
            dp[tmp * 2] = dp[tmp] + 1
        else:
            dp[tmp * 2] = min(dp[tmp] + 1, dp[tmp * 2])
        deq.append(tmp * 2)

    if tmp - 1 < 100000:
        if dp[tmp - 1] == 0:
            dp[tmp - 1] = dp[tmp] + 1
        else:
            dp[tmp - 1] = min(dp[tmp] + 1, dp[tmp - 1])
        deq.append(tmp - 1)

    if tmp + 1 < 100000:
        if dp[tmp + 1] == 0:
            dp[tmp + 1] = dp[tmp] + 1
        else:
            dp[tmp + 1] = min(dp[tmp] + 1, dp[tmp + 1])
        deq.append(tmp + 1)

print(dp[k])
