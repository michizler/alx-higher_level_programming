#!/usr/bin/python3

"""
    module to return the JSON representation
    of an object(string).
"""


def to_json_string(my_obj):
    """
        Returns the appropriate JSON
        representation of the object.
    """

    import json

    return json.dumps(my_obj)
