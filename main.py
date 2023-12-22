n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper