# Merge Sort: Recursive, divide-and-conquer sorting algorithm that repeatedly divides an array into halves, sorts the subarrays, and then merges them in a sorted manner.

from utils.sort import Sort


def merge_(num_list, left, right, mid):
    left_copy = num_list[left: mid + 1]
    right_copy = num_list[mid + 1: right + 1]

    l_counter, r_counter = 0, 0
    sorted_counter = left

    while l_counter < len(left_copy) and r_counter < len(right_copy):
        if left_copy[l_counter] <= right_copy[r_counter]:
            num_list[sorted_counter] = left_copy[l_counter]
            l_counter += 1
        else:
            num_list[sorted_counter] = right_copy[r_counter]
            r_counter += 1

        sorted_counter += 1

    while l_counter < len(left_copy):
        num_list[sorted_counter] = left_copy[l_counter]
        l_counter += 1
        sorted_counter += 1

    while r_counter < len(right_copy):
        num_list[sorted_counter] = right_copy[r_counter]
        r_counter += 1
        sorted_counter += 1


def sort(num_list, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    sort(num_list, left, mid)
    sort(num_list, mid + 1, right)

    merge_(num_list, left, right, mid)


def merge():
    Sort(lambda arr: sort(arr, 0, len(arr) - 1)).sort()
