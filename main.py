import array
def get_array_as_int(array):
        return int(array[0])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h