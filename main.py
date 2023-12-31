import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)