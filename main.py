import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)