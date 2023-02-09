# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math
def isPrime(n)-> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5 #Lowest positive 6k-1 value
    while(math.pow(i,2)<=n):
        #if n is evenly divisble by 6k-1 or 6k+1, it is not prime.
        if(n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True

primeList = []
maxRange = int(input('The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.\nPlease enter a number to calculate the sum of the primes\nlower than your choice: '))
for n in range(2,maxRange+1):
    if isPrime(n) == True:
        primeList.append(n)
print(f'The sum of all {len(primeList)} primes below {maxRange} is {sum(primeList)}')
