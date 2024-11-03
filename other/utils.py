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

def validate_int(value: int, *, min_value: int | None = None, max_value: int | None = None) -> bool:
    """
        Validates an integer with optional lower and upper bounds.

        Time Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Space Complexity:
            Worst Case: O(1)
            Average Case: O(1)
            Best Case: O(1)

        Args:
            value (int): the value to be validated.
            min_value (int): the lower bound value.
            max_value (int): the upper bound value.

        Returns:
            bool: true if integer is valid, false otherwise.

        Raises:
            TypeError: if value, min_value, or max_value are not 'int'.
    """

    # validates type of value
    validate_type(value, int)

    # validates types of min_value and max_value
    if min_value is not None:
        validate_type(min_value, int)
    if max_value is not None:
        validate_type(max_value, int)

    # validates bounds
    if min_value is not None and value < min_value:
        return False
    if max_value is not None and value > max_value:
        return False

    # integer is validated
    return True
