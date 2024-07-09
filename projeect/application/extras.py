import random, time
# function to generate random arrays with different input sizes
def generate_random_array(size): 
    student_number = [4, 2, 5, 6, 3, 4] # digits from my student number G00425634
    array = [random.choice(student_number) for _ in range(size)] # Generate a random array using digits from student number
    return array

def benchmark_sorting_algorithm(algorithm):
    # List of array sizes to test the algorithm with
    sizes = [10, 100, 250, 500, 1000, 1250, 2000, 3000, 5000, 6000, 8000]

    # Iterate through each size in the list
    for size in sizes:
        # Generate a random array of the current size
        arr = generate_random_array(size)
        total_time = 0
        # Repeat the sorting 10 times to get a more accurate measure of time
        for _ in range(10):
            # Make a copy of the array to sort, to keep the original unsorted for next iteration
            arr_copy = arr.copy()
            # Record the start time of the sort
            start_time = time.time()
            # Execute the sorting algorithm
            algorithm(arr_copy)
            # Record the end time of the sort
            end_time = time.time()
            # Calculate the time taken for this sort and add to total_time
            total_time += (end_time - start_time) * 1000
        # Calculate the average time over the 10 sorts
        avg_time = total_time / 10
        # Print the average time taken for the current size
        print(f"Average time taken by {algorithm.__name__} for input size {size}: {avg_time:.3f} ms")
        
def benchmark(*algorithms):
    sizes = [10, 100, 250, 500, 1000, 1250, 2000, 3000, 5000, 6000, 8000]
    algorithm_names = [algorithm.__name__ for algorithm in algorithms]

    # Print header with input sizes
    header = "Input size".ljust(15) # using ljust to tidy up output formatting
    for size in sizes:
        header += str(size).ljust(10)
    print(header)
    # iterate over each algo & name simultaneously using zip
    for algorithm_name, algorithm in zip(algorithm_names, algorithms):
        row = algorithm_name.ljust(15) # add the algorithm name
        for size in sizes: # iterate over the sizes
            total_time = 0
            for _ in range(10): #repeat benchmark 10 times for accuracy
                arr = generate_random_array(size)
                start_time = time.time()
                algorithm(arr) # call the sorting algorihtm
                end_time = time.time()
                total_time += (end_time - start_time) * 1000 # converts to milliseconds
            average_time = total_time / 10 # calculate the average time
            row += "{:.3f}".format(average_time).ljust(10)
        print(row)