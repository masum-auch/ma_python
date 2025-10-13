##Let's practice Question
##1. write a function to print the lengh of a list(list is the parameter)
##2. write a fucncton to print the element of a list in a single line(")
##3. write a function to converd to USD to INR.
##4. write a function to fine the factorial of n.

##question_01
list1 = ["Masum", "tuhin", "AK"]
num = [1, 2, 3, 4, 5]

def item_list(my_list):
    print(len(my_list))  # list1 এর length
    print(len(num))      # num এর length

item_list(list1)

##question_02

list2 = ["Masum", "tuhin", "AK"]
num2 = [1, 2, 3, 4, 5]

def sing_line(my_list2):
    for item in my_list2:
        print(item, end=" ")
    print()
sing_line(list2)


##qustion_05
def converter(usd_val):
    inn_val = usd_val * 83
    print(usd_val, "USD =", inn_val, "INR")

converter(74)

##qustion_04
def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {n} is {fact}")

cal_fact(8)
 





 

