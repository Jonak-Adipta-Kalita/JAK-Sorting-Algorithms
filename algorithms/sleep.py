# Sleep Sort: Sorts elements by assigning each element a sleep time proportional to its value and appends the array after sleeping.

from utils import get_list, benchmark
from time import sleep
from threading import Timer

arr = get_list()


def sort():
    global arr

    new_arr = []
    max_element = max(arr)

    def append(item):
        new_arr.append(item)

    for i in arr:
        Timer(i, append, (i,)).start()
    sleep(max_element + 1)

    arr = new_arr


time = benchmark(sort)

print(f"Sorted: {arr}")
print(time)
