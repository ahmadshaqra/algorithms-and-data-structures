"""
    Linear Search

    A searching algorithm for unsorted arrays.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray
from typing import TypeVar

E = TypeVar('E')

def linear_search(array: StaticArray, element: E) -> int | None:
    """
        Searches through array until element is found.

        Time Complexity:
            Worst Case: O(n)
            Average Case: O(n)
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
    """

    # initialises index
    index = 0

    # increments index until element is found or the entire array is checked
    while (index < len(array) and array[index] != element):
        index += 1

    # checks if entire array was checked
    if index >= len(array):
        return None

    # returns index
    return index
