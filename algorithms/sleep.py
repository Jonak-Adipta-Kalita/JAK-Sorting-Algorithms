# Sleep Sort: Sorts elements by assigning each element a sleep time proportional to its value and appends the array after sleeping.

from utils.sort import Sort
from typing import List
from threading import Timer
import time


def algorithm(arr: List):
    new_arr = []
    max_element = max(arr)

    def append(item):
        new_arr.append(item)

    for i in arr:
        Timer(i, append, (i,)).start()
    time.sleep(max_element + 1)

    arr.clear()
    arr.extend(new_arr)


sleep = Sort(algorithm)
sleep.sort()
