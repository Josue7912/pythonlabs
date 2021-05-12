'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''
items = ['orange', 'apple', 'bike', 'pc', 'car']

def my_enumerate(x):
    for index_i, item in enumerate(items):
        if item == 'car':
            print(f"it's a car! and it's index is {index_i}")

print(my_enumerate(items))
