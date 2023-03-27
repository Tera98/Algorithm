# 3/27 코딩 테스트

from collections import deque

data = input()
a = deque()
out = "YES"
for i in data:
    if i in ("(", "{", "["):
        a.append(i)
    elif i in (")", "}", "]"):
        if len(a) != 0:
            if a[-1] == "(" and i == ")":
                a.pop()
            elif a[-1] == "{" and i == "}":
                a.pop()
            elif a[-1] == "[" and i == "]":
                a.pop()
            else:
                out = "NO"
        else:
            out = "NO"

if len(a) != 0:
    out = "NO"
print(out)
