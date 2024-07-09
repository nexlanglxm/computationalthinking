def insertionSort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(1, n):
        key = arr[i]  # Element to be positioned
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key element in the correct position