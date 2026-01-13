# Conditional statement is used for decision making in python by using diffrent block of code

"""
we have 3 types of conditional statement
 if
 if else
 if elif else
 we can have multiple elif condition
 and in these only one condition
"""
a = 10
if a > 5 :
    print("I will do task A")
else:
    print("I will do task B")

money = int(input("Please give me money: "))
if money < 300:
    print("I will have a book")
elif money == 500:
    print("I will have shakspeer collection")
else:
    print("I will have collens collections")