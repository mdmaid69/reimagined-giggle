import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)