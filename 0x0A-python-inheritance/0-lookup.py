#!/usr/bin/python3
""" Module for the lookup method """


def lookup(obj):
    """
    Looks up object attributes and methods.

    Args:
        obj (object): the object to list.

    Returns:
        list: the List of attributes.
    """
    return dir(obj)
