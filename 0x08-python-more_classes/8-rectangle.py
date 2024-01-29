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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes instances or Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width property

        Returns:
            int: The width of the rectangle
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
            int: The height of the rectangle
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

    def area(self):
        """
        Computes the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle

        Returns:
            int: the perimeter of the rectangle or 0 if either the
            width or the height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Prints the rectangle with the character # .

        Returns:
            str: the rectangle
        """
        rect = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(str(self.print_symbol))
            rect.append("\n")

        rect.pop()

        return "".join(rect)

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Recognizes the deletion of an instance
        """
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Determines which rectangle has bigger area

        Args:
            rect_1 (Rectangle): rectangle object 1
            rect_2 (Rectangle): rectangle object 2

        Returns:
            Rectangle: the rectangle with bigger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
