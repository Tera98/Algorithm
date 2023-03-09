# 10816 : 숫자 카드 2
import sys

n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dict1 = {}

for i in data:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

for i in arr:
    if i in dict1:
        print(dict1[i], end=" ")
    else:
        print(0, end=" ")
