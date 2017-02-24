#PRIME NUMBER GENERATOR


limit = int(input("Please enter the number up to which you want all the prime numbers displayed\n"))

for i in range (2,limit):
    
    j = 2 #This variable is the divisor
    
    counter = 0

    while j < i:
        if i % j == 0:
            counter =1
            j=j+1
        else:
            j=j+1

    if counter == 0:
        print (str(i) + " is a prime number")
