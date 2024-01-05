import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}