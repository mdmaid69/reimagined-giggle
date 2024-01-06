import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)