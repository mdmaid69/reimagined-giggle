import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a