#FOR LOOP COUNTER

print("FOR LOOP COUNTER\n")

for num in range(1,11):
    print (num)

print("\nEVEN NUMBERS 0 TO 10")

for evens in range (0,11,2):
    print(evens)

#ITERATE A LIST WITH FOR LOOP

print("\nIterating a list with for loop\n")

wizkhalifa = ["Roll up","Work hard Play hard","King of everything","We dem boyz","Black and yellow","Remember"]

for song in wizkhalifa:
    print (song)


for song in wizkhalifa:
    if song == "Roll up":
        print("\nFound Roll up")
 #?? want to print location in list if found 
