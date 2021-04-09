sentence = "I love to work with dictionaries!"
lower_count = sum(map(str.islower, sentence))
upper_count = sum(map(str.isupper, sentence))
number_letters = len(sentence) - sentence.count(" ")
symbols = sentence.count("!")
print(f"Lower case: {lower_count}")
print(f"Upper case: {upper_count}")
print(f"Punctuation: {symbols}")
print(f"Total chars: {number_letters}")