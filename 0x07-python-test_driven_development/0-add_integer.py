#!/usr/bin/python3

def add_integer(a, b=98):
    """ Returns the sum of two integers """

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
