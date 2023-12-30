import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper