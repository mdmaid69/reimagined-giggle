import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper