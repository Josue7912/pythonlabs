'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
num = 2
num_float = float(num)
print(num_float)
type(num_float)
num_int = int(num)
print(num_int)
type(num_int)
x = 2 // 1.5
y = 3
z = 6
multip = y * z
print(multip)