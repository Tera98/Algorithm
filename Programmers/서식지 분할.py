# 2/10 [상] [누적 합]

n = int(input())
data = list(input())
cnt = [[0] * n for _ in range(26)]

for i in range(26):
    for j in range(n):
        if data[j] == chr(ord('a') + i):
            cnt[i][j] = 1

maxi = 0

for i in range(n - 1):
    tmp = 0
    for j in range(26):
        arr1 = cnt[j][:i + 1]
        arr2 = cnt[j][i + 1:]
        if sum(arr1) > 0:
            tmp += 1
        if sum(arr2) > 0:
            tmp += 1
    maxi = max(maxi, tmp)

print(maxi)
