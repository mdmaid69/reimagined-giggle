import array
def get_array_as_memoryview(array):
        return memoryview(array)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)