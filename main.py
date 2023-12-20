import array
def get_array_as_frozenset(array):
        return frozenset(array)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)