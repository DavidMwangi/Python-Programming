def class_mean(n):

    marks_list = []

    for i in range(1, n+1):

        user_input = int(input("Enter mark: "))

        marks_list.append(user_input)

    total = sum(marks_list)

    mean = total / len(marks_list)

    return mean


while True:

    n =  int(input("Number of students in the class?\n"))

    try:

        if n == 0:

            break

        else:

            output = class_mean(n)

            print ("Class Mean: ",output)

    except:

        print("Invalid Entry\n")

        
