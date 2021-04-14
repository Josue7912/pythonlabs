'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
start = int(input("Enter low interval number: "))
end = int(input("Enter top interval number: "))
num = 1
while num in range(start, end):
    if num % 5 == 0:
        print(num)
    num += 1