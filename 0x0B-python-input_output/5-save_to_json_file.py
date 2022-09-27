#!/usr/bin/python3

"""
    Module to write python objects to textfile
"""


def save_to_json_file(my_obj, filename):
    """ Converts python object to its JSON
        representation and wirtes it to the
        textfile.
    """

    import json

    with open(filename, "w", encoding="utf-8") as tf:
        tf.write(json.dumps(my_obj))
