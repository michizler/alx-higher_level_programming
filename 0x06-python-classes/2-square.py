#!/usr/bin/pyhton3

""" Square class to represent a square """


class Square:
    """ class initialization

        Args:
        size(int): size of the square

    """

    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
