import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)