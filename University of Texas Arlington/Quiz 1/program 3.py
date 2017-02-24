"""

Write a program that asks the user for a positive integer between 1 and 7
(Assume that the user may enter any number from 1 to 7 both inclusive)
and prints the day of week corresponding to that number in all capital letters.
Assume that the day of the week starts from MONDAY. 

"""

while True:

    num = int(input("Please enter a possitive number from 1 to 7\n"))

    if num < 1:

        print ("Number less than 1\n")
        continue

    elif num == 1:

        print ("MONDAY")
        break

    elif num == 2:

        print ("TUESDAY")
        break

    elif num == 3:

        print ("WEDNESDAY")
        break

    elif num == 4:

        print ("THURSDAY")
        break

    elif num == 5:

        print ("FRIDAY")
        break

    elif num == 6:

        print ("SATURDAY")
        break

    elif num == 7:

        print ("SUNDAY")
        break

    elif num > 7:

        print ("Number greater than 7\n")
        continue

    else:

        print ("Invalid entry\n")
        continue
