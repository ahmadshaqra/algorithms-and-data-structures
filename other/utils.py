"""
    Utils

    A module of utility functions.

    Author: Ahmad Abu-Shaqra
"""

from typing import TypeVar

T = TypeVar('T')

def validate_type(value: T, expected_type: type) -> None:
    """
        Validates a value's type.

        Time Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Space Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Args:
            value (T): the value to be validated.
            expected_type (type): the expected type of value.

        Raises:
            TypeError: if value is not the correct type.
    """

    if not isinstance(value, expected_type):
        raise TypeError(f"expected '{expected_type.__name__}' but got '{type(value).__name__}' instead.")
