# Stalin Sort: Removes any Item from the Array which is smaller than the previous item

arr = [4, 5, 8, 7, 10, 7, 6, 15]
print(f"Unsorted: {arr}")

for i, d in enumerate(arr):
    try:
        if arr[i + 1] < d:
            arr.remove(arr[i + 1])
    except IndexError:
        pass

print(f"Sorted: {arr}")
