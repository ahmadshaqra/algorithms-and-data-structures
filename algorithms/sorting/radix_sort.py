"""
    Radix Sort

    A sorting algorithm.

    Author: Ahmad Abu-Shaqra
"""

from data_structures.arrays.static_array import StaticArray

def radix_sort(array: StaticArray) -> None:
    """
        Sorts the array.

        Time Complexity:
            Worst Case: O(n*m)
            Average Case: O(n*m)
            Best Case: O(n*m)

        Space Complexity:
            Worst Case: O(n)
            Average Case: O(n)
            Best Case: O(n)

        Args:
            array (StaticArray): the array to be sorted.

        Raises:
            TypeError: if elements in array are not integers.
            ValueError: if element in array is negative.
    """

    # finds the maximum number of digits
    digits = len(str(max(array)))

    # initialises indexed array
    indexed_array = StaticArray(len(array))
    for i in range(len(indexed_array)):

        # checks if value is negative
        if array[i] < 0:
            raise ValueError("value must be non-negative integer.")

        # sets key-value tuple
        indexed_array[i] = (0, array[i])

    # sorts array on each digit
    for i in range(digits):

        # indexes elements by the current digit
        for j in range(len(indexed_array)):
            indexed_array[j] = ((indexed_array[j][1] // 10 ** i) % 10, indexed_array[j][1])

        # stable sorts the array by the element digits
        modified_counting_sort(indexed_array)

    # copies indexed array into array
    for i in range(len(array)):
        array[i] = indexed_array[i][1]

def modified_counting_sort(array: StaticArray) -> None:
    """
        Stable sorts the array based on the digit.

        Time Complexity:
            Worst Case: O(n)
            Average Case: O(n)
            Best Case: O(n)

        Space Complexity:
            Worst Case: O(n)
            Average Case: O(n)
            Best Case: O(n)

        Args:
            array (StaticArray): the array to be sorted.

        Raises:
            TypeError: if elements in array are not tuples of integers.
    """

    # creates a count array and initialises all values to an empty linked list
    count_array = StaticArray(10)
    for i in range(10):
        count_array[i] = [] # TODO: CHANGE TO CUSTOM LINKED LIST IMPLEMENTATION

    # adds elements in the array to the count array
    for i in range(len(array)):
        count_array[array[i][0]].append(array[i])

    # copies count array into array
    i = 0
    for j in range(10):
        for k in range(len(count_array[j])):
            array[i] = count_array[j][k]
            i += 1
