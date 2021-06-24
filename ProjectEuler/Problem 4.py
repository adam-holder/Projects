##Project Euler Problem 4: Largest Palindrome Product
##
##A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
##Find the largest palindrome made from the product of two 3-digit numbers.

numberLength = input("Input number length:")
numA = 1
numB = 1
MultiplicationTotal = 0
palindromeList = []

def checkPalindrome(i):
    forwards = list(i)
    backwards = forwards[::-1]
    if forwards == backwards:
        return True

for i in range(10**int(numberLength)):
    for j in range(10**int(numberLength)):
        numA = i+1
        numB = j+1
        MultiplicationTotal = numA * numB
        #print(MultiplicationTotal)
        if checkPalindrome(str(MultiplicationTotal)) == True:
            palindromeList.append(MultiplicationTotal)
print(palindromeList)
print("The largest palindromic number measured by the multiplication of two " + str(numberLength) + " digit numbers is " + str(max(palindromeList)))
