import pygame

#TREMAUX ALGORITM
def solveDFS(maze, i, j, l, r, vis, solutionDFS, flag):

    # If we've reached the end, we're done
    if i == l and j == r :
        solutionDFS.append((i,j))
        flag = True
        return;

    # If end has been reached, don't add anything to solution
    if not flag:
        solutionDFS.append((i,j))

    # Mark the current cell as visited
    vis[i][j] = 1

    # Recursively solve the maze if we haven't reached the end
    # If down in open and not visited, move down
    if i<maze.height-1 and maze.maze[i+1][j] == 0 and vis[i+1][j] == 0:
        solveDFS(maze, i+1, j, l, r, vis, solutionDFS, flag)

    # If right in open and not visited, move right
    if j<maze.width-1 and maze.maze[i][j+1] == 0 and vis[i][j+1] == 0:
        solveDFS(maze, i, j+1, l, r, vis, solutionDFS, flag)

    # If up in open and not visited, move up
    if i>0 and maze.maze[i-1][j] == 0 and vis[i-1][j] == 0:
        solveDFS(maze, i-1, j, l, r, vis, solutionDFS, flag)

    # If left in open and not visited, move left
    if j>0 and maze.maze[i][j-1] == 0 and vis[i][j-1] == 0:
        solveDFS(maze, i, j-1, l, r, vis, solutionDFS, flag)

    # If we've reached the end, we're done
    return;


# Function to visualize the algorithm
def showDFS(solution, screen, running):
    # Color of maze solver
    blue = (0,0,255)

    # For each cell in solution, draw a circle on its position
    for j,i in solution:
        pygame.draw.circle(screen, blue, (i*40+20,j*40+20), 10, 0)
        pygame.display.update()
        if j==0 and i==1:
            pygame.time.delay(1000)
        pygame.time.delay(200)

        # If we've reached the end, we're done
        if j==10 and i==19:
            running = False
            pygame.time.delay(3000)
            break
    
    return running