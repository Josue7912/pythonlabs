'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''
def decorator_func(fn):
    def wrapper_func(*args):
        return "<p>" + fn(*args) + "</p>"
    return wrapper_func

@decorator_func
def prettify():
    return "flowers for you"

print(prettify())