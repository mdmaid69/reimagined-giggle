import array
def get_array_as_frozenset(array):
        return frozenset(array)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)