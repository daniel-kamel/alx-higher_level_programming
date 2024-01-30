#!/usr/bin/python3
"""
This module contains a function that prints a text with
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after each of these characters: ., ? and :.

    Args:
        text (str): text to be split and printed

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for delim in '.?:':
        text = (delim + '\n\n').join(
            [line.strip(' ') for line in text.split(delim)])

    print(text, end='')


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
