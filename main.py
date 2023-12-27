import collections
def create_stack():
        return collections.deque()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)