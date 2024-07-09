def bubbleSort(arr):
    n = len(arr) # Get length of the array
    # Iterate through the elements
    for i in range(n-1): # range(n) also works but outer loop repeats more than needed
        swapped = False
        for j in range(0, n-i-1): # Iterate through from 0 to n-i-1
            if arr[j] > arr[j+1]: # swap if the elemebt found is greater than the next 
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped: # if no swap required just exit main loop
            return