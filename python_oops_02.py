# class Person:
#     species = "Homo sapiens"
    
#     def __init__(self, name, age):  # Constructor
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         return f"Hi, I'm {self.name}, {self.age} years old."
    
#     def describe_species(self):
#         return f"{self.name} is a {self.species}"

# person1 = Person("Masum", 19)
# print(person1.greet()) 
# print(person1.describe_species()) 
# print(Person.species) 

# class Student9:
#     coll_name = "Apna_college"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print(f"Welcome to our College, {self.name}! Let's start learning.")

#     def Welcome(self):
#         return f"Welcome To {self.name}"

#     def get_marks(self):
#         print("Oh Nice! Perfect Score. You are a good student.")
#         return f"Your marks: {self.marks}"


# S12 = Student9("Tuhin", 68)
# print(S12.coll_name)
# print(S12.Welcome())
# print(S12.get_marks())   


# class Customer:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# def greet(customar):
#         if customar.gender == "Male":
#             print("Hello", customar.name, "Sir")
#         else:
#             print("Hello", customar.name, "Ma'am")

#         cust2 = Customer("NItish", "Male")
#         return cust2




# cust = Customer("Ankita", "Female")
# new_cust = greet(cust)
# print(new_cust.name)

# class Customer2:
#     def __init__(self, name):
#         self.name = name

# def greet2(customer):
#     print(id(customer))
#     customer.name = "Nitish"
#     print(customer.name)

# cust2 = Customer2("Ankita")
# # print(id(cust2))
# greet2(cust2)
# print(cust2.name)

# def change(L):
#     print(id(L))
#     L.append(5)
#     print(id(L))

# L1 = [1, 2, 3, 4]
# print(id(L1))
# print(L1)

# change(L1)
# print(L1)

class Customer3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cust3(sefl):
        print(f"hello I'm {sefl.name} and my age {sefl.age}")
L1 = Customer3("Tuhin", 19)
L2 = Customer3("Orin", 23)
L3 = Customer3("Nopur", 24)

L = [L1, L2, L3]

for i in L:
    i.cust3() 

