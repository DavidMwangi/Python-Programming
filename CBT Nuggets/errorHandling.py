"""

Error Handling skill is one of the basic python skills every python programmer should have.
Other than letting computers handle errors for us, having control of how our code handles
the errors that occur is pretty sleek.
One of the basic ways to do that is havint the try-except clause.
However on this file, I am going to be catching specific error off the code.
Check it out

"""

while True:

    err = "There was an error"

    try:

        print("\nLet us evaluate the equation")
        print("To terminate program, enter 0")

        prompt = '>'

        x = float(input(prompt))
        y = float(input(prompt))

        if x == 0 or y == 0:

            break

        ans =  (x/2) / (x-y)


    except ZeroDivisionError as e:

        #This clause raises division by zero errors

        print (err)
        print("You keyed in values that caused a division by zero error")

    except NameError as e:

        #This clause raise name errors

        print (err)
        print ("You keyed in a text value. Only number values are expected")

    except Exception as e:

        #This clause raise any other error not caught by the other two clauses

        print (err)
        print ("Error message: ", str(e))

    else:

        #The else clause always comes after all the except clauses
        #This clause runs the clean code
        #The code that should run if no errors occur
        #In this case:

        print ("Equation evaluation = ", ans)

    finally:

        #Runs no matter what. Whether an error occurs or not
        #Best place to place clean up code
        #Releasing handles and cloing documents

        print ("Clean up code goes here")
