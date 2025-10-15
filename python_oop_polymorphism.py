class Geometry:
    def area(self, a,b = 0):
        if b == 0:
            print("cicle", 3.1416*a*a)
        else:
            print("Rect", a*a)

obj = Geometry()
obj.area(4)
obj.area(4,5)



# Method Overriding

# class Animal:
#     def sound(self):
#         return "Some generic animal sound"
    
#     def move(self):
#         return "Animal is moving"

# class Dog(Animal):
#     def sound(self):  
#         return "Bark"
    
#     def move(self):   # Method Overriding
#         return "Dog is running"

# class Cat(Animal):
#     def sound(self):  # Method Overriding
#         return "Meow"
    
#     def move(self):   # Method Overriding
#         return "Cat is jumping"

# # Polymorphism in action
# def make_animal_sound(animal):
#     return animal.sound()

# def make_animal_move(animal):
#     return animal.move()

# # Testing
# dog = Dog()
# cat = Cat()

# print(make_animal_sound(dog))  # Output: Bark
# print(make_animal_sound(cat))  # Output: Meow

# print(make_animal_move(dog))   # Output: Dog is running
# print(make_animal_move(cat))   # Output: Cat is jumping


class PaymentMethod:
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class Bitcoin(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing ${amount} via Bitcoin"

class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []
    
    def add_payment_method(self, method):
        self.payment_methods.append(method)
    
    def process_all_payments(self, amount):
        results = []
        for method in self.payment_methods:
            results.append(method.process_payment(amount))
        return results

# Usage
processor = PaymentProcessor()
processor.add_payment_method(CreditCard())
processor.add_payment_method(PayPal())
processor.add_payment_method(Bitcoin())

results = processor.process_all_payments(100)
for result in results:
    print(result)