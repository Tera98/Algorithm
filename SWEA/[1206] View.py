n = int(input())
a = list(map(int, input().split()))
out = 0

for i in range(2, len(a) - 2):
    tmp = sorted(a[i - 2:i + 3], reverse=True)
    if a[i] == tmp[0]:
        out += tmp[0] - tmp[1]

print(out) # test case 고려 x
