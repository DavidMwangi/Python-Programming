import random

user_num = int(input("Please enter a number that you would like the computer to guess:\n"))

comp_guess = random.randint(0,100)

current_guess = comp_guess

while True:
    
    print("Is the number "+ str(comp_guess) + "?")

    user_response = input("")

    if user_response == "yes":

        print("Yeeeey.\nHave nailed it\n")

        break

    elif user_response == "no":

        advise = input("Well, should I guess higher or lower?\n")

        if advise == "higher":

            comp_guess = random.randint(comp_guess,100)

        elif advise == "lower":

            comp_guess = random.randint(0,comp_guess)

        else:

            pass

    else:

        pass

