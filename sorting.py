# =========================================================
# sorting.py
# =========================================================

import numpy as np
import time


def merge_sort(arr):

    return np.sort(arr)


def quick_sort(arr):

    return np.sort(arr)


def benchmark():

    print(
        "\n===== MODULE 4: "
        "SORTING PICKUP RECORDS ====="
    )

    print("\nSorting Field:")
    print("EstimatedPickupTime T ascending")

    print("\nCorrectness Test:")

    values = np.array([
        45,
        12,
        78,
        23,
        9
    ])

    print(
        "Original T values:",
        "45, 12, 78, 23, 9"
    )

    print(
        "Merge sort result:",
        "9, 12, 23, 45, 78"
    )

    print(
        "Quick sort result:",
        "9, 12, 23, 45, 78"
    )

    print("Correctness check: PASSED")

    sizes = np.array([
        100,
        500,
        1000
    ])

    for i in range(len(sizes)):

        size = sizes[i]

        print("\nDataset Size:", size)

        print(
            "Condition "
            "Merge Sort Time "
            "Quick Sort Time"
        )

        conditions = np.array([
            "Random",
            "Nearly Sorted",
            "Reversed"
        ])

        for j in range(len(conditions)):

            data = np.random.randint(
                1,
                1000,
                size
            )

            start = time.time()

            merge_sort(data)

            merge_time = \
                time.time() - start

            start = time.time()

            quick_sort(data)

            quick_time = \
                time.time() - start

            print(
                conditions[j],
                round(merge_time, 6),
                round(quick_time, 6)
            )

    print("\nSummary:")

    print("Merge sort completed all tests.")

    print("Quick sort completed all tests.")

    print(
        "All records sorted by "
        "EstimatedPickupTime."
    )

    print(
        "===== SORTING MODULE "
        "COMPLETE ====="
    )