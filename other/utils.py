"""
    Utils

    A module of utility functions.

    Author: Ahmad Abu-Shaqra
    Last Modified: 01/11/24
"""

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
    validate_int_type(value)
    
    # validates types of min_value and max_value
    if min_value is not None:
        validate_int_type(min_value)
    if max_value is not None:
        validate_int_type(max_value)

    # validates bounds
    if min_value is not None and value < min_value:
        return False
    if max_value is not None and value > max_value:
        return False
    
    # integer is validated
    return True

def validate_int_type(value: int) -> None:
    """
        Validates an integer's type.

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

        Raises:
            TypeError: if value is not of type 'int'.
    """

    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"expected 'int' but got '{type(value).__name__}' instead.")
