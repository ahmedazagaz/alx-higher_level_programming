#!/usr/bin/python3
"""
Module for add_integer method.
"""


def add_integer(a, b=98):
    """ Adds two integers.

    Args:
        a: first integer
        b: second integer , default 98.
    
    Raises:
        TypeError: if a,b are not int or float

    Return:
        the sum of the two integers.
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
