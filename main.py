import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper