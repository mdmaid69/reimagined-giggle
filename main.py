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
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))