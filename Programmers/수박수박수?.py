n = int(input())
tmp = n // 2
out = ""
for _ in range(tmp):
    out += "수박"
if n % 2 != 0:
    out += "수"
print(out)
