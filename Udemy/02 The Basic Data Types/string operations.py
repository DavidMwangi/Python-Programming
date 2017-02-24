#STRING OPERATIONS

firstName = "David"
secondName = "Mwangi"
thirdName = "Mathenge"

#You can print out the values of the 3 variables by adding them together
#The " " prints a space between individual names

fullName = firstName + " " + secondName + " " + thirdName

# * [num] used together with a sring prints out the string [num] number of times

print (fullName + "!" * 3)

#SLICE OPERATIONS

#You can print out any single letter holding a position within the sting
#Remember the indexing starts from 0 not 1
#The first letter of the string holds position 0

print (fullName[0] + ": is the first character of the string" )
print (fullName[7] + ": is the eighth character of the string")

#Printing out a subset of the string

print (fullName[0:4] + ": are the first four characters of the string")
print (fullName[4:] + ": fifth character to the last character of the string")
