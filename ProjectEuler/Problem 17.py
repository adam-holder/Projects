# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# Numbers 1-19 unique. 20 starts tens digit + single digit. 100 starts single digit + hundred + and + tens. 1000 is one thousand.
import time

def numcheck(num):
    andNeeded = False
    charTot = 0
    if num/1000 >= 1:
        charTot = charTot + numbers[checkThousands(num)] + numbers[1000]
        num = num % 1000
        if num > 0:
            andNeeded = True
        else:
            return charTot
    if num/100 >= 1:
        charTot = charTot + numbers[checkHundreds(num)] + numbers[100]
        num = num % 100
        if num > 0:
            andNeeded = True
        else:
            return charTot
    if num >= 20:
        charTot = charTot + checkOverTwenty(num)
    else:
        charTot =  charTot + numbers[num]
    if andNeeded ==  True:
        charTot = charTot + 3
    return charTot

def checkThousands(num):
    thouCount = (num - (num % 1000))/1000
    return thouCount

def checkHundreds(num):
    hundCount = (num - (num % 100))/100
    return hundCount

def checkOverTwenty(num):
    tenCount = numbers[num - (num % 10)]
    if num % 10 > 0:
        tenCount = tenCount + numbers[num % 10]
    return tenCount


startTime = time.time()
numbers = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:8}
numTot = 0
for i in range(1,1001):
    numTot += numcheck(i)
print(f'The addition of the letters of every number from 1-1000 is {numTot}')
elapsedTime = time.time() - startTime
print('Elapsed Time: ', elapsedTime)
