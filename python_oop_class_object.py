#class is a blueprint.
##class basic Structure
#color = "blue" #data
#model = "sport" #data

# def calculateAvgSpeed(km, time)
        #Somecode
# class ATM:
#     def __init__(self):

#         self.pin = ""
#         self.balance = 0

#         self.menu()

#     def menu(self):
#             user_input = input("""
#                 Hello, how would you like to proceed? 
#                     1. Enter 1. to create a pin
#                     2. Enter 2. to deposit
#                     3. Enter 3. to withdrow
#                     4. Enter 4. to check balance
#                     5. Enter 5. to exit
# Your choice: """)
            
#             if user_input == "1":
#                 self.create_pin()
#             elif user_input == "2":
#                 self.user_deposit()
#             elif user_input == "3":
#                 self.user_withdrow()
#             elif user_input == "4":
#                 self.check_balance()
#             elif user_input == "5":
#                 print("Exit Ber kor naile churi kore pelbi, Sabdhan CC camara dara niyntritho")
#             else:
#                 print("No Click")
    
#     def create_pin(self):
#         self.pin = input("Enter Your New Pin: ")
#         print(f'Print Create Successful')
    
#     def user_deposit(self):
#         entered_pin = input("Enter your created pin: ")
#         if entered_pin == self.pin:
#             amount = int(input("Enter your deposit Amount: "))    
#             self.balance += amount
#             print("You deposit successfully")
#         else:
#             print("Pin Invild! Try Again Now")

#     def user_withdrow(self):
#         entered_pin = input("Enter your create pin: ")
#         if entered_pin == self.pin:
#             amount = int(input("Enter your withdrow amount: "))
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f'Your balance Withdrow Now')
#             else:
#                 print("Taka Nai")
#         else:
#             print("Pin Jamela! try again")

#     def check_balance(self):
#         entered_pin = input("Enter your create pin: ")
#         if entered_pin == self.pin:
#             print(self.balance)
#         else:
#             print("pin Incorrect")

# A = ATM() #this object
# A.menu()
 


# class Animal:  # Base class
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."

# class Dog(Animal):  # Derived class inherits from Animal
#     def speak(self):  # Override the method
#         return f"{self.name} says Woof!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# # Creating objects
# my_dog = Dog("Buddy") #this is a object 
# my_cat = Cat("Whiskers") # this a object

# print(my_dog.speak())  # Output: Buddy says Woof!
# print(my_cat.speak())  # Output: Whiskers says Meow!


class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)

    def __add__(self,other):

        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num,temp_den)

    def __sub__(self,other):

        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num,temp_den)

    def __mul__(self,other):

        temp_num = self.num * other.num
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num,temp_den)

    def __truediv__(self,other):

        temp_num = self.num * other.den
        temp_den = self.den * other.num

        return "{}/{}".format(temp_num,temp_den)
    
Fa = Fraction(3, 4) #object
print(Fa)

