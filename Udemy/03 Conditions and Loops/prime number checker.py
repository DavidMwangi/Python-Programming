#PRIME NUMBER CHECKER

num = int(input("Please enter a number: \n"))

j = 2
counter = 0

while j < num:
    if num % j == 0:
        counter = 1
        j = j+1

    else:
        j = j+1

if counter == 0:
    print (str(num) + " is a prime number\n")

elif counter == 1:
    print (str(num) + " is not a prime number\n")

else:
    pass
