from bisect import *

n = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(list(set(data)))
answer = [0] * n
for idx, num in enumerate(data):
    answer[idx] = bisect_left(sorted_data, num)
print(*answer)
