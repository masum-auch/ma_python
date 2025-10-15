# class User:

#     def login(self):
#         print("Login")

#     def reg(self):
#         print("Register")

# class student(User):

#     def enroll(self):
#         print("student Enroll")

#     def review(self):
#         print("student reviews")

# stu = student()
# stu.login()
# stu.reg()
# stu.enroll()
# stu.review()


# class Phone:
#     def __init__(self, name, brand, camara):
#         print("Inside Phone Constractor")
#         self.name = name
#         self.brand = brand
#         self.camara = camara

# class SmartPhone(Phone):
#     pass

# ph = SmartPhone("Iphone", "Apple", "18mpx")
# print(ph.name)


# class Phone:
#     def __init__(self, name, brand, camara):
#         print("Inside Phone Constractor")
#         self.name = name
#         self.brand = brand
#         self.camara = camara

#     def buy(self):
#         print("Buying a Phone")

# class SmartPhone(Phone):
    
#     def buy(self):
#         print("Buing a SmartPhone")

# ph = SmartPhone("Iphone", "Apple", "18mpx")
# print(ph.name)
# ph.buy()

# class Parant:
#     def __init__(self, num):
#         self.__num = num

#     def get_num(self):
#         return self.__num
    
# class Child(Parant):

#     def show(self):
#         print("your main balance")

# s1 = Child(233)
# print(s1.get_num())
# s1.show()


# #super method

# class Phone:
#     def __init__(self, name, brand, price):
#         print("Inside Phone Constractor")
#         self.name = name
#         self.brand = brand
#         self.price = price

#     def buy(sef):
#         print("Buing the Phone")

# class SmartPhone(Phone):

#     def buy(self):
#         print("Buing the a SmartPhone")
#         super().buy()

# bu = SmartPhone("iphone", "apple", 120000)
# print(bu.name)
# print(bu.buy())

# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         super().__init__(price, brand, camera)
#         print("thsi code a fast work")
#         self.os = os
#         self.ram = ram
#         print("Inside smartphone constructor")

# s = SmartPhone(20000, "Samsung", 12, "Android", 2)

# print(s.os)
# print(s.brand)

class Product:
    def review(self):
        print("Review the phone")


class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buing the phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(20000, "Samsung", 1)

p = Phone(1000, "apple", 1)
print(p.brand)

s.buy()
p.review()
