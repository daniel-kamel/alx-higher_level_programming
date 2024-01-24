#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
   Class that defines properties of square by: (based on 0-square.py)

    Attributes:
        size: size of a square (1 side)
        position: position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Creates new instances of square.

        Args:
            __size (int): size of the square (1 side)
            __position (tuple): position of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of square

        Returns:
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
    def size(self, value):
        """
        Setter method for the size field

        Args:
            size: size of the sqaure

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position field

        Return:
            position of the square instance
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position field

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        prints a square to stdout
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
