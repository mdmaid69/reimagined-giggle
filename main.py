import collections
def create_priority_queue():
        return collections.deque()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)