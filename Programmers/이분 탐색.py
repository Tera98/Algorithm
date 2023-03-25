# 3/13 [이분 탐색]

n, x = map(int, input().split())
a = list(map(int, input().split()))
lo, hi = -1, n

while lo + 1 < hi:
    mid = (lo + hi) // 2
    print(str(lo) + " " + str(hi))
    if a[mid] < x:
        lo = mid
    else:
        hi = mid
print(hi)
