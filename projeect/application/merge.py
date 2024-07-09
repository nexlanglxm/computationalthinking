def mergeSort(arr):
    # Base case: If the array has one or no elements, it is already sorted
    if len(arr) > 1:
        # Find the middle point and split the array into left and right halves
        mid = len(arr) // 2
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        # Recursively sort both halves
        mergeSort(L)  # Sort the left half
        mergeSort(R)  # Sort the right half

        # Initialize pointers for L, R, and the main array
        i = j = k = 0

        # Merge the sorted halves back into the main array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:  # If the current element of L is smaller than the current element of R
                arr[k] = L[i]  # Place the smaller element in the main array
                i += 1  # Move the pointer in L forward
            else:
                arr[k] = R[j]  # Place the smaller element in the main array
                j += 1  # Move the pointer in R forward
            k += 1  # Move the pointer in the main array forward

        # If there are any remaining elements in L, copy them to the main array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # If there are any remaining elements in R, copy them to the main array
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1