#!/usr/bin/python3
"""
my_int module doc
"""


class MyInt(int):
    """
    MyInt class doc
    """
    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
