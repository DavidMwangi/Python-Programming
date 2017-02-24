#Tuples and lists are quite similar.
#The major difference between the two is that the data in tuples cannot be manipulated.
#Unlike in lists, we cannot append or delete items in a tuple

#CREATING TUPLES

tuple = ("Hillary Clinton","Donald Trump")

print (tuple)

#Trying to append or delete items from a tuple will result to an error

#tuple.append("Bill")

#del tuple["Hillary Clinton"]

#However, tuples can change after reinitialization

print ("\nReinitializing our tuple\n")

tuple = ("Barack Obama","Joe Biden")

print(tuple)

#Indexing and slicing like in lists are possible

print("\nIndexing tuple items by position")

print ("Postiton 1: ", tuple[0])
print ("Position 2: ", tuple[1])

#Deleting tuple items is impossible but deleting a tuple is easy and possible

del tuple




