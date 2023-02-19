# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# RRDD, RDRD, RDDR, DRRD, DRDR, DDRR
#
# How many such routes are there through a 20×20 grid?

#NOTES: gridSize limits how many R's and D's.
import time

def pathToPoint(row,column):
    if grid[(row,column)] is not None:
        return grid[row,column]
    else:
        if row == 1:
            grid[row,column] = j+1
            return grid[row,column]
        if column == 1:
            grid[row,column] = i+1
            return grid[row,column]
        else:
            grid[row,column] = pathToPoint(row-1,column) + pathToPoint(row,column-1)
            return grid[row,column]

def gridSetup(row,column):
    maxRow = row + 1
    maxCol = column + 1
    grid = {(i,j): None for i in range(1,maxRow) for j in range(1,maxCol)}
    for i in range(1,maxRow):
        grid[(i,1)] = i + 1
    for j in range(1,maxCol):
        grid[(1,j)] = j + 1
    return grid

row,column = input('Input row and column.\neg 1,1: ').split(',')
row = int(row)
column = int(column)
startTime = time.time()
grid = gridSetup(row,column)
print(pathToPoint(row,column))
elapsedTime = time.time() - startTime
print('Elapsed Time: ', elapsedTime)
