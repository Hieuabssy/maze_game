import pygame

class cell():

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col
        self.y = row
        self.walls = {'top': True, 'bot': True, 'right': True, 'left': True}
        self.is_visited = False
        self.is_entry_exit = None
        self.thickness = 1

    def draw(self, screen, cell_size):
        """ This function use to draw wall if it appear """
        x, y = self.x * cell_size, self.y * cell_size 
        # wall_ver = pygame.image.load('Do_an/Assets/Wall/wall_vertical.png')
        # wall_ver = pygame.transform.scale(wall_ver, (cell_size, 3 + cell_size//20))
        # wall_hor = pygame.image.load('Do_an/Assets/Wall/wall_horizontal.png')
        # wall_hor = pygame.transform.scale(wall_hor, (3 + cell_size//20, cell_size))
        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color('black'), (x, y), (x + cell_size, y), self.thickness + cell_size//20)
            # screen.blit(wall_ver, (x, y))
        if self.walls['right']:
            pygame.draw.line(screen, pygame.Color('black'), (x + cell_size, y), (x + cell_size, y + cell_size), self.thickness + cell_size//20)
            # screen.blit(wall_hor, (x + cell_size, y))
        if self.walls['bot']:
            pygame.draw.line(screen, pygame.Color('black'), (x + cell_size, y + cell_size), (x , y + cell_size), self.thickness + cell_size//20)
            # screen.blit(wall_ver, (x, y + cell_size))
        if self.walls['left']:
            pygame.draw.line(screen, pygame.Color('black'), (x, y + cell_size), (x, y), self.thickness + cell_size//20)
            # screen.blit(wall_hor, (x, y))
    
    def remove_walls(self, neighbour_row, neighbour_col):
        """
        Function that removes walls between neighbour cell given by indices in grid.

            Args:
                neighbour_row (int):
                neighbour_col (int):

            Return:
                True: If the operation was a success
                False: If the operation failed
                
        """

        if self.row - neighbour_row == 1:
            self.walls["top"] = False
            return True
        elif self.row - neighbour_row == -1:
            self.walls["bot"] = False
            return True
        elif self.col - neighbour_col == 1:
            self.walls["left"] = False
            return True
        elif self.col - neighbour_col == -1:
            self.walls["right"] = False
            return True
        
        return False
    
    