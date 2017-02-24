mark = int(input("Please enter your mark to be graded: \n"))

if mark > 100:
           print("Invalid Entry\n")

elif mark >= 90 and mark <= 100:
           print("Grade A\n")

elif mark >= 80 and mark < 90:
           print ("Grade B\n")

elif mark >= 70 and mark < 80:
           print ("Grade C\n")

elif mark >= 60 and mark < 70:
           print ("Grade D\n")

elif mark >=50 and mark < 60:
           print("Grade E\n")

elif mark >=0 and mark < 50:
           print("Fail\n")

else:
           print ("Invalid Entry\n")
