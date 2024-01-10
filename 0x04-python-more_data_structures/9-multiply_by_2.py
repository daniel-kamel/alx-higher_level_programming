#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {x: x * 2 for x in a_dictionary.values()}
    return new_dict
