#demo file create
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# file read element

# f = open("demo.txt", "r")
# data = f.read(16)
# print(data)
# f.close()

#the single line count
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()

#new line write and append

# f = open("single.txt", "a")
# f.write("\nAfter that nodejs")
# f.close()


# import os
# os.remove("single.txt")

#qustion_35
#create a new file "practice.txt" using python. add the following data in it.
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\nusing Java\ni like programming in Java") 


#question_36
#WAF that replace all occurrences of "Java" with "Python" in above file.

# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)
# with open("practice.txt", "w") as f:
#     f.write(new_data)

#question_37
#Search if the word "Learning" exists in the file or not?


# def check_for_function():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")

# check_for_function()


#question_38
#write a function to find in which line of the file dose the word "Learning" occur frist.(Print -1 if word not found).

# def check_for_line():
#     word = "Learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
        
#     return -1 

# check_for_line()

#question_39
#from a file containing number separated by comma, print the count of even number?

# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()
#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1

# print(count)