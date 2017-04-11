"""

This is an introduction to object oriented programming in Python.
OOP is an incredibly powerful programming methodology.
Why OOP?

1. Code Re-use
2. Proper Isolation of code. Easier to read and test.
3. Code Legibility,
4. Modeling data.

"""

from math import pi

def calcCircumference(radius):

    return pi * radius * 2


circle = [["First",4.2,0],["Second",45.0]]

circle[0][2] = calcCircumference(circle[0][1])

print(circle)
