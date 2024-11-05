"""
    Binary Search

    A searching algorithm for sorted arrays.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray
from typing import TypeVar

E = TypeVar('E')

def binary_search(array: StaticArray, element: E) -> int | None:
    """
        Searches through array until element is found.

        Time Complexity:
            Worst Case: O(log(n))
            Average Case: O(log(n))
            Best Case: O(1)

        Space Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Args:
            array (StaticArray): the array to be searched.
            element (E): the element to search for.

        Returns:
            int: the index of the element if found, None otherwise.

        Raises:
            TypeError: if comparison operators are not supported between types of elements in array.
    """

    # initialises lo and hi pointers
    lo = 0
    hi = len(array) - 1

    # loops until lo is greater than hi
    while lo <= hi:

        # gets the index of the middle element
        index = (hi + lo) // 2

        # compares the element at the index to the given element
        if array[index] == element:
            return index
        elif array[index] > element:
            hi = index - 1
        elif array[index] < element:
            lo = index + 1

    # returns None if the element wasn't found
    return None
