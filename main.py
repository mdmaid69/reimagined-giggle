import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))