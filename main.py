import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)