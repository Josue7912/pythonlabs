'''
Write a script with a function that demonstrates the use of **kwargs.

'''
def objectlist(**kwargs):
    for k, v in kwargs.items():
        print(f"{v} is a {k}")

objectlist(clothes="t-shirt", car="Cupra", brand="Zara")