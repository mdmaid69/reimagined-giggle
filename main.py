import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper