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
        """Returns True if no cells are alive"""
        for x in range(self.width):
            for y in range(self.height):
                if(self.state[x][y]):
                    return False
        return True

    def get(self):
        """Returns current state of play as 2d list"""
        return self.state

    def print(self):
        """Prints the current state of play to the console"""
        for y in range(self.height):
            # I'm likely printing this rotated 90 degrees...
            print(self.state[y])

    def set_cell(self, x, y, is_alive):
        """Sets the given x and y position on the board to be alive or dead"""
        self.state[x][y] = is_alive
    
    def get_cell(self, x, y):
        """Gets the current state of a cell at the given x and y position"""
        return self.state[x][y]

    def get_num_neighbors(self, cell_x, cell_y):
        """Get the number of live neighbors given an x and y position"""
        num_neighbors = 0
        for neigh_x in range(cell_x-1, cell_x+2):
            for neigh_y in range(cell_y-1, cell_y+2):
                # Don't count itself
                if((cell_x == neigh_x) and (cell_y == neigh_y)):
                    continue
                # Don't count cells outside of width of board
                if((neigh_x < 0) or (neigh_x > self.width-1)):
                    continue
                # Don't count cells outside of height of board
                if((neigh_y < 0) or (neigh_y > self.height-1)):
                    continue
                # If neighboring cell is alive, increment
                if(self.state[neigh_x][neigh_y]):
                    num_neighbors += 1
        return num_neighbors
    
    def iterate(self):
        """Run one round of the Game of Life"""
        new_state = [[False for x in range(self.width)] for y in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                num_neighbors = self.get_num_neighbors(x,y)
                # Cell starves
                if(num_neighbors < 2):
                    new_state[x][y] = False
                # Cell stays the same
                if(num_neighbors == 2):
                    new_state[x][y] = self.get_cell(x,y)
                # Cell survives or comes alive
                if(num_neighbors == 3):
                    new_state[x][y] = True
                # Cell is overcrowded
                if(num_neighbors > 3):
                    new_state[x][y] = False
        self.state = new_state
