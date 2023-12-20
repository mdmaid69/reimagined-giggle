import array
def get_array_as_memoryview(array):
        return memoryview(array)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)