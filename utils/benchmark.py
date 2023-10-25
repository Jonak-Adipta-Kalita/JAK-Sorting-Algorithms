from typing import Callable
import time

def benchmark(func: Callable) -> str:
    st = time.perf_counter()
    func()
    et = time.perf_counter()

    return f"Took {et-st:.3f} sec"
