#!/usr/bin/python3
""" Module for the lookup method """


def lookup(obj):
    """
    Gets the list of available attributes and methods
    of an object.

    Args:
        obj (object): the object to list.

    Returns:
        list: the List of attributes.
    """
    return dir(obj)
