import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)