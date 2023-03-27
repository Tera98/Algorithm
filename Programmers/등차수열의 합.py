# 3/14 [이분 탐색]
x = int(input())
lo, hi = -1, x

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if (mid * (mid + 1) / 2) < x:
        lo = mid
    else:
        hi = mid
print(hi)
