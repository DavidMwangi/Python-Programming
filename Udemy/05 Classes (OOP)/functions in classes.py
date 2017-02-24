class Students: #Intializing a class Students

    def __init__(self,name, age,year): #Defining the parameters for each instance

        #Setting attributes for each object of the class
        self.name=name
        self.age=age
        self.year=year

    def displayStudent(self):

        return("Student name is " + self.name + " and the age is " + str(self.age) + " and is in " + str(self.year) + " year")

student1=Students("David", 23, "4th") #Instance of the class Student

print(student1.displayStudent())
 
