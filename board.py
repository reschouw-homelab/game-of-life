from array import *
from unittest import case

class board:
    """The game board class"""

    def __init__(self, width=10, height=10):
        """Creates empty game board given width and height"""
        self.width = width
        self.height = height
        self.state = [[False for x in range(width)] for y in range(height)]

    def is_empty(self):
        for x in range(self.width):
            for y in range(self.height):
                if(self.state[x][y]):
                    return False
        return True

    def get(self):
        return self.state

    def print(self):
        for y in range(self.height):
            # I'm likely printing this rotated 90 degrees...
            print(self.state[y])

    def set_cell(self, x, y, is_alive):
        self.state[x][y] = is_alive
    
    def get_cell(self, x, y):
        return self.state[x][y]

    def get_num_neighbors(self, x, y):
        num_neighbors = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                # Don't count itself
                if((x == i) and (y == j)):
                    continue
                # Don't count cells outside of width of board
                if((i < 0) or (i > self.width-1)):
                    continue
                # Don't count cells outside of height of board
                if((j < 0) or (j > self.height-1)):
                    continue
                # If neighboring cell is alive, increment
                if(self.state[i][j]):
                    num_neighbors += 1
        return num_neighbors
    
    def iterate(self):
        new_state = [[False for x in range(self.width)] for y in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                # This needs to be a case, but I don't have internet to look that up right now
                num_neighbors = self.get_num_neighbors(x,y)
                if(num_neighbors < 2):
                    new_state[x][y] = False
                if(num_neighbors == 2):
                    new_state[x][y] = self.get_cell(x,y)
                if(num_neighbors == 3):
                    new_state[x][y] = True
                if(num_neighbors > 3):
                    new_state[x][y] = False
