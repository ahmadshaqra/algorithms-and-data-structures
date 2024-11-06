"""
    Bubble Sort

    A sorting algorithm.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray

def bubble_sort(array: StaticArray) -> None:
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

    # every iteration swaps the largest element to the end
    for i in range(len(array)):

        # checks every pair of elements in unsorted section
        for j in range(len(array) - i - 1):

            # swaps elements if previous element is smaller
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
