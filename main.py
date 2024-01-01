import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)