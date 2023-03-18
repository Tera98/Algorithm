def fibonacci_recursion(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def fibonacci_loop(n):
    a = []
    a.append(1)
    a.append(1)
    for i in range(n - 2):
        a.append(a[-1] + a[-2])
    return a.pop()


# fibonacci
fibonacci_num = 10
print("Fibonacci number %d is %d" % (fibonacci_num, fibonacci_recursion(fibonacci_num)))
print("Fibonacci number %d is %d" % (fibonacci_num, fibonacci_loop(fibonacci_num)))
