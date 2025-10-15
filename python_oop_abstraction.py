# from abc import ABC, abstractmethod

# # Abstract Class
# class ATM(ABC):
#     @abstractmethod
#     def withdraw(self, amount):
#         pass

#     @abstractmethod
#     def check_balance(self):
#         pass

# class CityBankATM(ATM):
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"You withdrew {amount} taka. Remaining balance: {self.balance}")
#         else:
#             print("Insufficient funds!")

#     def check_balance(self):
#         print(f"Your current balance: {self.balance}")

# # Create object
# atm = CityBankATM(10000)

# atm.check_balance()
# atm.withdraw(300)
# atm.check_balance()


# from abc import ABC, abstractmethod

# class Animal(ABC):     # Abstract Class
#     @abstractmethod
#     def sound(self):   # Abstract Method
#         pass

# class Dog(Animal):     # Concrete Class
#     def sound(self):
#         print("Bark!")

# class Cat(Animal):
#     def sound(self):
#         print("Meow!")

# d = Dog()
# c = Cat()
# d.sound()
# c.sound()


# from abc import ABC, abstractmethod

# class Bank(ABC):
#     @abstractmethod
#     def loan(self):
#         pass

# class CityBank(Bank):
#     def loan(self):
#         print("City Bank provides 8% jamela lon loan.")

# class BracBank(Bank):
#     def loan(self):
#         print("Brac Bank provides 7.5% interest loan.")

# b1 = CityBank()
# b2 = BracBank()
# b1.loan()
# b2.loan()


from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        print(f"Area of {self.name}: {3.14 * self.radius * self.radius}")

c = Circle(5)
c.area()



from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started with key ignition.")

class Bike(Vehicle):
    def start(self):
        print("Bike started with self start.")

Car().start()
Bike().start()
