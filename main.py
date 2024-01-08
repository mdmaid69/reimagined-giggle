import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h