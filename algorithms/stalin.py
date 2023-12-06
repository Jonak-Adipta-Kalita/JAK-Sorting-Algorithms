# Stalin Sort: Removes any Item from the Array which is smaller than the previous item

from utils.sort import Sort
from typing import List


def algorithm(arr: List):
    for i, d in enumerate(arr):
        try:
            while arr[i + 1] < d:
                del arr[i + 1]
        except IndexError:
            pass


def sort(): Sort(algorithm).sort()
