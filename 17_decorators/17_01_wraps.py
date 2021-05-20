"""
Write a decorator function that wraps text passed to it in a html <p> tag.
"""
def decorator_func(fn):
    def wrapper_func(*args):
        return "<p>" + fn(*args) + "</p>"
    return wrapper_func

@decorator_func
def prettify():
    return "flowers for you"

print(prettify())