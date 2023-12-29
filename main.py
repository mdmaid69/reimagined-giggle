import array
def get_array_as_bytearray(array):
        return bytearray(array)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h