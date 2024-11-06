"""
    Dynamic Array

    A dynamic-sized array with efficient index-based access.

    Author: Ahmad Abu-Shaqra
"""

from other.utils import validate_type
from data_structures.arrays.static_array import StaticArray
from typing import Generic, TypeVar

E = TypeVar('E')

class DynamicArray(Generic[E]):
    """
        Attributes:
            length: the number of elements in the array.
            size: the size of the array.
            array: the array container.
    """

    def __init__(self) -> None:
        """
            Initialises dynamic array.

            Time Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)

            Space Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)
        """

        self.length = 0
        self.size = 1
        self.array = StaticArray(1)

    def __setitem__(self, index: int, element: E) -> None:
        """
            Sets an element at a specific index.

            Time Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)

            Space Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)

            Args:
                index (int): the index to insert at.
                element (E): the element to insert.

            Raises:
                TypeError: if index is not of type 'int'.
                IndexError: if index is out of range.
        """

        # checks if array is empty
        if self.length == 0:
            raise IndexError("array is empty.")

        # validates index
        validate_type(index, int)
        if index < 0 or index >= self.length:
            raise IndexError(f"index {index} out of range [0-{self.length - 1}].")

        # sets element
        self.array[index] = element

    def __getitem__(self, index: int) -> E:
        """
            Gets an element from a specific index.

            Time Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)

            Space Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)

            Args:
                index (int): the index to get the element from.

            Returns:
                E: the element at the index.

            Raises:
                TypeError: if index is not of type 'int'.
                IndexError: if index is out of range.
        """

        # checks if array is empty
        if self.length == 0:
            raise IndexError("array is empty.")

        # validates index
        validate_type(index, int)
        if index < 0 or index >= self.length:
            raise IndexError(f"index {index} out of range [0-{self.length - 1}].")

        # returns element
        return self.array[index]

    def set_array(self, elements: list[E]) -> None:
        """
            Sets the array from a list of values.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Args:
                elements: the list of values.

            Raises:
                TypeError: if elements is not of type 'list'.
        """

        # validates type of elements
        validate_type(elements, list)

        # increases size of array
        while (self.size < len(elements)):
            self.size *= 2
        self.array = StaticArray(self.size)

        # copies elements and sets length
        for i in range(len(elements)):
            self.array[i] = (elements[i])
        self.length = len(elements)

    def append(self, element: E) -> None:
        """
            Appends an element at the end of the array.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(1)
                Best Case: O(1)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(1)
                Best Case: O(1)

            Args:
                element (E): the element to append.
        """

        # checks if there is space in the array
        if self.length >= self.size:
            self.grow()

        # adds the element to the end of the array and increments length
        self.array[self.length] = element
        self.length += 1

    def insert(self, index: int, element: E) -> None:
        """
            Inserts an element at a specific index.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(1)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(1)
                Best Case: O(1)

            Args:
                index (int): the index to insert the element at.
                element (E): the element to insert.

            Raises:
                TypeError: if index is not of type 'int'.
                IndexError: if index is out of range.
        """

        # validates index
        validate_type(index, int)        
        if index < 0 or index > self.length:
            raise IndexError(f"index {index} out of range [0-{self.length}].")

        # checks if there is space in the array
        if self.length >= self.size:
            self.grow()

        # shifts elements
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]

        # adds the element and increments length
        self.array[index] = element
        self.length += 1

    def pop(self) -> E:
        """
            Pops and returns the last element.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(1)
                Best Case: O(1)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(1)
                Best Case: O(1)

            Returns:
                E: the last element.
        """

        # checks if array is empty
        if self.length == 0:
            raise IndexError("array is empty.")

        # gets the last element then deletes it
        element = self.array[self.length - 1]
        self.array[self.length - 1] = None
        self.length -= 1

        # checks if the array can shrink
        if self.length <= self.size // 2 and self.size != 1:
            self.shrink()

        # returns element
        return element

    def extract(self, index: int) -> E:
        """
            Extracts and returns an element from a specific index.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(1)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(1)
                Best Case: O(1)

            Args:
                index (int): the index to extract the element from.

            Returns:
                E: the element at the index.

            Raises:
                TypeError: if index is not of type 'int'.
                IndexError: if index is out of range.
        """

        # checks if array is empty
        if self.length == 0:
            raise IndexError("array is empty.")

        # validates index
        validate_type(index, int)        
        if index < 0 or index >= self.length:
            raise IndexError(f"index {index} out of range [0-{self.length-1}].")

        # gets the element at the index then deletes it
        element = self.array[index]
        self.array[index] = None

        # shifts elements
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i+1]
        self.array[self.length - 1] = None

        # decrements the length of the array
        self.length -= 1

        # checks if the array can shrink
        if self.length <= self.size // 2 and self.size != 1:
            self.shrink()

        # returns element
        return element

    def grow(self) -> None:
        """
            Doubles the size of the array.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)
        """

        # initialises a new array that is double the size
        new_array = StaticArray(self.size * 2)

        # copies the previous element to the new array
        for i in range(self.size):
            new_array[i] = self.array[i]

        # sets the new array and size
        self.array = new_array
        self.size *= 2

    def shrink(self) -> None:
        """
            Halves the size of the array.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)
        """

        # halves the size
        self.size //= 2

        # initialises a new array that is half the size
        new_array = StaticArray(self.size)

        # copies the previous element to the new array
        for i in range(self.size):
            new_array[i] = self.array[i]

        # sets the new array and size
        self.array = new_array

    def __len__(self) -> int:
        """
            Returns the length of the array.

            Time Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)

            Space Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)

            Returns:
                int: the size of the array.
        """

        return self.length

    def __repr__(self) -> str:
        """
            Returns a detailed string representation of the object.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Returns:
                str: the string representation of the object.
        """

        return f"{{ length: {self.length}, size: {self.size}, array: {str(self.array)} }}"

    def __str__(self) -> str:
        """
            Returns a simple string representation of the object.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Returns:
                str: the string representation of the object.
        """

        elements = [str(self.array[i]) for i in range(self.length)]
        return f"[{", ".join(elements)}]"
