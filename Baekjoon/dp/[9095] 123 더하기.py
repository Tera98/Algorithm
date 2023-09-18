from collections import deque

n = int(input())
dp = [0] * 12
deq = deque()
deq.append(0)

while len(deq):
    try:
        tmp = deq.popleft()
        if tmp < 12:
            deq.append(tmp + 1)
            deq.append(tmp + 2)
            deq.append(tmp + 3)
        for i in range(3):
            dp[tmp + i + 1] += 1
    except IndexError:
        pass
output = []
for i in range(n):
    output.append(int(input()))
for i in range(n):
    print(dp[output[i]])
