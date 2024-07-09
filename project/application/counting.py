def countingSort(arr):
    # Find the maximum value in the array to determine the size of the count array
    max_val = max(arr)

    # Initialize the count array with zeros, with size of max_val + 1
    count = [0] * (max_val + 1)

    # Initialize the output array with zeros, with the same size as the input array
    output = [0] * len(arr)

    # Step 1: Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1

    # Step 2: Modify the count array by adding the previous counts (cumulative count)
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # Step 3: Build the output array by placing elements in their correct positions
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]  # Place the element at the correct position in output array
        count[arr[i]] -= 1  # Decrease the count for the placed element
        i -= 1  # Move to the previous element in the input array

    # Step 4: Copy the sorted elements from the output array back to the input array
    for i in range(len(arr)):
        arr[i] = output[i]
