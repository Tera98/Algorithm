# 3/15 [이분 탐색]
import sys


def binomial(num):
    lo, hi = -1, n
    if num % a[-1] == 0:
        num = a[-1]
    else:
        num %= a[-1]
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if a[mid] < num:
            lo = mid
        else:
            hi = mid
    return hi + 1


n = int(input())
length, a, total = 0, [], 0
data = list(map(int, sys.stdin.readline().rstrip().split()))

for i in data:
    length += i
    a.append(length)

x = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))

for i in data:
    total = (total + binomial(i)) % 1000000007

print(total)
