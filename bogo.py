# Bogo Sort: Shuffles Entire list, Until the List is Sorted

import random, time

arr = [4, 5, 8, 7, 10, 7, 6, 15]
print(f"Unsorted: {arr}")

st = time.perf_counter()

while not all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)):
    random.shuffle(arr)

et = time.perf_counter()

print(f"Sorted: {arr}")
print(f"Took {et-st:.3f} sec")
