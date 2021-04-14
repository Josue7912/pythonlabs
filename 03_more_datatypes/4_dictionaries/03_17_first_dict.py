'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
n = int(input("Input a number "))
d = dict()

for x in range(1,n*1):
    d[x]=x*x

print(d)

