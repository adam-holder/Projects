import random

def mergesort (arr):
    #If an array "arr" has more than 1 item, find a midpoint in that array.
    if len(arr)>1:
        midpoint = len(arr)//2

        #create two more smaller arrays from position 0 to the midpoint and from the midpoint to the end.
        Leftside = arr[:midpoint]
        Rightside = arr[midpoint:]
        #run mergesort on the leftside array, shrinking it again
        mergesort(Leftside)
        #run mergesort on the rightside array, shrinking it again
        mergesort(Rightside)

        i = j = k = 0
        #compare the values of leftside and rightside, put the smallest one in the next k position of arr[]. Repeat until leftside or rightside is depleted.
        while i < len(Leftside) and j < len(Rightside):
            if Leftside[i] < Rightside[j]:
                arr[k] = Leftside[i]
                i += 1
            else:
                arr[k] = Rightside[j]
                j += 1
            k += 1

        #if rightside was depleted first, empty the last few values of leftside into arr[]
        while i < len(Leftside):
            arr[k] = Leftside[i]
            i += 1
            k += 1
        #if leftside was depleted first, empty the last few values of rightside into arr[]
        while j < len(Rightside):
            arr[k] = Rightside[j]
            j += 1
            k += 1

#prints array A but separated by spaces instead of just the array.
def printArray(A):
    for i in range(len(A)):
        print(A[i], end=" ")
    print()

#generates an array of random numbers to sort
def generateArray(length):
    genA = []
    for i in range(length):
        genA.append(random.randint(1,1000))
    return genA

#main code:
#generate an array based on user input, print the unsorted array, use mergesort, print sorted array.
if __name__ == '__main__':
    A = generateArray(int(input("Input size of generated array: ")))
    print("Array provided:", end="\n")
    printArray(A)
    mergesort(A)
    print("Sorted array: ", end="\n")
    printArray(A)
