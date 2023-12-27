import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))