import array
def get_array_length(array):
        return len(array)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h