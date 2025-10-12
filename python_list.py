#python list full concept
#1. what is a list
#2. list Vs array
#3. create
#4. access
#5. Edit
#6. Add
#7. delete
#8. operations

#1. A built-in data type stores a set of values. It can store elements.

# marks = [73, 51, 89, 42, 10]
# print(marks)
# print(type(marks))

# fruits = ['apple', 'banana', 'cherry']
# fruits[1] = 'blueberry'
# fruits = ['apple', 'blueberry', 'cherry']

# marks1 = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks1)  #output
# print(len(marks1)) #5
# print(marks1[0]) #frist number count
# print(marks1[0]) #second number count

# Student = ["karan", 95.4, 17, "dellhi", True]
# print(Student)

# #4. Access list and changeable
# student2 = ["karan",94.2, 17, "mumbai"]

# student2[0] = "Arjun"
# student2[2] = 26
# print(student2)

#list Slicing
# list_marks = [87, 64, 33, 95, 76]
# print(list_marks[1:4])
# print(list_marks[:4])
# print(list_marks[1:])
# print(list_marks[1: len(list_marks)])
# print(list_marks[-4:-1]) #right and laft
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3]
print(numbers[:3])     # [0, 1, 2] (from start)
print(numbers[::2])    # [0, 2, 4] (every second element)
print(numbers[::-1])   # [5, 4, 3, 2, 1] (reverse)

#list method
# list_marks1 = [2, 1, 3, "hello", "tumi"]
# list_marks1.append(4) # New Item added
# list_marks1.reverse() # laft to right
# list_marks1.pop() # always delete the last item
# list_marks1.clear() # This is list empty
# list_marks1.insert(1, 9) #
# list_marks1.extend([4, 5, 6]) #multiple item add
# list_marks1.remove(1) # selete on delete
# print(list_marks1)

# marks1 = [94.4, 87.5, 95.2, 66.4, 45.1]
# marks2 = [23, 54, 92, 87, 55, 20, 30]
# marks3= [[[23, 54], 92], [87, [55, 20], 30]]
# print(marks3[1][1][0])
# print(marks3[0][0][1])

# marks4 = list("masum")
# print(marks4)

##list function
# list6 = [2, 3, 5, 8, 4, 0]
# print(len(list6))
# print(min(list6))
# print(max(list6))
# print(sorted(list6))
# li = sorted(list6, reverse= True) # not a create permanent. just one time create list
# print(li)

# text = "how are you?"
# result = text.title()
# print(result)

# Title Case a String Without title()
# sample = "how are you?"
# sample.split()
# L = []
# for i in sample.split():
#     L.append(i.capitalize())
# print(L)
# print(" ".join(L))

# sample= "masum@gmail.com"
# print(sample[:sample.find("@")])


# a = [1, 1, 3, 3, 2, 2, 5, 5]
# b = [3, 2, 5]
# unique_item = list(set(a + b))
# print(unique_item)

# for use
# L = []
# for i in a:
#     if i not in L:
#         L.append(i)
# print(L)

##quetion
# write a program to ask the user id enter name of their 3 favorite movies. store them in a list
# movies = []
# movies.append(input("Enter your frist movies: "))
# movies.append(input("Enter your second movies: "))
# movies.append(input("Enter your thried movies: "))
# print(movies)

##question
#write a program to check if a list contains a palindrome of elements.(Hint: use copy() method)
# list3 = [1, 2, 3, 4]
# list4 = ["m", "a", "s", "u", "m"]
# copy_list = list3.copy()
# copy_list.reverse()
# if(copy_list == list3):
#     print("palindrome")
# else:
#     print("Not a Palindrome")