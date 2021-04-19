'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
def square(x):
    y = a * a
    return y

def cube(x):
    y = square(x) * a
    return y

def sum_of_multiplication(x):
    y = cube(x) * a
    return y

a = 5
result = sum_of_multiplication(a)
print(result)