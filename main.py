import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a