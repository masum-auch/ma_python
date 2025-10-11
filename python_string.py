#string: string is data type that stores a sequence of characters.
#Baisic operations,
#.concatenation.
#   "hello" + "world" --> "hello world"
#.length of str
#   len(str)



# name = "masumkhan"
# print(name)
# print(type(name))

# ##Each character in a String has an index (position)
# fullname= "TheMasumKhan"
# print(name[0])
# print(name[-1])

# ## A specific part of a string can be cut off.
# name = "Masum Khan"
# print(name[0:5])
# print(name[6: ])

# ## Two strings can be concatenated using the + operator.
# first = "Masum"
# last = "Khan"
# full = first + " " + last
# print(full)


## String Methods let's try

# text = "hellow world"

# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.casefold()) #casefold() একটি string method যা মূলত স্ট্রিংকে completely lowercase-এ রূপান্তর করে.
# print(text.count('o'))
# print("hello.txt".endswith(".ete"))

# text2 = "TAKA"
# print(text2.center(10, "_"))


###Practices Question?
##Q-01. write a program to input user's first name & print it's length.
##Q-02. write a program to find the occurrence of '$' in a string.

##Q-01= answer:
# first = input("Enter your First Name: ")
# print(first)
# print(len(first))

##Q-02= answer:
# text = input("Enter a string: ")
# count = text.count('$')
# print("The character '$' occurred", count, "times.")


# text = input("Enter a string: ")
# count = 0

# for char in text:
#     if char.isdigit():
#         count += 1

# print("Number of digits in the string:", count)   

# 1. Password strength checker
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password too short"
    elif password.isalpha():
        return "Weak: Only letters"
    elif password.isdigit():
        return "Weak: Only numbers"
    else:
        return "Strong: Good password"

print(check_password_strength("abc123"))    # Weak
print(check_password_strength("StrongPass123"))  # Strong

# 2. Text analyzer
def analyze_text(text):
    words = text.split()
    characters = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    
    return {
        'words': len(words),
        'characters': characters,
        'sentences': sentences,
        'avg_word_length': round(characters / len(words), 2) if words else 0
    }

sample = "Hello world. This is Python!"
print(analyze_text(sample)) 


