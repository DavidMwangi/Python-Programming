#This function calculates and prints out square roots

def sqrt(input_number):
	
	square_root = input_number / 2

	accuracy = 0.001

	while abs(input_number-(square_root**2)) > accuracy:
	
		square_root = (square_root + (input_number/square_root))/2

	return square_root

status = 1

while status == 1:

	try:
		user_input = float(input("Enter your number: \n"))

		sqroot = sqrt(user_input)

		print ("The square root of", user_input, "is", sqroot)
	
		status =1


	except:
	
		status = 0
