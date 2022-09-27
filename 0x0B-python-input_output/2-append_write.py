#!/usr/bin/python3

""" module to append text to a
    textfile.
"""


def append_write(filename="", text=""):
    """ Returns the number of characters
        contained in the text.
    """

    with open(filename, mode="a", encoding="utf-8") as tf:
        tf.write(text)
        return len(text)
