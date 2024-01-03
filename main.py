import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)