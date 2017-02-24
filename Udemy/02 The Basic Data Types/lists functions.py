#DELETE ITEM FUNCTION

shoppingList = ["Oranges", "Arrow roots", "Cabbage", "Onions", "Tomatoes"]

print("My Shopping List \n")
print(shoppingList)

print("\nSame shopping with the 4th item deleted\n")

del shoppingList[3]

print(shoppingList)

#APPENDING ITEM TO LIST

print("\nAppending Brocolli and Bananas to the list\n")

shoppingList.append("Brocolli")
shoppingList.append("Bananas")

print(shoppingList)

#LENGTH OF A LIST

print("\nLenth of the list\n")

print(len(shoppingList))

#OPERATIONS LIST FUNCTIONS

#ADDING LISTS

print("\nADDING LISTS\n")

numArray1 = [12,45,64,56,24]
numArray2 = [6987,46,677,56,4325,236,56]

print("\nArray 1\n")
print(numArray1)
print("\nArray 2\n")
print (numArray2)

numArray3 = numArray1 + numArray2

print("\nArray 3 = Array 1 + Array 2\n")
print(numArray3)

#MAX AND MIN FUNCTIONS

print("\nMax in Array 3\n")
print (max(numArray3))

print("\nMin in Array 3\n")
print(min(numArray3))

#COUNT FUNCTION

print("\nCount how many times 56 appears\n")
print (numArray3.count(56))

wordArray = ["David", "Moses", "John", "David", "Kevin", "david"]

print ("\nCount how many times 'David' appears in a word arrayn\n")

print (wordArray.count("David"))
