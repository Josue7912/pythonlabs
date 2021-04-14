'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
input = "hello world"
li = input.split(" ")
result_list = []
for item in li:
    char_list = []
    for char in item:
        char_list.append(char)
    tupled_list = tuple(char_list)
    result_list.append(tupled_list)
print(result_list)