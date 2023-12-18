import array
def get_array_as_str(array):
        return str(array)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h