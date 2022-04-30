from array import *


class Board:
    """The game board class"""

    def __init__(self, width=10, height=10):
        """Creates empty game board given width and height"""
        self.width = width
        self.height = height
        self.state = [[False for x in range(width)] for y in range(height)]

    def is_empty(self):
        return True

    def get_board(self):
        return self.state