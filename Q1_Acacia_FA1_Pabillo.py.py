import math
# This imports the math library, with predefined functions
x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
d =  math.sqrt(math.pow((x2 - x1), 2) + (math.pow((y2 - y1), 2)))
#This part of the code is what processes the formula for the distance.

print ("The distance between the two points is", d)

#It made my coding easier, because i didn't have to do the functions manually. The square root and power funtions. It would be tedious to do, do to the manual coding for each function which is substantially harder than using sqrt and math.pow

