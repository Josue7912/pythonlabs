'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

gen = (x for x in range(15000))

for x in gen:
    if x % 1111 == 0:
        print(x)
