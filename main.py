import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h