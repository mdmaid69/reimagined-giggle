import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)