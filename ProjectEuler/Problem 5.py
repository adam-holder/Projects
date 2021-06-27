##Project Euler Problem 5: Smallest Multiple
##
##2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
##What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

def FactorsUpTo (target: int) -> list:
    #create a list of factors [1,2.....,target]
    FactorList = []
    for i in range(1,target+1):
        FactorList.append(i)
    return FactorList

#creates a list of factors [1,2,.....,target] and saves it to FactorList
target = int(input("Input the highest factor: "))
FactorList = FactorsUpTo(target)

solution = 0
ApprovedFactors = 0

for i in range(1,1000000000):
    #iterate through every i up to a range, currently 1000000000
    for factor in FactorList:
        #iterate through each factor in FactorList and check:
        #if i is divisible by factor, if so, ApprovedFactors ticks up by 1.
        if i % factor == 0:
            ApprovedFactors += 1
        #if i is NOT divisible by factor, set ApprovedFactors back to 0 and break to the next i.
        if i % factor != 0:
            ApprovedFactors = 0
            break
        #if we make it to the end of the FactorList and everything is divisible, we found the lowest solution. Set solution to the value of i.
        if ApprovedFactors == target:
            solution = i
    #when i is NOT 0, we have found the solution. Break out of the code and finish.
    if solution != 0:
        break
print(solution)
