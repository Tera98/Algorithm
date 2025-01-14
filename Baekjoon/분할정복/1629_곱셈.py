def div_con(a, b, c):
    if b <= 1:
        return a % c
    elif b % 2 == 0:
        q1 = div_con(a, b // 2, c)
        q2 = q1
    elif b % 2 == 1:
        q1 = div_con(a, b // 2, c)
        q2 = div_con(a, b // 2 + 1, c)
    return (q1 * q2) % c


a, b, c = map(int, input().split())
print(div_con(a, b, c))
