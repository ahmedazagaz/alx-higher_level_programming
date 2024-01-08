#!/usr/bin/python3
""" Module for the lookup method. """


def lookup(obj):
    """
    Gets the list of available attributes and methods
    of an object.

    Args:
        obj (object): The object to list.

    Returns:
        list: List of attributes.
    """
    return dir(obj)
