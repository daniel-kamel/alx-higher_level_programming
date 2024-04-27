#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    length = len(list_of_integers)
    mid = int(length // 2)

    if length == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    if length == 1:
        return list_of_integers[0]

    if sum(list_of_integers[:mid + 1]) < sum(list_of_integers[mid + 1:]):
        return find_peak(list_of_integers[mid + 1:])
    else:
        return find_peak(list_of_integers[:mid + 1])
