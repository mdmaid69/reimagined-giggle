import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h