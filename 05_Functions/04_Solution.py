# Create a function that returns both the area and circumference of a circle given its radius:

import math 
r = int(input("Radius of the circle is: "))

def areaCircumFunc(r):
    area = math.pi * r ** 2
    circum = 2* math.pi * r
    return round(area, 4), round(circum, 4)
A, C = areaCircumFunc(r)
print("Area: ", A, "Circumference: ", C)