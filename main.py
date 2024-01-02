import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)