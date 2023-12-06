from algorithms import *
import sys

algorithms = {
    "bogo": "Shuffles Entire list, Until the List is Sorted",
    "bubble": "Repeatedly steps through the List, comparing the current element with the one after it, swapping their values if needed.",
    "insertion": "Builds the final sorted array one item at a time by comparisons",
    "merge": "Divide and Conquer Algorithm, that divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.",
    "sleep": "Sorts elements by assigning each element a sleep time proportional to its value and appends the array after sleeping.",
    "stalin": "Iterates through the list, removing any element that is not in order.",
}

choice = ""
if sys.argv[1:]:
    choice = sys.argv[1].lower()
else:
    for algorithm in algorithms:
        print(f"{algorithm}: {algorithms[algorithm]}")

    choice = str(input("\nEnter the algorithm you want to use: ")).lower()

if choice not in algorithms:
    print("Invalid Algorithm")
    exit()

print()
if choice == "bogo":
    bogo.sort()
elif choice == "bubble":
    bubble.sort()
elif choice == "insertion":
    insertion.sort()
elif choice == "merge":
    merge.sort()
elif choice == "sleep":
    sleep.sort()
elif choice == "stalin":
    stalin.sort()
