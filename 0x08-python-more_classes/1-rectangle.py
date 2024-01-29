#!/usr/bin/python3
"""
This module contains the definition of a Rectangle class
"""


class Rectangle:
    """
    This class defines an empty Rectangle

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes instances or Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Gets the width property

        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width property

        Args:
            width (int): width of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        """
        Gets the height property

        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height property

        Args:
            height (int): height of the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height
