#!/usr/bin/python3
"""This is a function that read text file and print to stdput"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
    