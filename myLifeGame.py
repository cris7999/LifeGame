import numpy as np
import pygame
import time

def random_grid(n):
    grid = np.array([])
    numeric_grid = np.random.rand(n,n).round()
    grid=np.zeros((n, n), dtype=bool)

    for i in range(len(numeric_grid)):
        for j in range(len(numeric_grid)):
            if (numeric_grid[i][j] == 1):
                grid[i][j] = True
            else:
                grid[i][j] = False
    return grid

def show_grid(grid):
    print(grid)

def count_neighbors(i , j):
    count = 0
    real_len=len(grid) - 1
    visited = False
    #corners
    if(i == 0 and j==0):
        visited = True
        if(grid[i + 1][j]):
            count += 1
        if(grid[i][j + 1]):
            count +=1
        if(grid[i +1][j + 1]):
            count +=1

    elif (i == 0 and j == real_len and (not visited)):
        visited = True
        if(grid[i + 1][j]):
            count += 1
        if(grid[i][j - 1]):
            count +=1
        if(grid[i - 1][j - 1]):
            count +=1

    elif (i == real_len and j == 0 and (not visited)):
        visited = True
        if(grid[i][j + 1]):
            count += 1
        if(grid[i - 1][j]):
            count +=1
        if(grid[i - 1][j + 1]):
            count +=1

    elif (i == real_len and j == real_len and (not visited)):
        visited = True
        if(grid[i][j - 1]):
            count += 1
        if(grid[i - 1][j]):
            count +=1
        if(grid[i - 1][j - 1]):
            count +=1
    #edges
    elif (i == 0 and (not visited)):
        visited = True
        if(grid[i + 1][j]):
            count += 1
        if(grid[i][j + 1]):
            count +=1
        if(grid[i + 1][j + 1]):
            count +=1
        if(grid[i + 1][j - 1]):
            count +=1
        if(grid[i][j - 1]):
            count +=1

    elif (i == real_len and (not visited)):
        visited = True
        if(grid[i - 1][j]):
            count += 1
        if(grid[i][j + 1]):
            count +=1
        if(grid[i - 1][j + 1]):
            count +=1
        if(grid[i - 1][j - 1]):
            count +=1
        if(grid[i][j - 1]):
            count +=1

    elif (j == 0 and (not visited)):
        visited = True
        if(grid[i][j + 1]):
                count += 1
        if(grid[i + 1][j]):
            count +=1
        if(grid[i + 1][j + 1]):
            count +=1
        if(grid[i - 1][j + 1]):
            count +=1
        if(grid[i - 1][j]):
            count +=1

    elif( j == real_len and (not visited)):
        visited = True
        if(grid[i][j - 1]):
            count += 1
        if(grid[i + 1][j]):
            count +=1
        if(grid[i + 1][j - 1]):
            count +=1
        if(grid[i - 1][j - 1]):
            count +=1
        if(grid[i - 1][j]):
            count +=1
    if (not visited):
        visited = True
        if(grid[i][j - 1]):
            count += 1
        if(grid[i][j + 1]):
            count +=1
        if(grid[i - 1][j]):
            count +=1
        if(grid[i + 1][j]):
            count +=1

    return count


def updateGrid(grid):

    new_grid= np.copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            num_neighbors = count_neighbors(i , j)
            if(grid[i][j]):
                if((num_neighbors < 2) or (num_neighbors > 3)):
                    new_grid[i][j] = False
            else:
                if(num_neighbors == 3):
                    new_grid[i][j] = True

    return new_grid

pygame.init()

pygame.display.set_caption("Life Game")
width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))
bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 25, 25
dimCW = width / nxC
dimCH = height / nyC

grid = random_grid(nxC)
for x in range(0,nxC):
    for y in range(0,nyC):
        grid[x ,y] = False

grid[5,3] = True
grid[5,4] = True
grid[5,5] = True

while True:

    screen.fill(bg)
    time.sleep(0.5)
    grid=updateGrid(grid)
    for x in range(0,nxC):
        for y in range(0,nyC):

            poly = [((x) * dimCW, y*dimCH),
                    ((x + 1) * dimCW, y*dimCH),
                    ((x + 1) * dimCW, (y + 1)*dimCH),
                    ((x) * dimCW, (y + 1)*dimCH)]

            if(grid[x][y]):
                pygame.draw.polygon(screen, (255, 255, 255),poly,1)
            else:
                pygame.draw.polygon(screen, (128,128,128),poly,0)

    pygame.display.flip()
