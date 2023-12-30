import array
def get_array_as_frozenset(array):
        return frozenset(array)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)