import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)