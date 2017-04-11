"""

This is an introduction to object oriented programming in Python.
OOP is an incredibly powerful programming methodology.
Why OOP?

1. Code Re-use
2. Proper Isolation of code. Easier to read and test.
3. Code Legibility,
4. Modeling data.

OOP methodology creates a custom datatype(object) and defines it's properties.

A constructor function is a function that gets executed whenever a new instance of a class is created.


"""

from math import pi
from random import uniform



"""

#Circumference using a list


circle = [["First",4.2,0],["Second",45.0]]

circle[0][2] = calcCircumference(circle[0][1])

print(circle)
"""

#Circle Class Definition

class Circle:
    
    #member properties of class Circle
    
    def calcCircumference(self):

        return pi * self.radius * 2

    def calcDiameter(self):

        return 2 * self.radius

    def calcArea(self):

        return pi * pow(self.radius,2)

circles = []

for i in range(0,10):

    c = Circle()
    c.radius = uniform(1.1,9.5)
    circles. append(c)

    
for c in circles:

    print("Radius:", c.radius,\
          "Circumference:", c.calcCircumference(),\
          "Diameter:", c.calcDiameter(),\
          "Area:", c.calcArea())
