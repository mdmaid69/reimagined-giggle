import collections
def create_stack():
        return collections.deque()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)