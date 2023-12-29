numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper