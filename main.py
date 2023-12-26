import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a