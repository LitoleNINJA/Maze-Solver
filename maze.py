import pygame

class maze():

    # Height and Width of maze
    height = 11
    width = 21

    # Maze in the form of matrix of 0's and 1's
    maze = [[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
            [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1],
            [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
            [1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1],
            [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]]
    
    # Function to draw the maze
    def draw(self, display_surf):

        # Color of walls
        black = (0,0,0)

        # For each cell in maze, add a wall if it's a '1'
        for i in range(0,self.width):
            for j in range(0,self.height):
                if self.maze[j][i] == 1:
                    pygame.draw.rect(display_surf, black, (i*40,j*40,40,40))