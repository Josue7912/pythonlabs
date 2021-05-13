'''
Write a script with a function that demonstrates the use of *args.

'''
def cities(*args):
    for location in args:
        print(f"* {location}")

cities("London", "Paris", "Madrid", "Budapest")