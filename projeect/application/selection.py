def selectionSort(arr):
    n = len(arr) 
    for i in range(n): 
        min_idx = i   # find the index of the minimum element (unsorted)
        for j in range(i+1, n):  
            if arr[j] < arr[min_idx]: 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Swap the found minimum element with the first element