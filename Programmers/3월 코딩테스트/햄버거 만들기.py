# 3/27 코딩 테스트

n, m = map(int, input().split())
count = 0
while n > 1 and m > 0:
    count += 1
    n -= 2
    m -= 1
print(count)
