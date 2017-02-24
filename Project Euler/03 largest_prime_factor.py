start_number = int(input("Enter the first number: \n"))


last_number = int(input("Enter the last number: \n"))

current_number = start_number

while current_number <= last_number:

    current_divisor = 2

    is_prime = True

    while current_divisor < current_number:

        if current_number % current_divisor == 0:

            is_prime = False
            
            break
        
        current_divisor+=1

        if is_prime == True:

            if last_number % current_number == 0:

                print(current_number)
                
            current_number+=1

            """else:

                print("No number found\n")"""

            
