import array
def get_array_as_bytearray(array):
        return bytearray(array)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)