# 1003 : 피보나치 함수
import sys

n = int(input())
d = [0] * 43
d[0] = 0
d[1], d[2], d[42] = 1, 1, 1
for i in range(3, 41):
    d[i] = d[i - 1] + d[i - 2]
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    print(str(d[tmp - 1]) + " " + str(d[tmp]))
