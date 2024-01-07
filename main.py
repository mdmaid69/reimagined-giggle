import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height