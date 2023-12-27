import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"