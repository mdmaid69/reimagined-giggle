import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper