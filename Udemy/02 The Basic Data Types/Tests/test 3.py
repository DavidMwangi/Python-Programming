#QUESTION 3

#Create a small program that will take in a User’s name and last
#name (Hint: varName = input(“Enter your name”)), store both in two
#variables. And then print out a message saying (“Hello there, FirstName
#LastName”) (Using the %s symbols)

firstName = input ("Please enter your first name: ")

lastName = input ("Please enter your last name: ")

greeting = ("Hello there %s %s")

print (greeting %(firstName, lastName))
