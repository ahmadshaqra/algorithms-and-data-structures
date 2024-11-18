"""
    Quick Sort

    A sorting algorithm.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray
from random import randint

def quick_sort(array: StaticArray) -> None:
    """
        Sorts the array.

        Time Complexity:
            Worst Case: O(n^2)
            Average Case: O(n*log(n))
            Best Case: O(n*log(n))

        Space Complexity:
            Worst Case: O(n)
            Average Case: O(log(n))
            Best Case: O(log(n))

        Args:
            array (StaticArray): the array to be sorted.

        Raises:
            TypeError: if comparison operators are not supported between types of elements in array.
    """

    quick_sort_aux(array, 0, len(array) - 1)

def quick_sort_aux(array: StaticArray, start: int, end: int) -> None:
    """
        Auxiliary quick sort function.

        Time Complexity:
            Worst Case: O(n^2)
            Average Case: O(n*log(n))
            Best Case: O(n*log(n))

        Space Complexity:
            Worst Case: O(n)
            Average Case: O(log(n))
            Best Case: O(log(n))

        Args:
            array (StaticArray): the array to be sorted.
            start (int): the start index of the section to be sorted.
            end (int): the end index of the section to be sorted.

        Raises:
            TypeError: if comparison operators are not supported between types of elements in array.
    """

    # checks if there is more than one element to sort
    if end - start >= 1:

        # partitions array and gets the pivot position
        pivot = partition(array, start, end, randint(start, end))

        # recursively sorts left and right sides
        quick_sort_aux(array, start, pivot)
        quick_sort_aux(array, pivot + 1, end)

def partition(array: StaticArray, start: int, end: int, pivot: int) -> int:
    """
        Partitions the array section by a pivot.

        Time Complexity:
            Worst Case: O(n)
            Average Case: O(n)
            Best Case: O(n)

        Space Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Args:
            array (StaticArray): the array to be partitioned.
            start (int): the start index of the section to be partitioned.
            end (int): the end index of the section to be partitioned.
            pivot (int): the pivot index to partition the section by.

        Returns:
            int: the pivot index after partitioning.

        Raises:
            TypeError: if comparison operators are not supported between types of elements in array.
    """

    # swaps pivot with first element
    array[pivot], array[start] = array[start], array[pivot]

    # sets up left and right pointers
    left = start + 1
    right = end

    # continues until left and right pointers cross
    while left <= right:

        # moves left to right until it finds an element larger than the pivot
        while left <= right and array[left] <= array[start]:
            left += 1

        # moves right to left until it finds an element smaller than or equal to the pivot
        while left <= right and array[right] > array[start]:
            right -= 1

        # swaps elements at left and right if they haven't crossed
        if left <= right:
            array[left], array[right] = array[right], array[left]

    # swaps element at right with pivot
    array[right], array[start] = array[start], array[right]

    # returns pivot position after partitioning
    return right
