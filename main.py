import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)