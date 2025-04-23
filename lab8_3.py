import sorting
import time
import random

# List of array sizes to test
sizes = [50000, 100000, 150000, 200000, 250000, 300000]

# put sorting algos in a dictionary
algorithms = {
    "Selection": sorting.selection,
    "Bubble": sorting.bubble,
    "Merge": sorting.merge,
    "Quick": sorting.quick,
    "Heap": sorting.heap,
    "Radix": sorting.radix
}

# Print table header
print("Array Size | Selection | Bubble | Merge | Quick | Heap | Radix")

for size in sizes:
    # Make a list of random numbers. list is length of size
    numbers = [random.randint(1, 1000000) for i in range(size)]
    
    # put current list size in first column
    print(f"{size:<10}", end=" ")

    # Try each sorting algorithm
    for name in algorithms:
        sort_function = algorithms[name]

        # Make a fresh copy of the numbers list to ensure fair calculation
        copy = numbers.copy()

        # calculate excecution time
        start = time.time()
        sort_function(copy)
        end = time.time()

        # Print rxecution time
        time_taken = end - start
        print(f"{time_taken:.2f}      ", end=" ")

    print()  # new line
