"""
    Merge Sort

    A sorting algorithm.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray

def merge_sort(array: StaticArray) -> None:
    """
        Sorts the array.

        Time Complexity:
            Worst Case: O(nlog(n))
            Average Case: O(nlog(n))
            Best Case: O(nlog(n))

        Space Complexity:
            Worst Case: O(n)
            Average Case: O(n)
            Best Case: O(n)

        Args:
            array (StaticArray): the array to be sorted.

        Raises:
            TypeError: if comparison operators are not supported between types of elements in array.
    """

    # checks if array can be split
    if len(array) > 1:

        # creates left and right arrays
        left = StaticArray(len(array) // 2)
        right = StaticArray(len(array) - len(array) // 2)

        # copies data to left and right arrays
        for i in range(len(left)):
            left[i] = array[i]
        for i in range(len(right)):
            right[i] = array[i + len(array) // 2]

        # recursively sorts left and right halves
        merge_sort(left)
        merge_sort(right)

        # merges sorted halves
        merge(array, left, right)

def merge(array: StaticArray, left: StaticArray, right: StaticArray) -> None:
    """
        Merges left and right halves of an array into a combined sorted array.

        Time Complexity:
            Worst Case: O(n)
            Average Case: O(n)
            Best Case: O(n)

        Space Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Args:
            array (StaticArray): the array to be written to.
            left (StaticArray): the left half of the array to be merged.
            right (StaticArray): the right half of the array to be merged.

        Raises:
            TypeError: if comparison operators are not supported between types of elements in array.
    """

    # initialises array indexes
    array_index = left_index = right_index = 0

    # merges left and right arrays until one of them is empty
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            array[array_index] = right[right_index]
            right_index += 1
        else:
            array[array_index] = left[left_index]
            left_index += 1
        array_index += 1

    # merges the remaining elements
    while left_index < len(left):
        array[array_index] = left[left_index]
        left_index += 1
        array_index += 1
    while right_index < len(right):
        array[array_index] = right[right_index]
        right_index += 1
        array_index += 1
