import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)