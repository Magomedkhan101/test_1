
def fibonacci(num):
    fib_1 = 0
    fib_2 = 1
    print(f'{fib_1}\n{fib_2}')
    while num > 2:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        num -= 1
    return fib_2
