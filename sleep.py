# Sleep Sort: Sorts elements by assigning each element a sleep time proportional to its value and appends the array after sleeping.

from utils import get_list, benchmark
import time, threading

arr = get_list()

def sort():
    pass

time = benchmark(sort)

print(f"Sorted: {arr}")
print(time)
