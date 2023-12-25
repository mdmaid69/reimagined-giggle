import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h