#!/usr/bin/python3
"""aywa ba2a el addition"""


def add_integer(a, b=98):
    """yaba el kkalam da eh

    Raises:
        TypeError law mesh sa7
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
