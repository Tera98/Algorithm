# 10866 : 덱
import sys
from collections import deque

n = int(input())
stack = deque()

for i in range(n):
    a = sys.stdin.readline().rstrip().split()

    if a[0] == "push_front":
        stack.appendleft(a[1])

    elif a[0] == "push_back":
        stack.append(a[1])

    elif a[0] == "pop_front":
        if len(stack) != 0:
            print(stack.popleft())
        else:
            print(-1)

    elif a[0] == "pop_back":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)

    elif a[0] == "size":
        print(len(stack))

    elif a[0] == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)

    elif a[0] == 'front':
        if len(stack) != 0:
            print(stack[0])
        else:
            print(-1)
    else:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
