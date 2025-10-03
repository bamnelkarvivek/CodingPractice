def swap(n1, n2):
    return n2, n1

def selection_sort(arr):
    n = len(arr)
    for i in range(n):  # Outer loop
        min_index = i
        for j in range(i + 1, n):  # Find index of smallest element
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap only once (if needed)
        if min_index != i:
            arr[i], arr[min_index] = swap(arr[i], arr[min_index])
    return arr

if __name__ == "__main__":
    array = [3, 2, 5, 1, 6, 4]
    print(selection_sort(array))  # [1, 2, 3, 4, 5, 6]
