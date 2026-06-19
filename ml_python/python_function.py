# def greet():
#     print("Hello, Worlld!")

# greet()
# print("This is a test message.")



# def MyFunction(name):
#     print(f"Hello, {name}!")

# MyFunction("Alice")


def MyFunction(name):
    return f'Hello, {name}!'


greeting = MyFunction("Alice")
print(greeting)

student_name = ['Ak', 'Tuhin', 'Sakib', 'Rafi']

def find_student(name):
    for student in student_name:
        if student == name:
            return f"{name} is found in the list."
    else:
        return f"{name} is not found in the list."

found_student= find_student("Tuhin")
print(found_student)