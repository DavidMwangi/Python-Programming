class Students: #Intializing a class Students

    def __init__(self,name, age,year): #Defining the parameters for each instance

        #Setting attributes for each object of the class
        self.name=name
        self.age=age
        self.year=year

    def displayStudent(self):

        return("Student name is " + self.name + " and the age is " + str(self.age) + " and is in " + str(self.year) + " year")

student1=Students("David", 23, "4th") #Instance of the class Student
student2=Students("Kevin", 21, "2th")

print(student1.displayStudent())

print(hasattr(student1, "age"))

print(hasattr(student2, "height"))


setattr(student2, "height", 150)#Sets an attrbute to our class that has not already been declared

print(hasattr(student2, "height"))

print(getattr(student2, "height"))


delattr(student2, "height")#Deletes an attribute from a class


print(hasattr(student2, "height"))
  
