#python_loops toturial topic_02

# nums = [1, 3, 8, 18, 38, 57, 39]
# for el in nums:
#     print(el)


# name = "apnacollage"
# for ele in name:
#     print(ele)
# else:
#     print("End")

# fullname = "masumkhan"
# for full in fullname:
#     if(full == 'k'):
#         print("K Found")
#         break
#     print(full)
# else:
#     print("END")


##using for

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for ele in nums:
#     print(ele)


# nums1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 1
# X = 36
# for element in nums1:
#     if(element == X):
#         print("Search number found..", idx)
#     idx += 1

#comcompare this code
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36
# i = 0

# while i < len(nums):
#     if(nums[i] == x):
#         print("Finding The index", i)
#     i += 1

##range() ,, range() == range(start, stop, step?) value let's try

# for i in range(10): #stop useing
#     print(i)

# for i in range(0, 5): #start and stop using
#     print(i)

# for i in range(0, 10, 2): #start, stop and step using
#     print(i)

### Question practice
##print numbers from 1 to 100.
##print numbers from 100 to 1.
##print the multiplication table of a number n.
##Write a program find the sum of first n numbers.(using while)
##Write a program find the factorial of first n numbers.(using for)

##Q-06 = answer:
# for i in range(1, 101):
#     print(i)

##Q-07 = answer:
# for i in range(101, 0, -1):
#     print(i) 

##Q-08 = answer:
# n = int(input("enter you number: "))
# for i in range(1, 11):
#     print(i * n)

##Q-08 = answer:
# n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum number", sum)

##Q-09 = answer:
n = 3
fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial number: ", fact)



