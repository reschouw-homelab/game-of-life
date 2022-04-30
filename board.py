from array import *

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
                if((x == i) and (y == j)):
                    continue
                if((x<0) or (x>self.width-1)):
                    continue
                if((y<0) or (y>self.height-1)):
                    continue
                if(self.state[i][j]):
                    num_neighbors += 1
        return num_neighbors