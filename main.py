import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a