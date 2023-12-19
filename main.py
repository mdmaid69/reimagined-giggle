import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper