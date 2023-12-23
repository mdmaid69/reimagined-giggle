print([x**2 for x in range(10)])
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)