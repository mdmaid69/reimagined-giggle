import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b