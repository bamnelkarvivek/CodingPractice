def swap(n1, n2):
    return n2, n1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Outer loop for passes
        for j in range(0, n - i - 1):  # Inner loop for comparisons
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = swap(arr[j], arr[j + 1])
    return arr

if __name__ == "__main__":
    array = [3, 2, 5, 1, 6, 4]
    print(bubble_sort(array)) # [1, 2, 3, 4, 5, 6]
