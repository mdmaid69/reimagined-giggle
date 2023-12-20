import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import array
def get_array_as_memoryview(array):
        return memoryview(array)