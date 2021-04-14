'''
Print out every prime number between 1 and 100.

'''
start, end = 1, 100
for num in range(start, end):
    for i in range (2, num):
        if(num % i==0):
            break
        else:
            print(num)
            break