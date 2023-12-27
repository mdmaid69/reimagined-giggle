import array
def get_array_as_bytearray(array):
        return bytearray(array)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)