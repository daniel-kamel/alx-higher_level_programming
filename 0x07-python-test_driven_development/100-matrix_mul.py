#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matricies
"""


def matrix_mul(m_a, m_b):
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
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    ma_row, mb_row = len(m_a), len(m_b)

    if ma_row == 0:
        raise ValueError("m_a can't be empty")
    elif mb_row == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        elif len(row) == 0:
            raise ValueError("m_a can't be empty")
        for elem in row:
            if not isinstance(elem, int):
                raise TypeError('m_a should contain only integers or floats')
            elif isinstance(elem, float):
                raise TypeError('m_a should contain only integers or floats')

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        elif len(row) == 0:
            raise ValueError("m_b can't be empty")
        for elem in row:
            if not isinstance(elem, int):
                raise TypeError('m_b should contain only integers or floats')
            elif isinstance(elem, float):
                raise TypeError('m_b should contain only integers or floats')

    ma_col, mb_col = len(m_a[0]), len(m_b[0])

    if ma_col != mb_row:
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a*b for a, b in zip(ma_row, mb_col))
             for mb_col in zip(*m_b)] for ma_row in m_a]


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/100-matrix_mul.txt')
