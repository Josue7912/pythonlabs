'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

num = int(input("Enter your number:"))

if(num%3==0):
    print("{} is divisible by 3".format(num))
else:
    print("{} is not divisible by 3".format(num))