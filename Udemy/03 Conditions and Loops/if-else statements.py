print ("THIS IS A SIMPLE FOUR OPERATION TWO NUMBER CALCULATOR\n")

print("Below is the list of options\n")
print("Press 1 to add\n")
print("Press 2 to subtract\n")
print("Press 3 to multiply\n")
print("Press 4 to divide\n")

choice = int(input("What operation do you want to carry out: \n"))

num1 = float(input("Enter first number: \n"))
num2 = float(input("Enter second number: \n"))


if choice == 1:
    print ("Addition results: ", num1+num2)

elif choice ==2:
    print("Subtraction results: ",num1-num2)

elif choice ==3:
    print("Multiplication results: ",num1*num2)

elif choice == 4:
    print ("Division results: ",num1/num2)

else:
    print ("Invalid Entry")
