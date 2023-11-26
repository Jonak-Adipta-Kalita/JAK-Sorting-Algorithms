# Stalin Sort: Removes any Item from the Array which is smaller than the previous item

from utils import get_list, benchmark

arr = get_list()

def sort():
    for i, d in enumerate(arr):
        try:
            while arr[i + 1] < d:
                arr.remove(arr[i + 1])
        except IndexError:
            pass

time = benchmark(sort)

print(f"Sorted: {arr}")
print(time)
