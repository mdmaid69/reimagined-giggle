import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)