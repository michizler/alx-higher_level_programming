#!/usr/bin/python3

"""
    module to return a python object
    from the JSON representation.
"""


def from_json_string(my_str):
    """
        Returns the appropriate python object
        from the JSON representation.
    """

    import json

    return json.loads(my_str)
