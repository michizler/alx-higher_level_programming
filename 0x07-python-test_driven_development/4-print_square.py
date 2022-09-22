#!/usr/bin/python3

""" Module is a function print_sqaure which
    takes a size argument --- length of the
    square.

    The size argument must meet certain conditions
    as seen in the function doc.
"""


def print_square(size):
    """ prints the square size with the character '#'
        
        The size argument must have the properties of
        normal arithmetic measurements.

        size must be an integer and must be >= 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if size == 0:
        return

    for i in range(size):
        print("#" * size)
