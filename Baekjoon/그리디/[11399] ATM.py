n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
length = n
output = 0
for i in range(n):
    output += arr.pop() * length
    length -= 1
print(output)
