import time, random
from sorting_algorithms import selection_sort, bubble_sort, merge_sort, quick_sort, heap_sort, radix_sort

def generate_data(n):
    return [random.randint(0, 1000000) for _ in range(n)]

sizes = [50000, 100000, 150000, 200000, 250000, 300000]
sorts = [("Selection", selection_sort), ("Bubble", bubble_sort), ("Merge", merge_sort), 
         ("Quick", quick_sort), ("Heap", heap_sort), ("Radix", radix_sort)]

print("Array Size\t" + "\t".join([s[0] for s in sorts]))

for size in sizes:
    print(f"{size}\t", end="")
    for name, func in sorts:
        data = generate_data(size)
        start = time.time()
        func(data.copy())  # make sure original isn't changed
        end = time.time()
        print(f"{end - start:.2f}s", end="\t")
    print()
