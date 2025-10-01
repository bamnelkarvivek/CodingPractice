def factorial_recursive(number):
    """Find the factorial using recursive approach"""
    if number == 0 or number == 1:
        return 1
    return number * factorial_recursive(number - 1)

def factorial_iterative(number):
    """Find the factorial using iterative approach"""
    factorial = 1
    while number > 0:
        factorial = factorial * number
        number -= 1
    return factorial

if __name__ == '__main__':
    print(factorial_recursive(5)) # 120
    print(factorial_iterative(5)) # 120
    print(factorial_recursive(0)) # 1
    print(factorial_iterative(0)) # 1