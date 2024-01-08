import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)