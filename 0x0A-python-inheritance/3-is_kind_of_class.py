#!/usr/bin/python3
"""
3-is_kind_of_class module doc
"""


def is_kind_of_class(obj, a_class):
    """
    returns if the objects is an instance of the specified class
    or a class that inherits from the specified class
    """
    return isinstance(obj, a_class)
