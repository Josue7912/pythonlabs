'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
a = "hello"
b = "world"
c = "greetings"
print(len(a),",", a)
print(len(b),",", b)
print(len(c),",", c)

list = ("hello", "world", "greetings")
max_len = -1
for ele in list:
    if len(ele) > max_len:
        max_len = len (ele)
        res = ele

print("Maximum length string is : " + res)