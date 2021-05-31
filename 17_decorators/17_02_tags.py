'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''
def html_phrase_wrapper(fn):
    def wrapper_func(phrase, p):
        return f"<{p}>" + fn(phrase, p) + f"</{p}>"
    return wrapper_func

@html_phrase_wrapper
def prettify(phrase, p):
    return phrase


print(prettify("My name is Joe","h1"))

