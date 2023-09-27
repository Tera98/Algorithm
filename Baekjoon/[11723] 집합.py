import sys

m = int(sys.stdin.readline().rstrip())
S = 0b00000000000000000000

for i in range(m):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == 'add':
        S |= (1 << int(a[1]))
    elif a[0] == 'remove':
        S &= ~(1 << int(a[1]))
    elif a[0] == 'toggle':
        S ^= (1 << int(a[1]))
    elif a[0] == 'check':
        print(1 if S & (1 << int(a[1])) != 0 else 0)
    elif a[0] == 'all':
        S = (1 << 21) - 1
    elif a[0] == 'empty':
        S = 0
