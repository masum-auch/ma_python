# Python OOP Full Concept part
# To map with real world senarius, we started using object in code. This is called objects oriented programming.

# Class & object in python
#class is a blueprint createing object.

#create class
# class Student:
#     name = "Tuhin"

# S1 = Student()
# print(S1.name)
# S2 = Student()
# print(S2.name)

# class Car:
#     color = "blue"
#     brand = "marcedes"
# car2 = Car()
# print(car2.color)
# print(car2.brand)
# car3 = Car()
# print(car3.color)
# print(car3.brand)

# C1 = Car()
# print(C1)

#__init__ function #init is constructor
#All class es hava a function colled --init--(), which is always excuted when the object is being initiated.
#Createing Class

# class Student2:
#     def __init__(self, fullname):
#         self.fullname = fullname

# S3 = Student2("Sahin")
# print(S3.fullname)

# class Student3:
#     def __init__(self, name):
#         self.fullname = name
#         print("adding new student in our database")

# S4 = Student3("Tuhin")
# print(S4.fullname)

# class Student4:
#     def __init__(self, fullname):
#         self.name = fullname
#         print("Add new student, In our School")
#         print("welcome to our school")
# S5 = Student4("Sobuj")
# print(S5.name)

## The self parameter is a reference to the corrent instance of the class and use to access variables that belong to the class.

# S6 = Student4("Payel")
# print(S6.name)

# class Student5:
#     College_name = "ABC College"
#     print(College_name)
#     def __init__(self, fullname, marks):
#         self.fullname = fullname
#         self.marks = marks
#         print("adding new student our school, in kutbari")
#         print(f'welcome to the school')

# S7 = Student5("Fahim", 47)
# print(S7.fullname)
# print(S7.marks)

# class Student5:
#     College_name = "Our College"
#     def __init__(self, name, marks):
#         self.fullname = name
#         self.marks = marks
#         print(f'Welcome to new student. The our College')

# S8 = Student5("karan", 57)
# print(S8.fullname, S8.marks)
# S9 = Student5("Raj", 100)
# print(S9.fullname, S9.marks)
# print(Student5.College_name)

## methods
#method are function that belong to object.
# class Stu:
#     Col_name = "Terminal College"
#     def __init__(self, name, marks):
#         self.fullname = name
#         self.marks = marks
#         print(f'welcome to our College. now start the college')

#     def hello(self):
#         return f"hello {self.fullname}"

# S10 = Stu("Rakib", 73)
# print(S10.marks)
# print(S10.hello())
# print(S10.Col_name)
# S11 = Stu("Roni", 31)
# print(S11.fullname, S11.marks)



class Student8:
    coll_name = "Apna_college"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def Welcome(self):
        return f'Welcome To {self.name}'
    print("welcome to our College, let's start College")

    def get_marks(self):
        return f'Your marks {self.marks}'
    print("Oh Nice, Perpact Score. you a good student.")

S12 = Student8("Tuhin", 88)
print(S12.coll_name)
print(S12.Welcome())
print(S12.get_marks())


#static methods
# methods that don't use the self parameter (wrok at class level)
#class student:
# @staticmethod #decoration
# def college():
#     print("PAKI COLLEGE")
##decorators allow us to wrap another function in order to extend behaviour of the wrapped function without permanently modifying it.   