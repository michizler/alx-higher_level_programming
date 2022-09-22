#!/usr/bin/python3

""" module holding function for the summation of
    two integers.
    The parameters can be a float or an integer.
    Regardless, the return value of the function is
    always an integer."""


def add_integer(a, b=98):
    """ Returns the sum of two integers
        a(int): first parameter
        b(int/float): second parameter (default value = 98)"""

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
