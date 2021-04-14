'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
user_input = "hello"

all_freq = {}
for i in user_input:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(str(all_freq))