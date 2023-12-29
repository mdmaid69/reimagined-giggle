import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a