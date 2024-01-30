#!/usr/bin/python3
"""
This module contains a function that print a square
"""


def print_square(size):
    """
    This function prints a square.

    Args:
        size (int): length of the squanre

    Raises:
        TypeError: size must be an int
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    print(('#' * size + '\n') * size, end='')


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
