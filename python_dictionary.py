#Python Dictionary Full Concept
##Dictionaries are use to store data values and key: value paris

# dic = {
#     "name": "Masum",
#     "age": 19,
#     "Gender": "male"
# }
# print(dic)

# Student = {
#     "Name" : "Rakib Ahmed",
#     "age" : 22,
#     "Ad Year" : 2023,
#     "passing year" : 2025,
#     "Gender" : "Male",
#     "Group" : "Science"
# }
# print(Student)
# print(type(Student))

# sub_student = {
#     "Name" : "Anwer",
#     "Ad year" : 2021,
#     "college identity" : {
#         "col name" : "X college",
#         "roll" : 30,
#         "group" : "science",
#         "gender" : "male"
#     }
# }
# print(sub_student)

# D3 = {
#     "name" : "Rohit",
#     "College" : "HIT",
#     "Marks" : {
#         "M1" : 56,
#         "DS" : 54,
#         "Eng" : 67
#     }
# }
# # D3["name"] = "Masum"
# # D3["Age"] = 32
# # bl = D3.keys() #return all keys
# # bl =D3.values() #return all value
# # bl = D3.items() #return all keys all value
# new_dict = {
#     "name" : "Tuhin",
#     "roll" : 33,
#     "group" : "mathmethic"
# }
# D3.update(new_dict) #insides the specified item in the dictionary.
# print(D3) 
# print(new_dict.get('name'))       # Output: Tuhin
# print(new_dict.get('salary', 0))  # Output: 0 (default if key missing)

# student = {"name": "Masum", "age": 20}
# extra_info = {"department": "Zoology", "year": 1}

# student.update(extra_info)
# print(student)

#use for on dictionaries

# for key, value in student.items():
#     print(f"{key}: {value}")  # name: Masum, etc.

#nested dictionaries

# nested = {
#     'user': {'name': 'Sahin', 'age': 30},
#     'address': {'city': 'NY', 'zip': 10001}
# }
# print(nested['user']['name'])  # Sahin

# names = ['Sohidul', 'Tultul']
# upper = {name: name.upper() for name in names}  # {'Sohidul': 'SOHIDUL', 'Tultul': 'TULTUL'}

# print(upper)

# from collections import OrderedDict
# od = OrderedDict([('a', 1), ('b', 2)])
# print(od)  # OrderedDict([('a', 1), ('b', 2)])


# keys = ['apple', 'banana', 'cherry']
# result = dict.fromkeys(keys)
# print(result) # Output: {'apple': None, 'banana': None, 'cherry': None}

# Create
data = {'fruits': ['apple', 'banana'], 'count': 2}

# Modify
data['vegetables'] = ['carrot']
data.update({'count': 3})

# Iterate
for k, v in data.items():
    print(f"{k}: {v}")

# Output:
# fruits: ['apple', 'banana']
# count: 3
# vegetables: ['carrot'] 