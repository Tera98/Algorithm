# 11050 : 이항 계수 1

def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1


n, k = map(int, input().split())
print(int(factorial(n) / factorial(k) / factorial(n - k)))
