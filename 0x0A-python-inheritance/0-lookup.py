#!/usr/bin/python3
""" Module for the lookup method """


def lookup(obj):
    """
    Gets the list of available attributes and methods
    of an object.

    Args:
        obj: The object to list.

    Returns:
        list: List of attributes and methods of an object.
    """
    return dir(obj)
