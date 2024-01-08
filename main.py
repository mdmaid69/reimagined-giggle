import array
def get_array_index(array, item):
        return array.index(item)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h