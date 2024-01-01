import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))