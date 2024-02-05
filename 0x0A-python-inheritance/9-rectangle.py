#!/usr/bin/python3
"""
rectangle module doc
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class doc
    """
    def __init__(self, width, height):
        """
        Initializes Rectangle object
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
