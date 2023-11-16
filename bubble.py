# Bubble Sort: Repeatedly steps through the List, comparing the current element with the one after it, swapping their values if needed.

from utils import get_list, benchmark

arr = get_list()

def sort():
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j]  = arr[j + 1]
                arr[j + 1] = temp

time = benchmark(sort)

print(f"Sorted: {arr}")
print(time)
