import random
from cell import cell
from algrithms import *

class maze():
    def __init__(self, num_rows, num_cols):
        """
        num_rows is the number of row of maze and num_cols is the number of col of maze
        auto_set_trence = True if player don't choose entry, exit and = False if player choose paticular entry, exit

        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid_size = num_rows * num_cols
        self.grid = self.generate_grid()
        self.start = self.pick_random_entry_exit()
        self.end = self.pick_random_entry_exit(self.start)

    def generate_grid(self):
        """
        Function that creates a 2D grid of Cell objects. This can be thought 
        of as a maze without any paths carved out

        Return:
            A list with Cell objects at each position

        """
        # Create an empty list
        grid = []

        # Place a Cell object at each location in the grid
        for i in range(self.num_rows):
            grid.append(list())

            for j in range(self.num_cols):
                grid[i].append(cell(i, j))

        return grid

    def find_neighbours(self, cell_row, cell_col):
        """Finds all existing and unvisited neighbours of a cell in the grid.
        Return a list of tuples containing indices for the unvisited neighbours.

        Args:
            cell_row (int):
            cell_col (int):

        Return:
            None: If there are no unvisited neighbors
            list: A list of neighbors that have not been visited
        """
        neighbours = []

        def check_neighbour(row, col):
            # Check that a neighbour exists and that it's not visited before.
            if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
                neighbours.append((row, col))

        check_neighbour(cell_row-1, cell_col)     # Top neighbour
        check_neighbour(cell_row, cell_col+1)     # Right neighbour
        check_neighbour(cell_row+1, cell_col)     # Bottom neighbour
        check_neighbour(cell_row, cell_col-1)     # Left neighbour

        if len(neighbours) > 0:
            return neighbours
        else:
            return None     # None if no unvisited neighbours found
        
    def validate_neighbours_generate(self, neighbour_indices):
        """
        Function that validates whether a neighbour is unvisited or not.

        Args:
            neighbour_indices:

        Return:
            True: If the neighbor has been visited
            False: If the neighbor has not been visited

        """
        neigh_list = []
        for x, y in neighbour_indices:
            if not self.grid[x][y].is_visited:
                neigh_list.append((x, y))

        if len(neigh_list) > 0:
            return neigh_list
        else:
            return None   
        
    def pick_random_entry_exit(self, start=None):
        """
        Function that picks random coordinates along the maze boundary to represent either
        the entry or exit point of the maze. Makes sure they are not at the same place.

        Args:
            start

        Return:

        """
        entry = start    # Initialize with used value

        if start is None:
            while entry == start:
                rand_side = random.randint(0, 3)
                if (rand_side == 0):     # Top side
                    entry = (0, random.randint(0, self.num_cols-1))
                elif (rand_side == 2):   # Bottom side
                    entry = (self.num_rows-1, random.randint(0, self.num_cols-1))
                elif (rand_side == 1):   # Right side
                    entry = (random.randint(0, self.num_rows-1), self.num_cols-1)
                elif (rand_side == 3):   # Left side
                    entry = (random.randint(0, self.num_rows-1), 0)

        else:
            if start[0] == 0:
                entry = (self.num_rows-1, random.randint(0, self.num_cols-1))
            elif start[0] == self.num_rows-1:
                entry = (0, random.randint(0, self.num_cols-1))
            elif start[1] == 0:
                entry = (random.randint(0, self.num_rows-1), self.num_cols-1)
            else:
                entry = (random.randint(0, self.num_rows-1), 0)

        return entry       # Return entry/exit that is different from exit/entry

    def set_entry_exit(self, start, end):
        """ This function use to set entry and exit which is entered by user """
        self.start = start
        self.end = end

    def generate_maze(self):
        self = depth_first_recursive_backtracker(self, self.start)

    def solve_maze(self, algorithm):
        if algorithm == 'bfs': return bfs(self)
        elif algorithm == 'dfs': return dfs(self)
        else: return None
