# Insertion Sort: Builds the final sorted array one item at a time by comparisons

from utils import get_list, benchmark

arr = get_list()

def sort():
    for i, d in enumerate(arr): 
        j = i-1
        while j >= 0 and d < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = d

time = benchmark(sort)

print(f"Sorted: {arr}")
print(time)
