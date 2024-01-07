import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)