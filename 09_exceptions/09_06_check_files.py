'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

while True:

    try:
        file_name = input("Please input your file name: ")
        with open(file_name, "r") as fin:
            content = fin.readlines()
            num1 = int(content[0])

        num2 = int(input("Please input a number to do magic maths: "))
        result = num1 * num2
        print(f"The multiplication of {num1} per {num2} is equals to {result}")
    except ValueError:
        print("Please input an integer, try again :)")
    except IOError:
        print("Wrong file name, Try again")
    else:
        break


