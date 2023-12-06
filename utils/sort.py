from typing import Callable, List
import random
import time


class Sort:
    def __init__(self, sorting_func: Callable) -> None:
        self.arr = self.get_list()
        self.sorting_func = sorting_func
        self.time = ""

    def sort(self) -> None:
        self.benchmark()

        if not self.is_sorted(self.arr):
            raise Exception("The array wasn't sorted.")

        print(f"Sorted: {self.arr}")
        print(self.time)

    @staticmethod
    def is_sorted(arr: List) -> bool:
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    def get_list(self) -> List:
        arr = [random.randint(0, 100) for _ in range(30)]
        print(f"Unsorted: {arr}")

        return arr

    def benchmark(self) -> str:
        st = time.perf_counter()
        self.sorting_func(self.arr)
        et = time.perf_counter()

        self.time = f"Took {et-st:.3f} sec"
