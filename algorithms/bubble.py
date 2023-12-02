# Bubble Sort: Repeatedly steps through the List, comparing the current element with the one after it, swapping their values if needed.

from utils.sort import Sort
from typing import List


def algorithm(arr: List):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


bubble = Sort(algorithm)
bubble.sort()
