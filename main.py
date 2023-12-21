import array
def set_array_item(array, i, item):
        array[i] = item
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h