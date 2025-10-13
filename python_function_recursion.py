##Python Function Recursion Full Concept
## When a function calls itself repeatedly

#prints n to 1 backwords.

# def Show(n):
#     if(n == 0): #base case
#         return 
#     print(n)
#     Show(n - 1)
# Show(1)

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)
# show(5)

# def factorial(n):
#     if n == 1:  # Base case
#         return 1
#     return n * factorial(n - 1)  # Recursive call

# print(factorial(5))  # Output: 120

#recursive function = call stack

# def show1(n):
#     if(n == 0):
#         return
#     print(n)
#     show1(n - 1)
#     print("END")

# show1(3)

def mul(a, b):
    if b == 1:
        return a
    else:
        return a + mul(a, b - 1)
print(mul(3, 4))
    

def palin(text):
    if len(text) <= 1:
        print("palindrome")
    else:
        if text[0] == text[-1]:
            palin(text[1:-1])
        else:
            print("not a palindrome")

palin("madam")
palin("malayalam")
palin("python")

# Recursive Fibonacci Function

import time
def fib(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fib(m - 1) + fib(m - 2)
start = time.time()
print(fib(24))
print(time.time() - start)

#Memoization using Recursion
import time
def memo(m, d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m -1, d) + memo(m - 2, d)
        return d[m]
start1 = time.time()
d = {0:1, 1:1}
print(memo(500, d))
print(time.time() - start)
# print(d) #dictionary is the big

def power_set(nums):
    if not nums:  
        return [[]]
    
    first = nums[0]
    rest_subsets = power_set(nums[1:])
    with_first = [[first] + subset for subset in rest_subsets]
    
    return rest_subsets + with_first


print(power_set([1, 2]))
# Output: [[], [2], [1], [1, 2]]



# def timer(func):
#     import time
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         print(f"Time: {time.time() - start}")
#         return result
#     return wrapper

# @timer
# def slow_add(a, b):
#     time.sleep(1)
#     return a + b

# slow_add(1, 2)  # Output: Time: ~1.0