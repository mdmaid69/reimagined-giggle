import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)