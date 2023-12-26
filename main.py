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
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)