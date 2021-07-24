import pygame
from maze import maze

# WALL FOLLOWER ALGORITHM
# Function to check if we can move Forward or not
def Forward(maze, i, j, face, vis):
    if face=='U':
        if i>0 and maze.maze[i-1][j] == 0 and vis[i-1][j] != 1:
            return True
    elif face=='R':
        if j<maze.width-1 and maze.maze[i][j+1] == 0 and vis[i][j+1] != 1:
            return True
    elif face=='D':
        if i<maze.height-1 and maze.maze[i+1][j] == 0 and vis[i+1][j] != 1:
            return True
    elif face=='L':
        if j>0 and maze.maze[i][j-1] == 0 and vis[i][j-1] != 1:
            return True
    return False

# Function to check if we can move Left or not
def Left(maze, i, j, face, vis):
    if face=='U':
        if j>0 and maze.maze[i][j-1] == 0 and vis[i][j-1] != 1:
            return True
    elif face=='R':
        if i>0 and maze.maze[i-1][j] == 0 and vis[i-1][j] != 1:
            return True
    elif face=='D':
        if j<maze.width-1 and maze.maze[i][j+1] == 0 and vis[i][j+1] != 1:
            return True
    elif face=='L':
        if i<maze.height-1 and maze.maze[i+1][j] == 0 and vis[i+1][j] != 1:
            return True
    return False

# Function to check if we can move Right or not
def Right(maze, i, j, face, vis):
    if face=='U':
        if j<maze.width-1 and maze.maze[i][j+1] == 0 and vis[i][j+1] != 1:
            return True
    elif face=='R':
        if i<maze.height-1 and maze.maze[i+1][j] == 0 and vis[i+1][j] != 1:
            return True
    elif face=='D':
        if j>0 and maze.maze[i][j-1] == 0 and vis[i][j-1] != 1:
            return True
    elif face=='L':
        if i>0 and maze.maze[i-1][j] == 0 and vis[i-1][j] != 1:
            return True
    return False

# Function to change the direction of the robot
def turn(face, dir):
    if dir=='L':
        if face=='U':
            face = 'L'
        elif face=='R':
            face = 'U'
        elif face=='D':
            face = 'R'
        elif face=='L':
            face = 'D'
    elif dir=='R':
        if face=='U':
            face = 'R'
        elif face=='R':
            face = 'D'
        elif face=='D':
            face = 'L'
        elif face=='L':
            face = 'U'
    elif dir=='B':
        if face=='U':
            face = 'D'
        elif face=='R':
            face = 'L'
        elif face=='D':
            face = 'U'
        elif face=='L':
            face = 'R'
    return face

# Function to solve the maze using Left wall as a guide
def solveWallLeft(maze, i, j, l, r, face, vis, solutionWall, flag):

    # If we've reached the end, we're done
    if i==10 and j==19:
        flag = True
        solutionWall.append((i,j))
        return;

    # If end has been reached, then there is no need to continue
    if not flag:
        # If we can move left, turn left
        if Left(maze, i, j, face, vis) :
            face = turn(face, 'L')
            solveWallLeft(maze, i, j, l, r, face, vis, solutionWall, flag)

        # Otherwise, if we can move forward, do so
        elif Forward(maze, i, j, face, vis) :
            solutionWall.append((i,j))
            vis[i][j] = 1
            if face=='D':
                solveWallLeft(maze, i+1, j, l, r, face, vis, solutionWall, flag)
            elif face=='L':
                solveWallLeft(maze, i, j-1, l, r, face, vis, solutionWall, flag)
            elif face=='R':
                solveWallLeft(maze, i, j+1, l, r, face, vis, solutionWall, flag)
            elif face=='U':
                solveWallLeft(maze, i-1, j, l, r, face, vis, solutionWall, flag)

        # Otherwise, if we can move right, turn right
        elif Right(maze, i, j, face, vis) :
            face = turn(face, 'R')
            solveWallLeft(maze, i, j, l, r, face, vis, solutionWall, flag)

        # If we can do none of the above, then turn around
        else :
            for x in range(0,maze.height):
                for y in range(0,maze.width):
                    vis[x][y]=0
            vis[0][1] = 1
            face = turn(face, 'B')
            solveWallLeft(maze, i, j, l, r, face, vis, solutionWall, flag)
    return

# Function to solve the maze using Right wall as a guide
def solveWallRight(maze, i, j, l, r, face, vis, solutionWall, flag):
    if i==10 and j==19:
        flag = True
        solutionWall.append((i,j))
        return;
    if not flag:
        if Right(maze, i, j, face, vis) :
            face = turn(face, 'R')
            solveWallRight(maze, i, j, l, r, face, vis, solutionWall, flag)
        elif Forward(maze, i, j, face, vis) :
            solutionWall.append((i,j))
            vis[i][j] = 1
            if face=='D':
                solveWallRight(maze, i+1, j, l, r, face, vis, solutionWall, flag)
            elif face=='L':
                solveWallRight(maze, i, j-1, l, r, face, vis, solutionWall, flag)
            elif face=='R':
                solveWallRight(maze, i, j+1, l, r, face, vis, solutionWall, flag)
            elif face=='U':
                solveWallRight(maze, i-1, j, l, r, face, vis, solutionWall, flag)
        elif Left(maze, i, j, face, vis) :
            face = turn(face, 'L')
            solveWallRight(maze, i, j, l, r, face, vis, solutionWall, flag)
        else :
            for x in range(0,maze.height):
                for y in range(0,maze.width):
                    vis[x][y]=0
            vis[0][1] = 1
            face = turn(face, 'B')
            solveWallRight(maze, i, j, l, r, face, vis, solutionWall, flag)
    return

# Function to visualize the solution
def showWall(solution, screen, running):
    red = (255, 0 , 0)
    blue = (0, 0, 255)
    white = (255, 255, 255) 
    m = maze()
    for j,i in solution:
            pygame.draw.circle(screen, blue, (i*40+20,j*40+20), 10, 0)
            pygame.display.update()
            if j==0 and i==1:
                pygame.time.delay(1000)
            pygame.time.delay(200)
            if j==10 and i==19:
                running = False
                for x in range(len(solution)-1):
                    p1 = solution[x]
                    p2 = solution[x+1]
                    pygame.draw.line(screen, red, (p1[1]*40+20, p1[0]*40+20), (p2[1]*40+20, p2[0]*40+20), 2)
                pygame.display.update()
                pygame.time.delay(5000)
                break
            screen.fill(white)
            m.draw(display_surf=screen)
            pygame.display.update()
    return running