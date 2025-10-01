def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n-2)

if __name__ == "__main__":
    print(fibonacci_recursive(5)) # 5
    print(fibonacci_recursive(6)) # 8