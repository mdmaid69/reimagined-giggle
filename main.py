import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)