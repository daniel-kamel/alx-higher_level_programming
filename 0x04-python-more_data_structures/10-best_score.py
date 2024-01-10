#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    highest = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == highest:
            return key
