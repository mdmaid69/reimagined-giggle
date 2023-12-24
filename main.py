import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)