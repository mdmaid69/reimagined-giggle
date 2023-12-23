import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper