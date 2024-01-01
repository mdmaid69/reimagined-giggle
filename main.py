import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a