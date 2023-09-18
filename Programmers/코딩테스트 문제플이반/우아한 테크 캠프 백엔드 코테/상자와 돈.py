n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
i, day = 0, 0
while day < k:
    if (m // 10000) * a[i] <= 100000:
        m += (m // 10000) * a[i]
    else:
        i += 1
        continue
    day += 1
print(m)

# enumerate 
# 리스트를 넣으면 인덱스 값을 다 붙여준다
