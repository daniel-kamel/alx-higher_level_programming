#!/usr/bin/python3
"""
This module conatains a custom list class
"""


class MyList(list):
    """
    Custom list class
    """
    def print_sorted(self):
        """
        prints a sorted copy of the MyList object
        """
        print(sorted(self))


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/1-my_list.txt')
