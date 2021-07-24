import pygame

#TREMAUX ALGORITM
def solveDFS(maze, i, j, l, r, vis, solutionDFS, flag):
    if i == l and j == r :
        solutionDFS.append((i,j))
        flag = True
        return;
    if not flag:
        solutionDFS.append((i,j))
    vis[i][j] = 1
    if i<maze.height-1 and maze.maze[i+1][j] == 0 and vis[i+1][j] == 0:
        solveDFS(maze, i+1, j, l, r, vis, solutionDFS, flag)
    if j<maze.width-1 and maze.maze[i][j+1] == 0 and vis[i][j+1] == 0:
        solveDFS(maze, i, j+1, l, r, vis, solutionDFS, flag)
    if i>0 and maze.maze[i-1][j] == 0 and vis[i-1][j] == 0:
        solveDFS(maze, i-1, j, l, r, vis, solutionDFS, flag)
    if j>0 and maze.maze[i][j-1] == 0 and vis[i][j-1] == 0:
        solveDFS(maze, i, j-1, l, r, vis, solutionDFS, flag)
    return;

def showDFS(solution, screen, running):
    blue = (0,0,255)
    for j,i in solution:
        pygame.draw.circle(screen, blue, (i*40+20,j*40+20), 10, 0)
        pygame.display.update()
        if j==0 and i==1:
            pygame.time.delay(1000)
        pygame.time.delay(200)
        if j==10 and i==19:
            running = False
            pygame.time.delay(3000)
            break
    return running