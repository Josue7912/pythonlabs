'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

month = int(input("Enter your number: "))

if(month==1):
    print("{} is equivalent to January".format(month))
elif(month==2):
    print("{} is equivalent to February".format(month))
elif(month==3):
    print("{} is equivalent to March".format(month))
elif(month==4):
    print("{} is equivalent to April".format(month))
elif(month==5):
    print("{} is equivalent to May".format(month))
elif(month==6):
    print("{} is equivalent to June".format(month))
elif(month==7):
    print("{} is equivalent to July".format(month))
elif(month==8):
    print("{} is equivalent to August".format(month))
elif(month==9):
    print("{} is equivalent to September".format(month))
elif(month==10):
    print("{} is equivalent to October".format(month))
elif(month==11):
    print("{} is equivalent to November".format(month))
elif(month==12):
    print("{} is equivalent to December".format(month))
else:
    print("{} is equivalent to Other".format(month))