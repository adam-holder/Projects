# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# RRDD, RDRD, RDDR, DRRD, DRDR, DDRR
#
# How many such routes are there through a 20×20 grid?

#NOTES: gridSize limits how many R's and D's.
import time

def initializePath(gridSize):
    #create blank string of equal 0's and 1's. Eg. gridsize 2 = 0011 the earliest time that a positive match is possible.
    path = ''
    for i in range(0,gridSize):
        path = path + '0'
    for j in range(0,gridSize):
        path = path + '1'
    return path

def initializeMaxPath(gridSize):
    #create a string that has 1's equal to gridSize, then 0's and then a 1. Eg. gridSize=2 '1101' creates a logical cutoff point for upticking the binary number. If we hit 1 more than the first half of iterations, we don't need to check anymore.
    maxPath = ''
    for i in range(0,gridSize):
        maxPath = maxPath + '1'
    if gridSize-1 != 0:
        for j in range(0,gridSize-1):
            maxPath = maxPath + '0'
    maxPath = maxPath + '1'
    return maxPath

def countZerosOnes(path):
    zeros = 0
    ones = 0
    for digit in path:
        if digit == '0':
            zeros += 1
        else:
            ones += 1
    if zeros == ones:
        return True
    else:
        return False

def incrementBinary(val,gridSize):
    decNum = int(val, 2) + 1
    biNum = bin(decNum).replace("0b", "")
    newBiStr = ''
    #add leading 0's
    if gridSize*2-len(biNum) != 0:
        for placeholder in range(0,gridSize*2-len(biNum)):
            newBiStr = newBiStr + '0'
    #add binary number to end of string
    newBiStr = newBiStr + str(biNum)
    return newBiStr

def pathFinder(size):
    start_time = time.time()
    gridSize = size
    print(f'Testing gridsize {size}')
    validPaths = []
    path = initializePath(gridSize)
    maxPath = initializeMaxPath(gridSize)
    while (path != maxPath):
        if countZerosOnes(path) == False:
            path = str(incrementBinary(path,gridSize))
            continue
        else:
            # letterPath = path
            # for rep in (('1','D'),('0','R')):
            #     letterPath = letterPath.replace(*rep)
            # validPaths.append(letterPath)
            validPaths.append(path)
            path = str(incrementBinary(path,gridSize))
    print(f'Total Paths: {len(validPaths)}')
    elapsed_time = time.time() - start_time
    print('Elapsed Time: ', elapsed_time)

pathFinder(2)
