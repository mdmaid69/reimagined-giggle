import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)