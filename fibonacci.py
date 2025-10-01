def fibonacci_recursive(n):
    """ Return index of fibonacci sequence using recursive approach """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n-2)

def fib_list_recursive(n):
    """ Return fibonacci sequence using recursive approach """
    if n < 0:
        return []
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    sequence = fib_list_recursive(n - 1) # get sequence up to n-1
    sequence.append(sequence[-1] + sequence[-2])  # append nth number
    
    return sequence

def fibonacci_iterative(n):
    """ Return index of fibonacci sequence using iterative approach """
    sequence = [0,1]
    for i in range(2,n+1):
        sequence.append(sequence[i-2]+sequence[i-1])
    return sequence[n]

if __name__ == "__main__":
    print(fibonacci_recursive(5)) # 5
    print(fibonacci_recursive(6)) # 8
    print(fibonacci_iterative(6)) # 8
    print(fib_list_recursive(5))  # [0, 1, 1, 2, 3, 5]