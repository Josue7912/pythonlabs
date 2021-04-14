'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
list = [10, 25, 3, 6 , 9, 99, 85, 21, 18, 60]
list.sort()
print("Largest number is:", list[-1])

product = 1
for num in list:
    product = product * num
print("Product is:", product)