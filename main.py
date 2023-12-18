import array
def extend_array(array, iterable):
        array.extend(iterable)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h