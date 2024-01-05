import array
def get_array_as_tuple(array):
        return tuple(array)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)