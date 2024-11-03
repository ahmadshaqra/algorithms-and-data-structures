"""
    Static Array

    A fixed-sized array with efficient index-based access.

    Author: Ahmad Abu-Shaqra
"""

from other.utils import validate_type, validate_int
from typing import Generic, TypeVar

E = TypeVar('E')

class StaticArray(Generic[E]):
    """
        Attributes:
            size: the size of the array.
            array: the array container.
    """

    def __init__(self, size: int) -> None:
        """
            Initialises static array.

            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Space Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)
            
            Args:
                size (int): the size of the static array.

            Raises:
                TypeError: if size is not of type 'int'.
                ValueError: if size is less than 0.
        """

        # validates size
        if not validate_int(size, min_value=0):
            raise ValueError("size must be greater than or equal to 0.")

        # initialises array
        self.size = size
        self.array = [None] * size

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

        # validates index
        if self.size == 0:
            raise IndexError(f"index {index} out of range, array size is 0.")
        if not validate_int(index, min_value=0, max_value=self.size-1):
            raise IndexError(f"index {index} out of range [0-{self.size-1}].")

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

        # validates index
        if self.size == 0:
            raise IndexError(f"index {index} out of range, array size is 0.")
        if not validate_int(index, min_value=0, max_value=self.size-1):
            raise IndexError(f"index {index} out of range [0-{self.size-1}].")
        
        # returns element
        return self.array[index]

    def __len__(self) -> int:
        """
            Returns the size of the array.

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

        return self.size

    def set_array(self, elements: list[E]) -> None:
        """
            Sets the array from a list of values.
        
            Time Complexity:
                Worst Case: O(n)
                Average Case: O(n)
                Best Case: O(n)

            Space Complexity:
                Worst Case: O(1)
                Average Case: O(1)
                Best Case: O(1)

            Args:
                elements: the list of values.

            Raises:
                TypeError: if array is not of type 'list'.
                ValueError: if array is not of the correct size.
        """

        # validates type of elements
        validate_type(elements, list)

        # validates length of elements
        if len(elements) != self.size:
            raise ValueError(f"expected list of size {self.size}, but got list of size {len(elements)} instead.")
        
        # copies elements
        for i in range(len(elements)):
            self.array[i] = elements[i]

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

        return f"{{ size: {self.size}, array: {str(self.array)} }}"

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

        return str(self.array)
