#!/usr/bin/python3
"""square class"""
from models.Rectangle import Rectangle


class Square(Rectangle):
    """square inherites from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """make init 7aga gamda"""
        super().__init__(size, size,x, y,id)


    def __str__(self):
        """Return the print() of square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Get width"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value
