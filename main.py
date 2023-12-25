import collections
def create_queue():
        return collections.deque()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)