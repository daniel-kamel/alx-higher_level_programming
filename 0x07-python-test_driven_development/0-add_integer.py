#!/usr/bin/python3
"""
This module contains a function that adds 2 numbers

"""


def add_integer(a, b=98):
    """
    Adds 2 numbers.

    Args:
        a (int or float): first number
        b (int or float): second number (default = 98)

    Returns:
        int: The sum of a and b

    Raises:
        TypeError: a and b must be either int or float
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return int(a + b)
