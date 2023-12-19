import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)