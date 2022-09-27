#!/usr/bin/python3

""" Module to read a text file and
    print it to stdout.
"""


def read_file(filename=""):
    """ prints the contents of a read file
        to stdout.
        Encoding is utf-8.
    """
    with open(filename, encoding="utf-8") as tf:
        print(tf.read(), end="")
