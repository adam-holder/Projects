#Euler Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

GoodNumbers = []
exp = 0
for i in range(1000):
    if ((i % 3 == 0) or (i % 5 == 0)):
        GoodNumbers.append(i)
print (sum(GoodNumbers))

#Solution to question: 233168

# Out of curiosity I tested at range = 1,000,000 and range = 1,000,000,000 and found that a pattern formed where i was a power of 10. Here is code exploring that.
# GoodNumbers = []
# exp = 0
# for i in range(10000000):
#     if ((i % 3 == 0) or (i % 5 == 0)):
#         if i % 10**exp == 0:
#             print(sum(GoodNumbers))
#             exp += 1
#         GoodNumbers.append(i)
# print (sum(GoodNumbers))
