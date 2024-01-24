#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """
        Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the current square

        Return:
            The area of the square insatnce
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method for the size field

        Return:
            size of the square instance
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter method for the size field

        Args:
            size: size of the sqaure

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """
        prints a square to stdout
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print('')
