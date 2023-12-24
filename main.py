def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)