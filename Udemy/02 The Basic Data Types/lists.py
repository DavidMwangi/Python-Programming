#Creating a shopping list with strings

shoppingList = "carrots, eggs, potatoes, bananas"

print (shoppingList + ": List of items using strings" )

print ("\n")

#It is hard to list individual item position within the list when strings are used 


#CREATING LISTS
#With lists it is relatively easier
#Each value in the list is given an index number

newList = ["Oranges", "Arrow roots", "Cabbage", "Onions", "Tomatoes"]

print (newList)
print ("List if items using a list array")


#Printing out individual list items

print("\n")
print (newList[0] +": First item in list")
print (newList[1] +": Second item in list")
print (newList[2] +": Third item in list")
print (newList[3] +": Fourth item in list")
print (newList[4] +": Fifth item in list")

#UPDATING LISTS
#List arrays can be updated unlike with strings

newList[1] = "Coconut"

print("\n")
print(newList)
print ("Updated 2nd item of the list to Coconut")

print("\n")
print (newList[0] +": First item in list")
print (newList[1] +": Updated second item in list")
print (newList[2] +": Third item in list")
print (newList[3] +": Fourth item in list")
print (newList[4] +": Fifth item in list")

#APPENDING NEW ITEMS TO A LIST

print ("\nAdding a sixth item 'Carrots' to our list\n")
newList.append("Carrots")

print (newList)
