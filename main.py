import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def convert_array_to_string(array):
        return array.tostring()