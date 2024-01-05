import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))