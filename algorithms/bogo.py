# Bogo Sort: Shuffles Entire list, Until the List is Sorted

from utils import get_list, benchmark, is_sorted
import random

arr = get_list()


def sort():
    while not is_sorted(arr):
        random.shuffle(arr)


time = benchmark(sort)

print(f"Sorted: {arr}")
print(time)
