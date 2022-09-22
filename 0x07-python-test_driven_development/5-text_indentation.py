#!/usr/bin/python3

""" Module contains fuction that prints an
    indented text to stdout based on some
    special characters
"""


def text_indentation(text):
    """ Prints indented text based on '.'
        '?' and ':'.
        Takes a str arg text as parameter
        only, otherwise raises an error
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        if char in ['.', '?', ':']:
            print(char)
            print("" * 2)
        else:
            print(char, end="")
    print()
