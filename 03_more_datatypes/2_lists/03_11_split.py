'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sentence = "I love Python and want to learn how to create codes with Python and be a Python expert"
print(sentence)
words = sentence.split(" ")


word_counter = {}
for word in words:
    if word in word_counter:
        word_counter[word] +=1
    else:
        word_counter[word] = 1

popular_word = sorted(word_counter, key = word_counter.get, reverse = True)
top = popular_word[:1]

print(f"Most repeated term is: {top}")