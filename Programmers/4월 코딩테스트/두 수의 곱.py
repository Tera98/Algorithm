n = int(input())
arr = list(map(int, input().split()))
output = -100000
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            continue
        else:
            output = max(output, arr[i] * arr[j])
print(output)