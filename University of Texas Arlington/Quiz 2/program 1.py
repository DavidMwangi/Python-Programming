"""

Write a program which asks the user to enter their age in years (Assume that the user always enters an integer) and based on the following conditions, prints the output exactly as in the following format (as highlighted in yellow): 
When age is less than or equal to 0, your program should print
UNBORN
When age is greater than 0 and less than or equal to 150, your program should print
ALIVE
When age is greater than 150, your program should print
VAMPIRE

"""

#prompt user for age

age = int(input("Enter your age:\n"))

if age <= 0:

    print("UNBORN\n")

elif age > 0 and age <= 150:

    print ("ALIVE\n")

else:

    print ("VAMPIRE\n")
