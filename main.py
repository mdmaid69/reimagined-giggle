def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper