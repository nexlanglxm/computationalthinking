import bubble, selection, insertion, merge, counting, extras

def display_menu():
    print("=================")
    print("MENU")
    print("=================")
    print("1 - Bubble Sort")
    print("2 - Selection Sort")
    print("3 - Insertion Sort")
    print("4 - Merge Sort")
    print("5 - Counting Sort")
    print("6 - Show Student Number")
    print("7 - Benchmark comparisons (warning: this may take some time to run)")
    print("x - Exit Application")

def main():
   # display_menu()
    
    while True:
        display_menu()
        choice = input("Choice : ")

        if choice == "1":
            extras.benchmark_sorting_algorithm(bubble.bubbleSort)
            
        elif choice == "2": 
            extras.benchmark_sorting_algorithm(selection.selectionSort)

        elif choice == "3":
            extras.benchmark_sorting_algorithm(insertion.insertionSort)

        elif choice == "4":
            extras.benchmark_sorting_algorithm(merge.mergeSort)

        elif choice == "5":
            extras.benchmark_sorting_algorithm(counting.countingSort)

        elif choice == "6":
            print("Student number is G00425634, so we will be using 4, 2, 5, 6, 3, 4 as our numbers.")

        elif choice == "7":
            extras.benchmark(counting.countingSort, merge.mergeSort, insertion.insertionSort, selection.selectionSort, bubble.bubbleSort)

        elif choice == "x":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()