import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)