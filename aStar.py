from heapq import *
import pygame
from maze import maze

# Function to calculate Heuristic
def heuristic(i, j, l, r):
    return abs(i - l)**2 + abs(j - r)**2

# Function to solve the maze
def solveAStar(maze, i, j, l, r, solution):

    height = maze.height
    width = maze.width
    # If we've reached the end, we're done
    if i == l and j == r:
        solution.append((i, j))
        return

    # All the possible moves from here
    pos = [(0,1),(0,-1),(1,0),(-1,0)]

    parent = {}             # list to store the parent of each node
    close = set()              # list to store the visited nodes  
    g_score = {(i,j):0}     # dict to store g_score of each node (cost from start to current node)
    h_score = {(i,j):heuristic(i, j, l, r)}     # dict to store h_score of each node (current node to end node)
    heap = []               # list to store the nodes in the heap

    # Add the starting node to the heap
    heappush(heap, (h_score[(i,j)], (i,j)))

    # Loop till the heap is not empty
    while heap :

        # Pop the node with minimum h_score value
        cur = heappop(heap)[1]

        # If we've reached the end, we're done
        if cur == (l, r):
            while cur in parent:
                solution.append(cur)
                cur = parent[cur]
            return

        # Add to close(visited) list 
        close.add(cur)

        # Loop for all the possible moves from the current node
        for i, j in pos:

            # Find the neighbour node
            neighbor = (cur[0] + i, cur[1] + j)

            # Calculate f_score of node 
            f_score = g_score[cur] + heuristic(cur[0], cur[1], neighbor[0], neighbor[1])

            # If position of neighbor is out of maze, skip this node
            if neighbor[0] < 0 or neighbor[0] >= height or neighbor[1] < 0 or neighbor[1] >= width:
                continue

            # If there is a wall in the way, skip this node
            if maze.maze[neighbor[0]][neighbor[1]] == 1:
                continue

            # If the node is already visited or it's f_score is greater than , skip this node
            if neighbor in close and f_score >= g_score.get(neighbor, 0):
                continue

            # If the node is not visited, update the parent and g_score of the node, and push it in heap
            if f_score < g_score.get(neighbor, 0) or neighbor not in [i[1] for i in heap]:
                parent[neighbor] = cur
                g_score[neighbor] = f_score
                h_score[neighbor] = f_score + heuristic(neighbor[0], neighbor[1], l, r)
                heappush(heap, (h_score[neighbor], neighbor))
    return

# Function to visualize the algorithm
def showStar(maze, solution, cell, screen, running):
    red = (255, 0 , 0)
    blue = (0, 0, 255)
    white = (255, 255, 255) 
    solution.reverse()
    start = solution[0]
    end = solution[-1]
    for j,i in solution:
        pygame.draw.circle(screen, blue, (i*cell + cell/2,j*cell + cell/2), cell/2)
        pygame.display.update()
        pygame.time.delay(100)
        if (j,i) == start:
            pygame.time.delay(1000)
        if (j,i) == end:
            running = False
            for x in range(len(solution)-1):
                p1 = solution[x]
                p2 = solution[x+1]
                pygame.draw.line(screen, red, (p1[1]*cell + cell/2, p1[0]*cell + cell/2), (p2[1]*cell + cell/2, p2[0]*cell + cell/2), 2)
            pygame.display.update()
            pygame.time.delay(5000)
            break
        screen.fill(white)
        maze.draw(screen = screen, cell = cell)
        pygame.display.update()
    return running
