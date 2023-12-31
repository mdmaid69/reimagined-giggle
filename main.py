import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)