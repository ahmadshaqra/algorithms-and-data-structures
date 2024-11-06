"""
    Selection Sort

    A sorting algorithm.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray

def selection_sort(array: StaticArray) -> None:
    """
        Sorts the array.

        Time Complexity:
            Worst Case: O(n^2)
            Average Case: O(n^2)
            Best Case: O(n^2)

        Space Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Args:
            array (StaticArray): the array to be sorted.

        Raises:
            TypeError: if comparison operators are not supported between types of elements in array.
    """

    # every iteration swaps the smallest element to the start
    for i in range(len(array)):

        # finds the smallest element in the unsorted section
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        # swaps smallest element to the end of the sorted section
        array[i], array[min_index] = array[min_index], array[i]
