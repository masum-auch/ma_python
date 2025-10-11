# This is try now Python conditional statements.
# Demo
"""if-elif-else(syntex)
    if(conditional)
        statements1
    elif(condition2)
        statements2
    else:
        statements
"""

#Let's write some code for traffic.
# light = input("Enter Yor Signal: ")

# if light == "Red":
#     print("Stop the car")
# elif light == "Orange":
#     print("Slow the Car")
# elif light == "Yellow":
#     print("the car stop for 30s")
# else:
#     print("Rood the block") 

# Traffic Control and Jam Detection System

# light1 = input("Enter the traffic light color (Red/Yellow/Green): ").capitalize()
# jam = input("Is there a traffic jam? (yes/no): ").lower()

# if(light1 == "Red"):
#     print("🔴 Stop The Car")
#     if (jam == "yes"):
#         print("Traffic jam detected! Wait until if clears.")
#     else:
#         print("wait for the green light. thank you")
# elif(light1 == "Yellow"):
#     print("🟡Get ready for move")
#     if(jam == "yes"):
#         print("Traffic is heavy. Please move slowly and carefully. thank you")
#     else:
#         print("prepare go to when it truns green light.")
# elif(light1 == "Green"):
#     if jam == "yes":
#         print("🟢 Green light, but traffic jam ahead — drive slowly!")
#     else:
#         print("🟢 Green light — go ahead!")

# else:
#     print("⚠️ Invalid color! Please enter Red, Yellow, or Green.") 

#Grade student based on marks
"""marks >= 90, grade = "A"
    90 > marks >= 80, grade = "B"
    80> marks>= 70, grade = "C"
    70> marks, grade = "D"
"""
# stu = int(input("Enter the student Number: "))
# if(stu >= 90):
#     grade = "A"
# elif(stu >= 80 and stu <90):
#     grade = "B"
# elif(stu >= 70 and stu <80):
#     grade = "C"
# else:
#     grade = "F" 
# print("Your student grade of the total Number : ", grade) #type input

#again python nesting
"""
age = 95
#nesting.
if(age >= 18):
    if(age >= 80):
        print("connot drive")
    else:
        print("Yes can drive")
"""

# Adult = int(input("enter you age here: "))
# if(Adult >= 18):
#     if(Adult >= 80):
#         print("cannot drive the car")
#     else:
#         print("Yes! can drive")
# else:
#     print("not drive car")   

##question
#write a program to check if a number entered by the user if odd or even number?
#answer
# num = int(input("Enter the you Even/Odd number: "))
# if(num % 2== 0):
#     print("Even Number.")
# else:
#     print("No! This is a Odd Number!")

##question
#wirte a program to find the greatest of 3 numbers entered by the user.
#answer:
# a = int(input("Enter your Frist number: "))
# b = int(input("Enter your Secound number: "))
# c = int(input("Enter your trith number: "))
# if(a >= b and a >= c):
#     print("frist number is largest: ", a)
# elif(b >= c):
#     print("second number the largest: ", b)
# else:
#     print("thirh number the largest: ", c)
##question
#write a program to check if a number is a multiple of 7 or not?
#answer
x = int(input("Enter your random number: "))
if(x % 7 == 0): 
    print(f"{x} the multiple of 7")
else:
    print(f"{x} not a multiple")