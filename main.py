import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h