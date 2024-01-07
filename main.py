import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)