'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

start, end = 1, 100

for num in range(start, end):
    if num % 2 != 0:
        print(num, end = " ")
