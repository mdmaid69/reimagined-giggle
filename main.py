import array
def remove_from_array(array, item):
        array.remove(item)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h