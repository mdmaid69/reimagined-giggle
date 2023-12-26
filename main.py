import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)