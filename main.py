import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)