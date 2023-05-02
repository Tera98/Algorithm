m = int(input())
arr = [[] for _ in range(0, m + 1)]
for _ in range(0, m - 1):
    a, b = map(int, input().split())
m = int(input())
output = 1
for _ in range(0, m):
    a, b, c = map(int, input().split())
    if a == 1:
        output += 1
    else:
        output -= 1
print(output)

