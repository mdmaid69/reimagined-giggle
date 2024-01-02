import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper