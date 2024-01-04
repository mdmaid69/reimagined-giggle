import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)