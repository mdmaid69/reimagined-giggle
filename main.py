import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)