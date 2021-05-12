'''
Write a script that demonstrates a try/except/else.

'''
try:
    dividend = int(input("Please enter the number to be divided: "))
    divisor = int(input("Please enter the divisor: "))
    result = dividend / divisor
    print(f"The result of {dividend} divided by {divisor} is {result}")
except ZeroDivisionError:
    print("My most sincere apologies, but you can't divide by zero.")
else:
    print("You're great, you are a math specialist :)")