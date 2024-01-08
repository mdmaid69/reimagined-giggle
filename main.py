import array
def reverse_array(array):
        array.reverse()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h