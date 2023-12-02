# Bogo Sort: Shuffles Entire list, Until the List is Sorted

from utils.sort import Sort
from typing import List
import random


def algorithm(arr: List):
    while not Sort.is_sorted(arr):
        random.shuffle(arr)


bogo = Sort(algorithm)
bogo.sort()
