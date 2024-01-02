import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def pop_from_array(array, i=-1):
        return array.pop(i)