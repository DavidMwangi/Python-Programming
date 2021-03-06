"""

Write a program which asks the user to enter a positive integer 'n' (Assume that the user always enters a positive integer) and based on the following conditions, prints the appropriate results exactly as shown in the following format (as highlighted in yellow). 
when 'n' is divisible by both 2 and 3 (for example 12), then your program should print
BOTH
when 'n' is divisible by only one of the numbers i.e divisible by 2 but not divisible by 3 (for example 8), or divisible by 3 but not divisible by 2 (for example 9), your program should print
ONE
when 'n' is neither divisible by 2 nor divisible by 3 (for example 25), your program should print
NEITHER

"""

#prompt user for input

n = int(input("Enter a positive integer:\n"))

if n % 2 == 0 and n % 3 == 0:

    print("BOTH")

elif (n % 2 != 0 and n % 3 == 0) or (n % 2 == 0 and n % 3 != 0):

    print("ONE")

else:

    print("NONE")
