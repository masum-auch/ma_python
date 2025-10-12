#Python tuple full concept
### A built-in data type that let's us create immutable sequence of values.

# tup = (1,) # Comma is must be required
# print(type(tup))
# print(tup)

# tup = (2, 1, 3, 1)
# print(tup)
# print(type(tup))
# print(tup[0])

# # tup[0] = 5 # not allow in tuple

# tup2 = (1, 2, 3, 4, 5)
# print(tup2[1:3])
# print(tup2[0:4])
# fruits1 = ('apple', 'banana', 'cherry', 'date')
# print("Length:", len(fruits1))
# print("First fruit:", fruits1[0])
# print("Last fruit:", fruits1[-1])
# print("Slice (1 to 3):", fruits1[1:3])
# print("Every second item:", fruits1[::2])

# mixed = (1, 'hello', 3.14)
# print(mixed)
# print(type(mixed))

# # Basic creation
# my_tuple = (1, 'apple', 3.14)
# print("Original tuple:", my_tuple)

# # Empty and single-element tuples
# empty_tuple = ()
# single_tuple = (42,)  # Note the comma!
# print("Empty:", empty_tuple)
# print("Single:", single_tuple)

# # Using constructor
# from_list = tuple([10, 20, 30])
# print("From list:", from_list)

# # Concatenation and repetition
# combined = my_tuple + (4, 'banana')
# repeated = my_tuple * 2
# print("Concatenated:", combined)
# print("Repeated:", repeated)

# Create a sample tuple
my_tuple = (1, 2, 2, 3, 4, 2)

# count method
count_two = my_tuple.count(2)
print("Number of 2's:", count_two)

# index method
index_three = my_tuple.index(3)
print("Index of 3:", index_three)

# Another example for count with non-existing
count_five = my_tuple.count(5)
print("Number of 5's:", count_five)

# index with non-existing (will raise ValueError, but catch it)
try:
    index_five = my_tuple.index(5)
except ValueError as e:
    print("Error for index(5):", str(e))
