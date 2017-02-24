"""

Create a loop that prints out either even numbers, or odd
numbers all the way up till your age. Ex: 2,4,6,….,14

"""

#The program first asks for user to input age and checks whether the age is an odd or even number
#If even, it prints out all even numbers up until the age
#If odd, it prints all odd numbers up untill the age

age = input("Please enter your age: \n") #user inputs age

try:

        if int(age) % 2 == 0:

            for i in range (2,int(age)+1,2):

                print(i)

        else:

            for i in range (1, int(age)+1,2):

                print (i)

except:

    print ("Invalid age. Please check again\n")
