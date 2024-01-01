import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}