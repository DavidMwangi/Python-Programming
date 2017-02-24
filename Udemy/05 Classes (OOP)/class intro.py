class Students: #Intializing a class Students

    def __init__(self,name, age,grade): #Defining the parameters for each instance

        #Setting attributes for each object of the class
        self.name=name
        self.age=age
        self.grade=grade

student1=Students("David", 23, "4th") #Instance of the class Student

print(student1.name)
print(student1.age)
print(student1.grade)
 
