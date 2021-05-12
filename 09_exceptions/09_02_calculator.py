'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
while True:
    try:
        dividend = int(input("Please enter the number to be divided: "))
        divisor = int(input("Please enter the divisor: "))
        result = dividend / divisor
        print(f"The result of {dividend} divided by {divisor} is {result}")
    except ZeroDivisionError:
        print("My most sincere apologies, but you can't divide by zero.")
    except ValueError:
        print("I am once again asking you to use only digits in your input.")
    except:
        print("Please remain calm...")