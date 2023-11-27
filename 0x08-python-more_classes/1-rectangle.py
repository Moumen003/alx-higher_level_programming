#!/usr/bin/python3
"""Defiargnes a Rectangle class."""


class Rectangle:
    """Representdzfg a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The wadfgrectangle.
            height (int): The heigadfght of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/seafgdff the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must zdfbbe an integer")
        if value < 0:
            raise ValueError("widtsdh must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height maergdust be an integer")
        if value < 0:
            raise ValueError("height madfust be >= 0")
        self.__height = value
