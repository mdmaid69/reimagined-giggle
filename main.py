import array
def get_array_slice(array, i, j):
        return array[i:j]
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h