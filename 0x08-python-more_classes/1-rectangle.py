#!/usr/bin/python3
""" recatangle class"""


class Rectangle:
    """rectangle ya bsaha"""

    def __init__(self, width=0, height=0):
        """new rec intialized.

        Args:
            width (int): ba asdfs
            height (int): we malo

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ay ba2a ya fn"""
        return self.__width

    @property
    def height(self):
        """we malo ya gameel"""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
