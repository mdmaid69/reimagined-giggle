import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)