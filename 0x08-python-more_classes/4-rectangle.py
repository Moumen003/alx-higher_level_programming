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

    def area(self):
        """aywa ya area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """aywa ya perimiter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2*self.__width + 2*self.__height)

    def __str__(self):
        """i love alx"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []

        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)
