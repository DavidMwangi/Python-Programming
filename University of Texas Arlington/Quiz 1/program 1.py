"""

Write a program that asks the user to enter their age in years as input
(assume that the user enters a positive integer) and calculates and
prints how old the user is in terms of days.
Assume that there are 365 days in a year.

"""

age = int(input("Please enter your age\n"))

days = age * 365

ageInDays = ("You are %s days old")

print (ageInDays%(days))
