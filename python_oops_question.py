##Python OOPS Question
##question
#01. Create student class that take a name & marks at 3 object as argument in constructor. Then create a method to print the average.

##question_01 - solve
# class Student:
#     College_name = "jamela college"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_avrg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         return f'Hi {self.name} my average number {sum/3}'

# S = Student("Tuhin", [98, 96, 92])
# print(S.College_name)
# print(S.get_avrg())

#02. Define a circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculate the area of the circle. Define a parameter() method of the class which allow you to calculate the parameter of the circle.
##question_02 - solve
# class circle:
#     def __init__(self, redius):
#         self.redius = redius

#     def area(self):
#         return (22/7) * self.redius **2
    
#     def paramiter(self):
#         return (22/7) * self.redius
    
# c1 = circle(21)
# print(c1.area())
# print(c1.paramiter())


#03. Define a employee class with attibute role, department & salary. This class also a ShowDetails() method. create a engineer class that entherits propertice form employee additional attributes: name & age & role
class Employee:
    def __init__(self, department, salary, role):
        self.department = department
        self.salary = salary
        self.role = role

    def ShowDetails(self):
        print(f'Department = {self.department}')
        print(f'Role =  {self.role}')
        print(f'Salary = {self.salary}')

class Engineer(Employee):
    def __init__(self, name, age, department, salary, role):
        super().__init__(department, salary, role)
        self.name = name
        self.age = age

    def ShowDetails(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        super().ShowDetails()

eni = Engineer("Masum", 19, "IT", 75000, "Software Engineer")
eni.ShowDetails()


#04. create a class called order which Stores item & its price. Use Dunder function __get__ to canvey that: order1> order2 price of order1> price of order2.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price
    
ord1 = Order("Chips", 20)
ord2 = Order("tea", 13)
print(ord1 > ord2)
