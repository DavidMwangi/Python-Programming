def get_grade(student, name_list, course_list, grade_list):

    i = name_list.index(student)
    
    grade = grade_list[i]
    
    course = course_list[i]

    return (course, grade)
    

names = ['David', 'Kevin', 'Alice']

courses = ['CS', 'Arts', 'Medicine']

grades = [90, 80, 85]

student = input("Enter student name: ")

print(get_grade(student, names, courses, grades))