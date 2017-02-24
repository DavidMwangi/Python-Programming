total = 50 #Global variable decalred outside a function
# Global variables can be called anywhere within the program

def multiply(a,b):

    total = a*b #Local variable declared within a function
    # Local variables can only be called within declared function
    return total


print(multiply(34,67))

print (total)
