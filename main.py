import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)