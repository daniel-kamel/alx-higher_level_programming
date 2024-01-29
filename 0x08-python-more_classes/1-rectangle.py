#!/usr/bin/python3
"""
This module contains the definition of a Rectangle class
"""


class Rectangle():
    """
    This class defines an empty Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes instances or Rectangle class
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Gets the width property
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width property
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

    @property
    def height(self):
        """
        Gets the height property
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height property
        """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height
