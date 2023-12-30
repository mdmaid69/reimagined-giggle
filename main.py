import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper