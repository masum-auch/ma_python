# count = 0
# while count <6:
#     print("hello")
#     count += 1
# print(count)

# i = 1
# while i <= 10000:
#     print(i)
#     i += 1
# print("Loops End")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("Loops End")

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1 
# print("loop end")

###Practices Question?
##Q-01. Print numbers from 1 to 100.
##Q-02. Print Numbers from 100 to 1.
##Q-03. Print the multiplication table of a number n?
##Q-04. Print the elements of the following list using a loop?
        #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
##Q-05. Search for a nuber x in this tuple using loops
        #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

##Q-01= answer:
# i = 1
# while i <=100:
#     print(i)
#     i += 1
# print("loop ended")

##Q-02= answer:
# i = 100
# while i >=1:
#     print(i)
#     i -= 1
# print("Loops ended")

##Q-03= answer:
# n = int(input("enter your random number: "))
# a = 1
# while a <= 10:
#     print(n*a)
#     a += 1

##Q-04= answer:

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# another example

# heroes  = ["iroman", "thor", "superman", "badman"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1

##Q-05= answer:

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36
# i = 0

# while i < len(nums):
#     if(nums[i] == x):
#         print("Finding The index", i)
#     i += 1


###how to use Break and Continue
# let's try

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 25
# idx = 0

# while idx < len(nums):
#     if(nums[idx] == x):
#         print("Finding the number..", idx)
#         break   #If the loop counts the right number, the loop stops
#     else:
#         print("finding...")
#     idx += 1
# print("Find Loops")

# i = 0

# while i <= 5:
#     if(i == 3): #skip working
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 0
# while i <= 5:
#     if(i%2 == 0):
#         i +=1
#         continue
#     print(i)
#     i += 1

# idx = 0
# while idx <= 10:
#     if(idx%2 != 0):
#         idx += 1
#         continue
#     print(idx)
#     idx += 1