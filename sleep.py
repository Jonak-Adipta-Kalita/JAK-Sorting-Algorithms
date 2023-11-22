# Sleep Sort: Sorts elements by assigning each element a sleep time proportional to its value and appends the array after sleeping.

from utils import get_list, benchmark
import time, _thread

arr = get_list()

def sort():
    global arr

    new_list = []
    for i in arr:
        _thread.start_new_thread(lambda x: (time.sleep(x), new_list.append(x)), (i,))

    arr = new_list

time = benchmark(sort)

print(f"Sorted: {arr}")
print(time)
