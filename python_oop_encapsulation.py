# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance
    
#     def set_balance(self, amount):
#         if amount >= 0:
#             self._balance = amount
#         else:
#             print("Invalid balance!")

# cus = BankAccount(200)
# print(200)

# class Student:
#     def __init__(self, name, age, id):
#         self.name = name      # Public
#         self._age = age       # Protected
#         self.__id = id        # Private - name mangling

# student = Student("John", 20, "S123")
# print(student._Student__id)

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder  # Public
#         self._account_number = "ACC12345"     # Protected
#         self.__balance = balance              # Private
#         self.__pin = 1234                     # Private
    
#     def display_info(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: ${self.__balance}")

# account = BankAccount("Alice", 1000)
# print(account.account_holder) 
# # print(account.__balance)    
# account.display_info() 


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
    
#     # Getter methods
#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#         return self.__age
    
#     # Setter methods with validation
#     def set_name(self, name):
#         if isinstance(name, str) and len(name) > 0:
#             self.__name = name
#         else:
#             print("Invalid name!")
    
#     def set_age(self, age):
#         if isinstance(age, int) and 0 <= age <= 150:
#             self.__age = age
#         else:
#             print("Invalid age!")

# # Usage
# person = Person("John", 25)
# print(person.get_name())  # John
# # person.set_age(30)       # Valid
# print(person.get_age())
# # person.set_age(200)       # Invalid age! 

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
                    self.__name = value
        else:
            raise ValueError("non=empty string")
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and 0 <= value <= 150:
            self.__age = value
        else:
            raise ValueError("be between 0 and 150")

# Usage
person = Person("Tuhin", 25)
print(person.name)     
person.age = 30          
# person.age = 200      
