
def fibonacci(num: int):
    fib_1 = 0
    fib_2 = 1
    print(f'{fib_1}\n{fib_2}')
    while num > 2:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        num -= 1
        print(fib_2)
    return 'End!'


def bin_search(lst: list, num: int) -> int:
    start_index = 0
    end_index = len(lst) - 1
    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        guess = lst[mid]
        if guess == num:
            return mid
        elif guess > num:
            end_index = mid - 1
        else:
            start_index = mid + 1
    return None


if __name__ == '__main__':
    print(fibonacci(10))
    print(bin_search([4, 0, 5, 9, 11, 7, 3], 5))
