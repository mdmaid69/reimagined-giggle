import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import array
def get_array_as_memoryview(array):
        return memoryview(array)