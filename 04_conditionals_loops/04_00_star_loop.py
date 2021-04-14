'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = int(input("Enter the number of rows"))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range (i+1):
        print("*",end="")
    print()
