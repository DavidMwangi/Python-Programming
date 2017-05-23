def bmi(weight, height):
	bmi = weight/pow(height,2)
	return (bmi)

while True:

	weight = float(input('Enter your current weight in kgs\n>'))

	height = float(input('Enter your current height in meters\n>'))

	if weight == 0 or height == 0:

		break

	else:

		print(bmi(weight,height))
