"""

This is a very old algorithm for finding the square root of a number.

The algorithm is attributed to Alexandria of Heron, dating 2nd century BC

"""

num = int(input(">"))

guess = num/2

while guess * guess != num:

    guess = (guess + (num/guess)) / 2

print(guess)
