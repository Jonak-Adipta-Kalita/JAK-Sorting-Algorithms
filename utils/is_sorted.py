from typing import List

def is_sorted(arr: List) -> bool:
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
