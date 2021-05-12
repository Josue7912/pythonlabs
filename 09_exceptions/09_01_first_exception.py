'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''
try:
    list_ = ["hello world!"]
    print(list_[1])
except IndexError:
    print("It is an IndexError, change the number to select one item from the list... Try again")