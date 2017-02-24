
print ("Below is the list of operations you can use\n")
print ("add for additifon")
print ("sub for subtraction")
print ("mult for multiplication")
print ("div for division")

op = input("\nWhat operaton do you want to perform?\n")

num1 = input("Please enter the first number: \n")

num2 = input("Please enter the second number: \n")


def addition(x,y):
    
    return x + y

def subtraction(x,y):

    return x - y

def multiplication(x,y):

    return x * y

def division(x,y):

    return x / y


try:

    if str(op) == 'add':

        print(addition(float(num1),float(num2)))

    elif str(op) == 'sub':

        print(subtraction(float(num1),float(num2)))

    elif str(op) == 'mult':

        print(multiplication(float(num1),float(num2)))

    elif str(op) == 'div':

        print(division(float(num1),float(num2)))

    else:

        print ("Invalid Option Entry. Please check again\n")

except:

    print ("Invald Number Entry. Please check again\n")

finally:

    print ("Thank you for using this simple calculator\n")
