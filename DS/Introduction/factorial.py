import time


def factorial_recursion(n):
    if n <= 1:
        return 1
    else:
        return factorial_recursion(n - 1) * n


def factorial_loop(n):
    out = 1
    for i in range(1, n + 1):
        out *= i
    return out


# recursion vs loop
factorial_num = 200
start_time = time.time()
print(factorial_recursion(factorial_num))
print("Recursion time : %f" % (time.time() - start_time))
start_time = time.time()
print(factorial_loop(factorial_num))
print("loop time : %f" % (time.time() - start_time))
