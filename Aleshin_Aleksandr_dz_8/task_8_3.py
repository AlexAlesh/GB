from functools import wraps

def logger(func):
    info = {}
    @wraps(func)
    def wrapper(*args):
        nonlocal info
        key = str(*args)
        val = type(*args)
        if key not in info:
            info[key] = val
        return  info
    return wrapper


@logger
def calc(x):
    """func to calculate x ** 3"""
    return x ** 3

a = calc(5)
a1 = calc(6)
print(a)
print(calc.__name__, a)