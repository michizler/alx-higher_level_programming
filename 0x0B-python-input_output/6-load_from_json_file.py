#!/usr/bin/python3

"""
    Module to create python objects from a textfile
"""


import json


def load_from_json_file(filename):
    """ Converts JSON representation to
        the python objects from a textfile.
    """

    with open(filename, "r", encoding="utf-8") as tf:
        return json.loads(tf.read())
