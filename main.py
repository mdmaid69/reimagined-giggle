import array
def append_to_array(array, item):
        array.append(item)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h