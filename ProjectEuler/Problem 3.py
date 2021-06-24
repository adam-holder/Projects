##Project Euler Problem 3: Largest Prime Factor
##
## The prime factors of 13195 are 5, 7, 13 and 29.
##
## What is the largest prime factor of the number 600851475143 ?

#This prime tester is based off of Wilson's Theorem. Every prime has the form 6k+1 or 6k-1.
#This tests an integer n where if it is divisble by 2 or 3 it returns false, if it is 2 or 3 it returns true, and if n is of the from 6k+1 or 6k-1 it checks to see if any i value divides evenly if so, it returns False. Otherwise, it is prime.
import math
def primetest(n: int) -> bool:
    if n <=3:
        return n>1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

#Initialize the PrimeFactors List and the listed Big Number as BigNum
PrimeFactors = []
BigNum = 600851475143

#loop to see if i divides evenly into BigNum. If it does and it is prime, adds i to the PrimeFactors list. If the product of PrimeFactors equals BigNum it stops the loop, prints the factors and announces the biggest factor.
for i in range(2,int(BigNum/2)):
    if BigNum % i == 0 and primetest(i) == True:
        print(i)
        PrimeFactors.append(i)
    if math.prod(PrimeFactors) == BigNum:
        break
print (PrimeFactors)
print (str(max(PrimeFactors)) + " is the largest prime factor.")
