"""
In this exercise, you will create a Python class named Student to represent students. 
The class should have the following attributes and methods:

Attributes:

name: instance variable
age: instance variable
courses: instance variable
available_courses: class variable -> possible values ["English", "Urdu", "Physics", "Math", "Chemistry"]

Methods:

display_info(): An instance method that displays the student's name and age.
enroll(): An instance method that allows a student to enroll in a course by adding it to their list of enrolled courses.
list_courses(): An instance method that displays all the courses that student is enrolled
list_available_courses(): An instance method that display all the avaiable courses


1. Create three instances of the Student class with different names and ages.

2. enroll the students in courses by calling the enroll method.
make sure student should only enroll in the course that are listing in available course
i.e if user input the course "Islamyat" then program should not allow it

3. call list_courses
4. call list_available_courses
"""


class Student:
    available_courses: []
    def __init__(self,name,age,courses):
        self.name=name 
        self.age=age
        self.courses=courses
        Student.available_courses=["English", "Urdu", "Physics", "Math", "Chemistry"]
    def display_info(self):
        return "Student name is {self.name} and age is "+str(self.age)
    def list_courses(self):
        return self.courses
    def enroll(self,courseName):
        print(any(ele in courseName for ele in self.courses))
        if(any(ele in courseName for ele in Student.available_courses)):
            self.courses.append(courseName)
            return self.courses
        else:
            return print("Course is not available")
    def list_available_courses(self):
        return Student.available_courses


# studentOne=Student("Hurmat",23,["English"])
# print(studentOne.__dict__)
# print(studentOne.display_info())
# print(studentOne.list_courses())
# print(studentOne.enroll("Urdu"))
# print(Student.available_courses)
# studentTwo=Student("hurrrrmatt",23,["Physics"])
# print(studentTwo.__dict__)
# print(studentTwo.display_info())
# print(studentTwo.list_courses())
# print(studentTwo.enroll("English"))
# print(Student.available_courses)
# studentThree=Student("hurrrrmatt",23,["Physics"])
# print(studentThree.__dict__)
# print(studentThree.display_info())
# print(studentThree.list_courses())
# print(studentThree.enroll("Math"))
# print(Student.available_courses)