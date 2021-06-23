import math
#User inputs amount of Rectangles to judge for Goldenness
N = int(input("How many rectangles do you want to test for Goldenessisity? "))
#initiate list for rectangles
rectangles = []
goldenboys = []
#User inputs length of sides for each rectangle and the dimensions are put into the rectangles list
for i in range(N):
    Sides = sorted(input("List the sides of Rectangle " + str(i+1) + " in the the form x y. Ex. 3 5: ").split())
    #print (Sides)
    rectangles.append(Sides)
#print (rectangles)
#Code calculates ratios and counts number of golden boys
for rectangle in rectangles:
    #iterate through rectangles selecting 1 at a time and gets a ratio of the sides
    ratio = int(rectangle[1])/int(rectangle[0])
    if ((ratio >= 1.6) and (ratio<= 1.7)):
        print ("Congrats you found a golden boy! " + str(rectangle) + " has a ratio of " + str(ratio))
        goldenboys.append(rectangle)
    else:
        print ("Oh no! " + str(rectangle) + " is not a golden boy.")
print ("We found " + str(len(goldenboys)) + " golden boy out of the rectangles you gave us. Thanks!")
