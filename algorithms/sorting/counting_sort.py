"""
    Counting Sort

    A sorting algorithm.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray

def counting_sort(array: StaticArray) -> None:
    """
        Sorts the array.

        Time Complexity:
            Worst Case: O(n+m)
            Average Case: O(n+m)
            Best Case: O(n+m)

        Space Complexity:
            Worst Case: O(m)
            Average Case: O(m)
            Best Case: O(m)

        Args:
            array (StaticArray): the array to be sorted.

        Raises:
            TypeError: if elements in array are not integers.
    """

    # gets minimum and maximum value of array elements
    min_value = min(array)
    max_value = max(array)

    # creates a count array and initialises all values to zero
    count_array = StaticArray(max_value - min_value + 1)
    for i in range(len(count_array)):
        count_array[i] = 0

    # counts the elements in the array
    for i in range(len(array)):
        count_array[array[i] - min_value] += 1

    # copies count array into array
    i = 0
    for j in range(len(count_array)):
        for _ in range(count_array[j]):
            array[i] = j + min_value
            i += 1
