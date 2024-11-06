"""
    Insertion Sort

    A sorting algorithm.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray

def insertion_sort(array: StaticArray) -> None:
    """
        Sorts the array.

        Time Complexity:
            Worst Case: O(n^2)
            Average Case: O(n^2)
            Best Case: O(n)

        Space Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Args:
            array (StaticArray): the array to be sorted.

        Raises:
            TypeError: if comparison operators are not supported between types of elements in array.
    """

    # every iteration inserts element into the sorted section
    for i in range(1, len(array)):

        # traverses through sorted section until element is in correct position
        j = i
        while j > 0 and array[j-1] > array[j]:

            # swaps elements and decrements index of element
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
