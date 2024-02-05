#!/usr/bin/python3
"""
Returns all available attributes for an opject
"""


def lookup(obj):
    """
    Returns all available attributes for an opject
    """
    return dir(obj)
