import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import array
def get_array_buffer_info(array):
        return array.buffer_info()