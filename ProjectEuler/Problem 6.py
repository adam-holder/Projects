##Project Euler Problem 6: Sum Square difference
##
##The sum of the squares of the first ten natural numbers is,
##1^2 + 2^2 +...+ 10^2 = 385
##The square of the sum of the first ten natural numbers is,
##(1 + 2 + ... + 10)^2 = 55^2 = 3025
##Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
##3025 - 385 = 2640
##Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#creates a List of "maxNumber" size based on the user input
def NumberList (maxNumber: int) -> list:
    NumberListOutput = []
    for i in range(maxNumber):
        NumberListOutput.append(i+1)
    return NumberListOutput

#takes a list of numbers, squares each number in the list and sums the total
def SumofSquares (List: list) -> int:
    total = 0
    for number in List:
        total += (number)**2
    return total

#takes list of numbers, finds the sum of all the numbers in the list and squares the result
def SquareofSum (List: list) -> int:
    total = sum(List)**2
    return total

maxNumber = int(input("Input top of range: "))
NumberListOutput = NumberList(maxNumber)
print ("The Sum of the Squares up to " + str(maxNumber) + " equals " + str(SumofSquares(NumberListOutput)))
print ("The Square of the sum of each number up to " + str(maxNumber) + " equals " + str(SquareofSum(NumberListOutput)))
difference = SquareofSum(NumberListOutput) - SumofSquares(NumberListOutput)
print("The difference of the two is " + str(difference))
