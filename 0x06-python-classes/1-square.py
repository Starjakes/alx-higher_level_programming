#!/usr/bin/python3
"""square class definition"""


class Square:
    """represent a square
    Attributes:
        __size (int): size of the side of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the Square
        Returns: None
        """
        self.__size = size
