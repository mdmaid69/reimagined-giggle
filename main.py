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
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h