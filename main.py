import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a