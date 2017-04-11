"""

This is an introduction to object oriented programming in Python.
OOP is an incredibly powerful programming methodology.
Why OOP?

1. Code Re-use
2. Proper Isolation of code. Easier to read and test.
3. Code Legibility,
4. Modeling data.

OOP methodology creates a custom datatype(object) and defines it's properties.

"""

from math import pi

def calcCircumference(radius):

    return pi * radius * 2

"""

#Circumference using a list


circle = [["First",4.2,0],["Second",45.0]]

circle[0][2] = calcCircumference(circle[0][1])

print(circle)
"""

class Circle: #Circle Class Definition

    pass

#Circumference using range


circles = []

for i in range(0,3):
    
    c = Circle() #creates a circle instance c for every iteration
    c.radius = uniform(1.1,9.5) #assign a random uniform radius to the circle c
    c.circumference = calcCircumference(c.radius) #calculates the circumference for that circle intance
    
    circles.append(c) #appends the instance properties to list circle
    
for c in circles: #Loops over list circles and prints out each instances radius and circumference
    
    print("Radius: ", c.radius, " Circumference: ",c.circumference) 
