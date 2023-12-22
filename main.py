import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable