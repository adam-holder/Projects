# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(num):
    #initialize collatzChain with starting chain value.
    collatzChain = [num]
    while (num != 1):
        if num % 2 == 0:
            num = int(num/2)
        else:
            num = int(3*num+1)
        collatzChain.append(num)
    # print(f'{collatzChain} has length {len(collatzChain)}')
    return collatzChain

maxChainLength = 0
maxChain = []
maxChainStarter = 0

for i in range(1,1000000):
    testChain = collatz(i)
    chainLength = len(testChain)
    if chainLength > maxChainLength:
        maxChainLength = chainLength
        # print(maxChainLength)
        maxChain = testChain
        maxChainStarter = i
print(f'{maxChainStarter}: With length {maxChainLength}, {maxChain}')

