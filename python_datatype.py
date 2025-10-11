#python data types
###Gategory-types
#1. Numeric - integer, float, complex.
#2. Text - string.
#3. Sequence - list, tuple, range
#4. Mapping - dict
#5. Set - set, frozenset
#6. Boolean - bool
#7. Binary - bytes, bytearry, memoryview
#8. None Type - NoneType


##let's try Numeric Types(int, float, complex)
#int(whole numbers(no decimal))
# x = 10
# y = -5
# z = 0

# print(f"x = {x}, type: {type(x)}")
# print(f"y = {y}, type: {type(y)}")
# print(f"z = {z}, type: {type(z)}")

# #arithmetic
# a = 15
# b = 4

# print(f"Addition: {a} + {b} = {a + b}")
# print(f"Subtraction: {a} - {b} = {a - b}")
# print(f"Multiplication: {a} * {b} = {a * b}")
# print(f"Division: {a} / {b} = {a / b}")  # Returns float
# print(f"Floor Division: {a} // {b} = {a // b}")  # Returns integer
# print(f"Modulus: {a} % {b} = {a % b}")
# print(f"Exponentiation: {a} ** {b} = {a ** b}")

# # float(Decimal (floating point) numbers)
# x = 3.14
# y = -2.5
# z = 0.0
# scientific = 1.23e-4  # 0.000123

# print(f"x = {x}, type: {type(x)}")
# print(f"y = {y}, type: {type(y)}")
# print(f"z = {z}, type: {type(z)}")
# print(f"scientific = {scientific}, type: {type(scientific)}")

# #arithmetic with floats
# a = 5.7
# b = 2.3

# print(f"Addition: {a} + {b} = {a + b}")
# print(f"Subtraction: {a} - {b} = {a - b}")
# print(f"Multiplication: {a} * {b} = {a * b}")
# print(f"Division: {a} / {b} = {a / b}")
# print(f"Floor Division: {a} // {b} = {a // b}")
# print(f"Modulus: {a} % {b} = {a % b}")
# print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Complex numbers (a + bj)
z1 = 3 + 4j      # Using 'j' notation
z2 = complex(2, -3)  # Using complex() function
z3 = 5j          # Pure imaginary number
z4 = -2 - 1j     # Negative complex number

print(f"z1 = {z1}, type: {type(z1)}")
print(f"z2 = {z2}, type: {type(z2)}")
print(f"z3 = {z3}, type: {type(z3)}")
print(f"z4 = {z4}, type: {type(z4)}")

# Accessing components
z = 3 - 4j

print(f"Complex number: {z}")
print(f"Real part: {z.real}")
print(f"Imaginary part: {z.imag}")
print(f"Conjugate: {z.conjugate()}")

#Text data types(str)
# String (sequence of characters)
text = "বাংলাদেশ"
print(f"Length: {len(text)}")
print(type(text))

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Case methods (কেস সম্পর্কিত)
text1 = "hello World"
print(text1.upper())       # HELLO WORLD
print(text1.lower())       # hello world
print(text1.title())       # Hello World
print(text1.capitalize())  # Hello world
print(text1.swapcase())    # HELLO wORLD

# Check methods
print("hello".isalpha())   # True
print("123".isdigit())     # True
print("hello123".isalnum()) # True
print("   ".isspace())     # True

sentence = "I love programming in Python"
new_sentence = sentence.replace("Python", "JavaScript")
print(new_sentence)  # I love programming in JavaScript


text = "Python"
print(text[0])      # P
print(text[2:5])    # tho
print(text.upper()) # PYTHON

# Sequence Types(list, tuple, range)
#list(Ordered, changeable, allows duplicates)
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"   # change value
print(fruits)          # ['apple', 'orange', 'mango']

mixed = [1, "two", 3.0] #Can mix data types

#tuple(Ordered, unchangeable, allows duplicates)
colors = ("red", "green", "blue")
print(colors[0])  # red

#range(Sequence r = range(5)
r = range(5)
print(list(r))  # [0, 1, 2, 3, 4]


# Mapping(dict)
# dict(Key-value pairs (unordered, changeable))
student = {
    "name": "Masum", 
    "age": 20, 
    "dept": "Zoology",
    "Roll": 18,
    }
print(student["name"])  # Masum
student["age"] = 21     # change value

#set(set, frozenset)
#set(Unordered, unique elements)
nums = {1, 2, 3, 3, 2}
print(nums)  # {1, 2, 3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union → {1, 2, 3, 4, 5}

#frozenset(Immutable set)

fs = frozenset({1, 2, 3})

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})

print(a | b)  # Union → frozenset({1, 2, 3, 4, 5})
print(a & b)  # Intersection → frozenset({3})
print(a - b)  # Difference → frozenset({1, 2})

# Boolean - bool(True or False)
x = True
y = False
print(5 > 3)  # True

#7. Binary - bytes, bytearry, memoryview

#bytes
b = b"Hello"
print(type(b))  # <class 'bytes'>

#bytearry

#8. None Type - NoneType(Represents absence of a value.)
x = None
print(type(x))  # <class 'NoneType'>

