#!/usr/bin/python3

""" Module contains a function say_my_name
    Function take two parameters (first_name & last_name),
    and returns the a greeting message.
    Both parameters must be a string.
"""

def say_my_name(first_name, last_name=""):
    """ Returns the greeting message as a string with
        both parameters of the same data type as well
        Raises a type error if the parameters are not
        strings.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    message = "My name is " + first_name + last_name

    return message
