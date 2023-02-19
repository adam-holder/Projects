# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# RRDD, RDRD, RDDR, DRRD, DRDR, DDRR
#
# How many such routes are there through a 20×20 grid?

#NOTES: gridSize limits how many R's and D's.
import time

def initializeMinPath(gridSize):
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
    for j in range(0,gridSize):
        maxPath = maxPath + '0'
    return bin(int(maxPath,2)).replace('0b','')

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

def binaryBuilder(maxNum,minNum,gridSize):
    biArr = []
    maxNum = int(maxNum,2)
    minNum = int(minNum,2)
    for i in range(minNum,maxNum+1):
        newBiStr = ''
        check = bin(i).replace('0b','')
        #add leading 0's
        if gridSize*2 - len(check) != 0:
            for placeholder in range(0,gridSize*2-len(check)):
                newBiStr = newBiStr + '0'
            #add binary number to end of string
        newBiStr = newBiStr + check
        if countZerosOnes(newBiStr) == False:
            continue
        else:
            biArr.append(newBiStr)
    return biArr
##    currentNum = bin(int(strNum,2)-1).replace('0b','')
##    minNum = bin(int(minNum,2)).replace('0b','')
##    if currentNum == minNum:
##        biArr.append(currentNum)
##        return biArr
##    if countZerosOnes(strNum) == False:
##        return binaryBuilder(currentNum,minNum,biArr)
##    else:
##        biArr.append(strNum)
##        return binaryBuilder(currentNum,minNum,biArr)


def pointFinder(size):
    startTime = time.time()
    gridSize=size
    minNum = initializeMinPath(size)
    biNum = initializeMaxPath(size)
    validPaths = binaryBuilder(biNum,minNum,size)
    print (f'{len (validPaths)} paths')
    elapsedTime = time.time() - startTime
    print('Elapsed Time: ', elapsedTime)
