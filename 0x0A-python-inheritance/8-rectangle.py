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
