import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)