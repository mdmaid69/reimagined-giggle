import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)