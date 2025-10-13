##Python Function full concept
#Block of statement that perform a Specifice task.

# def cale_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum
# cale_sum(3, 5)
# cale_sum(5, 5)

# def cale_avg(a, b, c):
#     sum = a + b + c
#     avg = sum/3
#     print(avg)
#     return avg  
# cale_avg(3, 5, 7)

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

X = is_even(8)
print(X) 

# Argument
# 1. Default Argument
def default(a = 1, b = 2):
    sum = a + b
    print(sum)
    return sum

default() #

#2. Positional Argument
def positional(x = 2, y = 9):
    multi = x * y
    print(multi)

positional(2, 2)

#3. Keyword Argument
def keyword(c = 3, d = 4):
    key_word = c - d
    print(key_word)
keyword(d=3, c=2)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC

#4. Arbitrary Argument
def flexi(*number):
    product = 1
    print(number)
    for i in number:
        product = product * i
    print(product)
flexi(1, 2, 3, 4)

def introduce(name, age):
    print(f"Hi, I'm {name} and I'm {age} years old.")

introduce("Alice", 25)          # Positional: Output: Hi, I'm Alice and I'm 25 years old.
introduce(age=30, name="Bob")   # Keyword: Output: Hi, I'm Bob and I'm 30 years old.

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b  # Returns float

result = divide(10, 2)
print(result)  # Output: 5.0

def get_coordinates():
    return 10, 20  # Tuple

x, y = get_coordinates()
print(x, y)  # Output: 10 20

# Goble function
def g(x):
    def h(x):
        x = x + 1
        print("in h(X): x = ", x)
    x = x + 1
    print("in g(x): x = ", x)
    h(x)
    return x
x = 3
z = g(x)
print("in main program scope: x = ", x)
print("in main program scope: z = ", z)