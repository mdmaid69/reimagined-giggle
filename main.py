import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)