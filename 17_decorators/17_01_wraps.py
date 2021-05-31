"""
Write a decorator function that wraps text passed to it in a html <p> tag.
"""
def decorator_func(fn):
    def wrapper_func(*args):
        return "<p>" + fn(*args) + "</p>"
    return wrapper_func

@decorator_func
def prettify(phrase):
    return phrase

#phrase = "It's a good day!"

print(prettify("My name is Joe"))