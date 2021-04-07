'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
string = "Hello there! I'm learning programming"
num = 0
for letter in string:
  if letter in "aeiouAEIOU":
    num+=1
print(string + str(num))

a_string = "Hello there! I'm learning programming"
a_string = "Abcde"
lowercase = a_string.lower()
vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count

print(vowel_counts)