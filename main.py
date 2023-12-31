import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)