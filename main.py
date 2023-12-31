import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def get_array_buffer_info(array):
        return array.buffer_info()