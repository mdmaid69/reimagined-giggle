import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)