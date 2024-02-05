#!/usr/bin/python3
"""
4-inherits_from.py module doc
"""


def inherits_from(obj, a_class):
    """
    returns if the objects is an instance of the specified class
    or a class that inherits from the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
