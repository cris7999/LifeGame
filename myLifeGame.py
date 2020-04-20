import numpy as np

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


def updateGrid():
    for i in range(len(grid)):
        for j in range(len(grid)):
            num_neighbors = count_neighbors(i , j)
            if(grid[i][j]):
                if((num_neighbors < 2) or (num_neighbors > 3)):
                    grid[i][j] = False
            else:
                if(num_neighbors == 3):
                    grid[i][j] = True    

    return grid        
                    

grid = random_grid(5)
show_grid(grid)
grid = updateGrid()
print("ACTUALIZACION:")
show_grid(grid)
