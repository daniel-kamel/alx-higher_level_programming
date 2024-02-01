#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matricies
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matricies.

    Args:
        m_a (list of lists of ints/floats): matrix a
        m_b (list of lists of ints/floats): matrix b

    Returns:
        (list of lists of ints/floats): product of the
        multiplication of m_a and m_b

    Raises:
        TypeError: m_a and m_b must be list of lists of
        integers/floats. All rows of
                each matrix must be same size.
        ValueError: m_a and m_b can't be empty and the
        number of columns of m_a must be equal to the
        number of rows in m_b.
    """
    return np.dot(m_a, m_b).tolist()


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/101-lazy_matrix_mul.txt')
