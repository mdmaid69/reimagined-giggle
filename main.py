import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h