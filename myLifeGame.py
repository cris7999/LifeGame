import numpy as np

def random_grid(n):
    grid = np.array([])
    numeric_grid = np.random.rand(n,n).round()
    grid=np.zeros((n, n), dtype=bool)
    print(numeric_grid)
    for i in range(len(numeric_grid)):
        for j in range(len(numeric_grid)):
            if (numeric_grid[i][j] == 1):
                grid[i][j] = True
            else:
                grid[i][j] = False
    print (grid)
    return grid

def show_grid():
    print(grid)

def count_neighbors(i , j):
    count = 0
    if(i == 0 and j==0):
        if(grid[i + 1][j] is True):
            count += 1
        if(grid[i][j + 1] is True):
            count +=1
        if(grid[i +1][j + 1] is True):
            count +=1

    elif (i == 0 and j == len(grid)):
        if(grid[i + 1][j] is True):
            count += 1
        if(grid[i][j - 1] is True):
            count +=1
        if(grid[i - 1][j - 1] is True):
            count +=1

    elif (i == len(grid) and j == 0):
        if(grid[i][j + 1] is True):
            count += 1
        if(grid[i - 1][j] is True):
            count +=1
        if(grid[i - 1][j + 1] is True):
            count +=1

    elif (i == len(grid) and j == len(grid)):
        if(grid[i][j - 1] is True):
            count += 1
        if(grid[i - 1][j] is True):
            count +=1
        if(grid[i - 1][j - 1] is True):
            count +=1
        
    return count


def updateGrid():
    for i in range(len(grid)):
        for j in range(len(grid)):
            num_neighbors = count_neighbors(i , j)
            if(grid[i][j] is True):
                if((num_neighbors < 2) or (num_neighbors > 3)):
                    grid[i][j] = False
            else:
                if(num_neighbors == 3):
                    grid[i][j] = True    

    return grid        
                    

grid = random_grid(3)
show_grid()
updateGrid()
print("ACTUALIZACION:")
show_grid()
