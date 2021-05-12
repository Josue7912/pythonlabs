'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
gen = (x for x in range(15000))

for x in gen:
    if x % 1111 == 0:
        print(x//2)

