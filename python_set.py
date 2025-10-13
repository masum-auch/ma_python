#Python Set Full Concept
##the python set all time mutable but element always immutable.
##Set is the colletion of the unordered items. Each element in the set must be unique & immutable.

# nums = {1, 2, 3, 4}
# set2 = {1, 2, 3, 4}

# print(nums)
# print(type(nums))

# list1 = {'masum', "jibon", 23, 45}
# print(list1)
# print(type(list1))

# set_empty = {} #no work set empty
# print(type(set_empty))

# #this is a empty set
# set_empty1 = set() #it is work set empty
# print(type(set_empty1))

set_empty1 = set("Hello") 
print(set_empty1) # Output: {'h', 'e', 'l', 'o'} (duplicates removed)

# collection = {1, 2, 3, 4, "hello", "world"}
# print(collection)
# print(type(collection))
# print(len(collection))

frutis = {"apple", "banana", "cherry",}
frutis.add("pepe") #new item added
print(frutis) #output {'apple', 'banana', 'cherry', 'pepe'}

numbers = {1, 2, 3}
numbers.update([5, 6, 2, 4])  # 2 is duplicate, ignored
print(numbers)

numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5, 6}

numbers.discard(7)  # No error, even though 7 not present

popped = numbers.pop()
print(popped)  # Output: e.g., 1 (arbitrary)
# print(numbers)  # Output: {2, 4, 5, 6} (one less)

# numbers.clear()
# print(numbers)


num1 = {1, 2, 3, 4}
num2 = {4, 5, 6}

unione_result = num1.union(num2)
print(unione_result)  # Output: {1, 2, 3, 4, 5}

intersection_result = num1.intersection(num2)  # or set_a & set_b
print(intersection_result)  # Output: {3}

diff_result = num1.difference(num2)  # or set_a - set_b
print(diff_result)

sym_diff = num1.symmetric_difference(num2)  # or set_a ^ set_b
print(sym_diff)

print(num1.issubset({1,2,3,4,5}))  # Output: True
print(num1 >= {1,3})

my_set = {1, 2, 3}
copy_set = my_set.copy()
print(len(my_set))  # Output: 3

print(2 in my_set)  # Output: True
print(4 in my_set)  # Output: False

for item in sorted(my_set):  # sorted() for ordered iteration
    print(item)  # Output: 1\n2\n3

fs = frozenset([1, 2, 3])
print(fs)  # Output: frozenset({1, 2, 3})

# Can't modify: fs.add(4)  # Raises AttributeError
print(2 in fs)  # Output: True