import array
def get_array_itemsize(array):
        return array.itemsize
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h