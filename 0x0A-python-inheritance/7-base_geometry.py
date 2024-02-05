#!/usr/bin/python3
"""
base_geometry module doc
"""


class BaseGeometry:
    """
    BaseGeometry class doc
    """
    def area(self):
        """
        area method doc
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        integer_validator method doc
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
