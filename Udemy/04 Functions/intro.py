#This program defines a function 'hi' that prints out 'Hello' x number f times
#It then prompts the user the number of time they need it printed and prints.

def hi(x): #Define function 'hi' which passes parameter x

    print ("Hello\n" * x)


num = int(input("How many times would you like me to print hello:\n")) #prompt user


hi(num) #Pass user's prompt repl as the parameter of the function

print("\nNow let us add numbers using an add function\n")

def adder(a, b):

    total = a + b
    
    print ("The sum is ", total)



num1 = int(input("Enter the first number\n"))

num2 = int(input("Enter the second number\n"))


adder(num1, num2)










