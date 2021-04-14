'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
n = int(input("Enter your number: "))
num = 1
while num in range(1, 1000000000):
    if num == n:
        print(num)
        break
    num += 1