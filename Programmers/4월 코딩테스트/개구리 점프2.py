from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * n
for _ in range(k):
    arr.append(0)
    dp.append(1)
deq = deque()
deq.append(0)
while deq:
    tmp = deq.popleft()
    if tmp > n:
        continue
    for i in range(1, k + 1):
        if dp[tmp + i] == 0:
            dp[tmp + i] = abs(arr[tmp] - arr[tmp + i]) + dp[tmp]
            deq.append(tmp + i)
        else:
            dp[tmp + i] = min(dp[tmp + i], abs(arr[tmp] - arr[tmp + i]) + dp[tmp])

print(dp[n - 1])
