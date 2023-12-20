import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)