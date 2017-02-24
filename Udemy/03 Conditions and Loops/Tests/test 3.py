"""

The weight of a person on the moon is 1/6th the weight of a
person standing on earth. Say that your weight on earth increases by 1 kg
every year. Write a program that will print your weight on the moon every
year for the next 10 years. (Your initial weight can be anything.)

"""

#This program asks the user to input their current weight
#The program then callculates and displays their weight on the moon for the next 10 years

weight = input("KIndly enter your current weight:\n")

year = 1

try:

    for year in range (1, 11):

        weight_on_moon = float(1/6 * float(weight))

        print(weight_on_moon)

        weight = float(weight) + 1

except:

    print ("Check your weight again\n")
