import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)