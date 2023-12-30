import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)