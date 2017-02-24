print ("Top 5 Rated Movies 2015")

topList = ["Mad Max: Fury Road","Inside Out","Selma","Spotlight","Star Wars: Episode VII - The Force Awakens"]

prompt = input ("Enter the movie number you would like to view and 'all' to view the entire list: \n")

#print (topList [int(prompt)])



if prompt == 'all':
    for counter in range(1,5):
        for i in topList:
            print(str(counter) + i)
            

elif int(prompt)>5 or int(prompt)<1:
   print("Invalid Entry")

else:
    counter = prompt
    print(str(counter)+": " + topList [int(prompt)-1])
