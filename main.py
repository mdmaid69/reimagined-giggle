def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper