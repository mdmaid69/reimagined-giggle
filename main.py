import array
def get_array_as_complex(array):
        return complex(array[0])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h