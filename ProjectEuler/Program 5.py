##Project Euler Problem 5: Smallest Multiple
##
##2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
##What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

def FactorsUpTo (target: int) -> list:
    #create a list of factors up to a "target"
    FactorList = []
    for i in range(1,target+1):
        FactorList.append(i)
    return FactorList

target = int(input("Input the highest factor: "))
FactorList = FactorsUpTo(target)

solution = 0
ApprovedFactors = 0

for i in range(1,1000000000):
    for factor in FactorList:
        if i % factor == 0:
            ApprovedFactors += 1
        if i % factor != 0:
            ApprovedFactors = 0
            break
        if ApprovedFactors == target:
            solution = i
    if solution != 0:
        break
print(solution)
