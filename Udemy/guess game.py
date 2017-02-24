import random #importing the random module

computer_guess = random.randint(0,100)#Computer guess is a random number between 0 and 100

end = 0

while end == 0:

    try:

        user_guess = int(input("Guess a number between 0 and 100\n"))
            

        if user_guess < 0 or user_guess > 100:

            print("Your guess is out of range. Please guess a number between 0 and 100\n")
            end = 0

        elif computer_guess > user_guess:

            print("Your guess is lower than computer guess. Guess higher\n")

            end = 0


        elif user_guess > computer_guess:

            print("Your guess is higher than the computer guess. Guess lower\n")

            end = 0
            

        else:

            print("Your guess is correct.\nThe computer guess was ", computer_guess)

            print("\n\nYOU WIN")

            end = 1


    except:

        print("Wrong input\n")

        end = 1

            
