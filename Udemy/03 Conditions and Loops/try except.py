# TRY AND EXCEPT STATEMENTS

my_Age = 23

while True:

    guess = input("Please guess my age:\n")

    try: # The program first checks the try part and if not well initialized or if a mistake occurs, runs the except

        if int(guess) == 23:

            print ("Hurray!! You got my age correct.\n")
            break

        else:

            print ("You got my age wrong, please try again\n")

    except: # Run if an error occurs on the try code

        print ("Something went wrong. You probably typed a none integer value. Check your guess again\n")
