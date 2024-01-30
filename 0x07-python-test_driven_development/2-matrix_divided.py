#!/usr/bin/python3
"""
This module contains a function that divides a matrix by
a number.
"""


def matrix_divided(matrix, div):
    """
    Divides a matrix (list of lists) by a number.

    Args:
        matrix (list): matrix to be divided
        div (int or float): number to divide the matrix by

    Returns:
        New matrix where each element is divided by div and rounded to
        2 decimal places

    Raises:
        TypeError: matrix must be a list of lists of integers/floats
                    and each row of the matrix should be of equal size.
        ZeroDivisionError: div cannot be 0

    """
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists)'
                            ' of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists)'
                                ' of integers/floats')

    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
