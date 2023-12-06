# Insertion Sort: Builds the final sorted array one item at a time by comparisons

from utils.sort import Sort
from typing import List


def algorithm(arr: List):
    for i, d in enumerate(arr):
        j = i - 1
        while j >= 0 and d < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = d


def sort(): Sort(algorithm).sort()
