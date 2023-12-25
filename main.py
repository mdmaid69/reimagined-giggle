n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper