#!/usr/bin/python3
"""
Square module doc
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class doc
    """
    def __init__(self, size):
        """
        Initializes Square object
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        returns the area of the Square
        """
        return self.__size ** 2
