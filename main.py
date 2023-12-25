import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper