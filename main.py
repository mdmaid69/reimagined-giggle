import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper