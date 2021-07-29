from pygame.locals import *
import pygame
from maze import maze
from Treamaux import *
from wall_follower import *
from aStar import *
from img_to_bin import *
import sys
sys.setrecursionlimit(10000)


white = (255, 255, 255)
black = (0, 0, 0)
green = (0,255,0)



if __name__ == '__main__':
    running = True
    pygame.init()

    # Solution array to store the solution path
    solution = []
    
    # Initial value of flag and face
    flag = False
    face = 'D'

    # If maze in in form of jpg / png, covert it into array using opencv
    path = "maze20.png"
    m, height, width = img_to_bin(path)

    maze = maze()
    maze.maze = m
    maze.height = height
    maze.width = width
    cell_h, cell_w = 10, 10

    # Visited array to store the visited nodes
    vis = []
    for i in range(0, height+1):
        vis.append([0]*( width+1))


    screen = pygame.display.set_mode((height*cell_h, width*cell_w))
    pygame.display.set_caption('Maze Solver')
    screen.fill(white)
    maze.draw(screen = screen, cell = cell_h)
    pygame.display.update()

    # Set start and end points
    start = (1, 1)
    end = (height-2, width-2)
    print(maze.maze)

    # Choose which algorithm to use

    solveDFS(maze, start[0], start[1], end[0], end[1], vis, solution, flag)
    # solveWallRight(maze, 0, 1, 10, 19, face, vis, solution, flag)
    # solveWallLeft(maze, 1, 1, 199, 199, face, vis, solution, flag)
    # solveAStar(maze, 1, 1, 39, 39, solution)
    # print(solution)

    while running:
        
        # maze.draw(display_surf=screen)
        # running = showDFS(solution, cell_h, screen, running)
        # running = showWall(solution, screen, cell_w, running)
        # running = showStar(maze, solution, cell_h, screen, running)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
