'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
li_1 = [2, 10, 45, 5, 13, 30, 8]
li_2 = [5, 8, 9, 7]
testcases = [li_1, li_2]
for item in testcases:
    length = len(item)
    if length % 2 == 0:
        changed_li = item
    #print(changed_li)
    else:
        item.append(0)
        changed_li = item
    #print(changed_li)
    changed_li = sorted(changed_li)
    #print(changed_li)
    #print(changed_li[0::2])
    #print(changed_li[1::2])
    grouped_list = (list(zip(changed_li[0::2],changed_li[1::2])))
    for tuple in grouped_list:
        print(tuple)
