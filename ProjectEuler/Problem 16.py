# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

def twoToPower(pow):
    return 2 ** int(pow)

def runProblem():
    storedPow = input('Storing a number 2 raised to x power. Select value for x: ')
    storedNum = str(twoToPower(storedPow))
    numSum = 0
    for digit in storedNum:
        numSum += int(digit)
    print(f'Summing the resulting digits of 2^{storedPow}...\nTotal Sum: {numSum}')

runProblem()
