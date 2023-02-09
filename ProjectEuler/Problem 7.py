##Project Euler Problem 7: 10001st Prime
##
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##What is the 10 001st prime number?
import math
#Generate an Array that is 1+sizeofarray in size. This creates an array from position 0 to size of array with each item initializing as True
def GenerateArray (size: int) -> list:
    SieveArray = []
    for i in range(size+1):
        SieveArray.append(True)
    return SieveArray

#Pulls a list into SieveArray and uses the Sieve of Eratosthenes. Starting with position 2, checks to see if i is True, if so, i^2 and each multiple of i after that are marked False.
#Then a second loop, checks the new list and appends the positions of each True starting at position 2 and adds those numbers into Primes. If the length of Primes is 10001 (meaning we found the 10001st prime) it breaks out of the loop and prints the 10001st Prime
def SieveArray (list: list):
    Primes = []
    for i in range(2,int(math.sqrt(len(list)))):
        if list[i] == True:
            for j in range(i**2,len(list),i):
                list[j]=False
    for k in range(2,len(list)):
        if list[k] == True:
            Primes.append(k)
            if len(Primes) == 10001:
                break
    return Primes

sizeofarray = int(input("Input Size of Array: "))
A = GenerateArray(sizeofarray)
Primes = SieveArray(A)
while len(Primes) < 10001:
    print(f'SieveArray is too smalland we only found {len(Primes)} Prime Numbers.\nPlease enter a new array with size greater than {sizeofarray}')
    sizeofarray = int(input("Input new size of array: "))
    A = GenerateArray(sizeofarray)
    Primes = SieveArray(A)
print ("The 10001st prime is: " + str(max(Primes)))
