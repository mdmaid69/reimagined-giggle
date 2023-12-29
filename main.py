import array
def get_array_as_float(array):
        return float(array[0])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h