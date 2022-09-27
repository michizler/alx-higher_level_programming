#!/usr/bin/python3

""" module to write text to a
    textfile.
"""


def write_file(filename="", text=""):
    """ Returns the number number of characters
        contained in the text.
    """

    with open(filename, mode="w", encoding="utf-8") as tf:
        tf.write(text)
        return len(text)
