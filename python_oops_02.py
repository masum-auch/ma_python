class Person:
    species = "Homo sapiens"
    
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, I'm {self.name}, {self.age} years old."
    
    def describe_species(self):
        return f"{self.name} is a {self.species}"

person1 = Person("Masum", 19)
print(person1.greet()) 
print(person1.describe_species()) 
print(Person.species) 

class Student9:
    coll_name = "Apna_college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"Welcome to our College, {self.name}! Let's start learning.")

    def Welcome(self):
        return f"Welcome To {self.name}"

    def get_marks(self):
        print("Oh Nice! Perfect Score. You are a good student.")
        return f"Your marks: {self.marks}"


S12 = Student9("Tuhin", 88)
print(S12.coll_name)
print(S12.Welcome())
print(S12.get_marks())   
