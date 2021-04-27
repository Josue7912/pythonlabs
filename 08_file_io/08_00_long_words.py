'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
words = []
with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

charac_list = []
for w in words:
    if len(w) - w.count(" ") >= 20:
        charac_list.append(w)

print(charac_list)