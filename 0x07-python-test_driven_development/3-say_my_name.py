#!/usr/bin/python3
"""
This module contains a function that prints
My name is <first_name> <last_name>
"""


def say_my_name(first_name, last_name=''):
    """
    This function prints My name is <first_name> <last_name>.

    Args:
        first_name (string): first name
        last_name (string): last_name

    Raises:
        TypeError: first_name and last_name must be strings
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
