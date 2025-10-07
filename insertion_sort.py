def insertion_sort(numbers):
    for index in range(1, len(numbers)):
        current = numbers[index]   # element to insert
        pos = index

        # Shift larger elements to the right
        while pos > 0 and numbers[pos - 1] > current:
            numbers[pos] = numbers[pos - 1]
            pos -= 1

        # Insert current element at the correct position
        numbers[pos] = current

    return numbers


if __name__ == "__main__":
    numbers = [2, 3, 41, 1, 4, 5, 8, 6, 0]
    print(insertion_sort(numbers))
