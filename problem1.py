 '''Create a program that asks the user to enter their name and their age.
 Print out a message that will tell them the year that they will turn 95 years old.'''

a=input("Enter your name = ")
b=int(input("Enter your present age  = "))

c= 95-b
d=2019 + c
print("========================================")
print("Your name is a = ", a)
print("Your present age is a = ", b)
print("this year {} to 95 year old ".format(d))
print("========================================")
