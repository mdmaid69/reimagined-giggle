import array
def clear_array(array):
        array *= 0
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h