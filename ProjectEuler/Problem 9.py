##Project Euler Problem 9: Special Pythagorean Triplet
##A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##a^2 + b^2 = c^2
##For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

import math

a=3
b=4
c=5

def checkConditions(a, b, c, sidesTot, hypeTot)-> bool:
    if c < b or c < a or b < a:
        # c>b>a is not true
        return False
    if sidesTot != hypeTot:
        # not a Pythagorean Triplet
        return False
    if a + b + c < 1000:
        # a+b+c too small
        return False


for a in range(3,1000):
    for b in range(4,1000):
        for c in range(5,1000):
            sidesTot = math.pow(a,2)+math.pow(b,2)
            hypeTot = math.pow(c,2)
            if checkConditions(a,b,c,sidesTot,hypeTot)==False:
                continue
            if a+b+c == 1000:
                print(f'The Pythagorean Triplet of {a}, {b}, {c} adds to 1000')
                print(f'The Product of this Triplet is {a*b*c}.')
                exit()


# print (f'a squared is {math.pow(a,2)}')
# print (f'b squared is {math.pow(b,2)}')
# print (f'Total of squared sides is {sidesTot}')
# print (f'Total of hypotenuse squared is {hypeTot}')
