"""
    Sorting Test

    Benchmarking for sorting algorithms.

    Author: Ahmad Abu-Shaqra
"""

from random import shuffle
from time import time
from data_structures.arrays.static_array import StaticArray
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.selection_sort import selection_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.counting_sort import counting_sort
from algorithms.sorting.radix_sort import radix_sort
from typing import Callable

def sorting_test(sorting_algorithms: list[Callable], size: int) -> None:
    """
        Benchmarks each given algorithm on a shuffled array.

        Args:
            sorting_algorithms (list[Callable]): the list of sorting algorithms to run.
            size (int): the size of the array to run the sorting algorithms on.
    """

    # creates array of inputted size
    print("\n... Creating Array ...", end="", flush=True)
    array = StaticArray(size)
    array.set_array([i for i in range(size)])
    print("\r\r", end="", flush=True)

    # runs each sorting algorithm individually
    for sorting_algorithm in sorting_algorithms:

        # displays sorting algorithm name
        name = sorting_algorithm.__name__
        name = name.upper()
        name = name.replace('_', ' ')
        print(f"{name}                      ")

        # shuffles array
        print("... Shuffling Array ...", end="", flush=True)
        shuffle(array.array)

        # sorts array
        print("\r... Sorting Array ...  ", end="", flush=True)
        start_time = time()
        sorting_algorithm(array)
        end_time = time()

        # verifies array is sorted
        is_sorted = True
        print("\r... Verifying Sort ...", end="", flush=True)
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                is_sorted = False

        # displays result
        print(f"\rSorted: {is_sorted}          ")
        print(f"Items Sorted: {len(array)}")
        print(f"Time Taken: {round(end_time - start_time, 3)}s\n")

if __name__ == '__main__':
    sorting_test([counting_sort, radix_sort, quick_sort, merge_sort, selection_sort, insertion_sort, bubble_sort], 10000)
