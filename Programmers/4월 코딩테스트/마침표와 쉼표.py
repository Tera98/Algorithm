n = input()
output = 'YES'
for _ in range(0, len(n) - 1):
    if n[_] == '.':
        output = 'NO'
if n[-1] != '.' or n[0] == ',':
    output = 'NO'

print(output)
