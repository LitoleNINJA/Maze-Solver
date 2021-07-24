from pygame.locals import *
import pygame
from maze import maze
from Treamaux import solveDFS, showDFS
from wall_follower import solveWallLeft, solveWallRight, showWall
import sys
sys.setrecursionlimit(200)


red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


if __name__ == '__main__':
    running = True
    pygame.init()
    maze = maze()
    solution = []
    vis = []
    for i in range(0,maze.height+1):
        vis.append([0]*(maze.width+1))
    flag = False
    face = 'D'
    # solveDFS(maze, 0, 1, 10, 19, vis, solution, flag)
    solveWallRight(maze, 0, 1, 10, 19, face, vis, solution, flag)
    # solveWallLeft(maze, 0, 1, 10, 19, face, vis, solution, flag)
    while running:
        # screen = pygame.display.set_mode((840,500))
        # screen.fill(white)
        # maze.draw(display_surf=screen)
        screen = pygame.display.set_mode((840,500))
        screen.fill(white)
        maze.draw(display_surf=screen)
        pygame.display.set_caption('Maze Solver')
        pygame.display.update()
        # running = showDFS(solution, screen, running)
        running = showWall(solution, screen, running)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False